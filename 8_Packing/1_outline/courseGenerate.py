"""
Course Metadata Generator

This system orchestrates the generation of course metadata using a configured pipeline 
where outputs from earlier steps are passed to later steps. It supports:
1. Dynamic field dependencies
2. Consistency preservation
3. Variation control
4. Instructional intent preservation
"""

import os
import yaml
import json
import logging
import openai
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('course_metadata_generator')

class CourseMetadataGenerator:
    def __init__(self, config_path: str):
        """Initialize with a YAML configuration file."""
        self.config = self._load_config(config_path)
        self._setup_openai()
        self.outputs = {}
        self.metadata_history = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load the YAML configuration file."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logger.info(f"Loaded configuration from {config_path}")
        return config
    
    def _setup_openai(self):
        """Setup OpenAI client."""
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
    def generate_metadata(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate course metadata following the pipeline defined in the configuration.
        
        Args:
            input_data: Initial metadata and context for generation
            
        Returns:
            Dict containing the generated course metadata
        """
        self.outputs = input_data.copy()
        pipeline = self.config['pipeline']
        
        # Process each pipeline step in order
        for step in pipeline:
            step_id = step['id']
            logger.info(f"Processing step: {step_id}")
            
            # Check dependencies for this step
            self._check_dependencies(step)
            
            # Generate content for this step
            result = self._process_step(step)
            
            # Store the result
            self.outputs[step_id] = result
            
            # Save intermediate result if configured
            if step.get('save_output', False):
                self._save_intermediate_output(step_id, result)
        
        # Compile final metadata
        final_metadata = self._compile_final_metadata()
        self._save_final_metadata(final_metadata)
        
        return final_metadata
    
    def _check_dependencies(self, step: Dict):
        """Check if all dependencies for a step are available."""
        if 'depends_on' in step:
            for dependency in step['depends_on']:
                if dependency not in self.outputs:
                    raise ValueError(f"Missing dependency '{dependency}' for step '{step['id']}'")
    
    def _process_step(self, step: Dict) -> Any:
        """Process a single pipeline step."""
        # Get the processor for this step
        processor_type = step.get('processor', 'gpt')
        
        if processor_type == 'gpt':
            return self._process_gpt_step(step)
        elif processor_type == 'template':
            return self._process_template_step(step)
        elif processor_type == 'python':
            return self._process_python_step(step)
        else:
            raise ValueError(f"Unknown processor type: {processor_type}")
    
    def _process_gpt_step(self, step: Dict) -> str:
        """Process a step using GPT."""
        # Prepare prompt with dependencies
        prompt = step['prompt']
        
        # Replace template variables with values from previous steps
        for var_name, var_value in self.outputs.items():
            placeholder = f"{{{{{var_name}}}}}"
            if placeholder in prompt:
                if isinstance(var_value, dict):
                    # Format dictionary as YAML or JSON
                    var_value = yaml.dump(var_value) if step.get('format', 'yaml') == 'yaml' else json.dumps(var_value, indent=2)
                prompt = prompt.replace(placeholder, str(var_value))
        
        # Add system prompt if provided
        system_prompt = step.get('system_prompt', self.config.get('default_system_prompt', ''))
        
        # Call GPT
        model = step.get('model', self.config.get('default_model', 'gpt-4-turbo'))
        temperature = step.get('temperature', self.config.get('default_temperature', 0.7))
        
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=step.get('max_tokens', 2000)
            )
            result = response.choices[0].message.content
            
            # Parse result if needed
            if step.get('parse_json', False):
                result = json.loads(result)
            elif step.get('parse_yaml', False):
                result = yaml.safe_load(result)
                
            return result
        
        except Exception as e:
            logger.error(f"Error in GPT step '{step['id']}': {str(e)}")
            raise
    
    def _process_template_step(self, step: Dict) -> str:
        """Process a template step by filling in variables."""
        template = step['template']
        result = template
        
        # Replace template variables with values from previous steps
        for var_name, var_value in self.outputs.items():
            placeholder = f"{{{{{var_name}}}}}"
            if placeholder in result:
                result = result.replace(placeholder, str(var_value))
                
        return result
    
    def _process_python_step(self, step: Dict) -> Any:
        """Execute Python code for custom processing."""
        code = step['code']
        local_vars = {'outputs': self.outputs, 'step': step}
        
        try:
            exec(code, globals(), local_vars)
            return local_vars.get('result', None)
        except Exception as e:
            logger.error(f"Error in Python step '{step['id']}': {str(e)}")
            raise

    def _save_intermediate_output(self, step_id: str, result: Any):
        """Save intermediate output to file."""
        output_dir = Path(self.config.get('output_directory', 'outputs'))
        output_dir.mkdir(exist_ok=True, parents=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = output_dir / f"{step_id}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            if isinstance(result, (dict, list)):
                json.dump(result, f, indent=2)
            else:
                json.dump({"content": str(result)}, f, indent=2)
        
        logger.info(f"Saved intermediate output for step '{step_id}' to {filename}")
    
    def _compile_final_metadata(self) -> Dict:
        """Compile the final metadata from all outputs."""
        output_fields = self.config.get('output_fields', [])
        final_metadata = {}
        
        for field in output_fields:
            field_name = field['name']
            source = field['source']
            
            if source in self.outputs:
                if field.get('is_property', False) and isinstance(self.outputs[source], dict):
                    # Extract a property from a dictionary
                    prop_path = field.get('property_path', field_name).split('.')
                    value = self.outputs[source]
                    for prop in prop_path:
                        if isinstance(value, dict) and prop in value:
                            value = value[prop]
                        else:
                            value = None
                            break
                    final_metadata[field_name] = value
                else:
                    final_metadata[field_name] = self.outputs[source]
        
        return final_metadata
    
    def _save_final_metadata(self, metadata: Dict):
        """Save the final metadata to a file."""
        output_dir = Path(self.config.get('output_directory', 'outputs'))
        output_dir.mkdir(exist_ok=True, parents=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = output_dir / f"course_metadata_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        logger.info(f"Saved final metadata to {filename}")


# Example YAML Configuration
example_config = """
# Course Metadata Generation Pipeline Configuration
name: "Course Metadata Generator"
version: "1.0"
default_model: "gpt-4-turbo"
default_temperature: 0.7
default_system_prompt: "You are an expert educational curriculum designer tasked with creating metadata for an online course."
output_directory: "outputs"

# Pipeline definition
pipeline:
  - id: "course_title"
    description: "Generate a compelling course title"
    processor: "gpt"
    model: "gpt-4-turbo"
    temperature: 0.8
    prompt: |
      Based on the following course topic and audience information, generate a compelling course title.
      
      Topic: {{topic}}
      Target Audience: {{audience}}
      Learning Goals: {{learning_goals}}
      
      The title should be concise (5-8 words), engaging, and clearly convey the value proposition of the course.
      Return ONLY the title without any explanation or formatting.
    save_output: true
  
  - id: "course_description"
    description: "Generate a course description"
    depends_on: ["course_title"]
    processor: "gpt"
    temperature: 0.7
    prompt: |
      Create a compelling course description for the following course:
      
      Course Title: {{course_title}}
      Topic: {{topic}}
      Target Audience: {{audience}}
      Learning Goals: {{learning_goals}}
      
      The description should be 2-3 paragraphs (150-200 words) that:
      1. Explains what the student will learn
      2. Highlights the practical applications
      3. Creates a sense of urgency or importance
      4. Uses conversational, engaging language
      
      Return ONLY the description without any explanation or formatting.
    save_output: true
  
  - id: "learning_objectives"
    description: "Generate learning objectives"
    depends_on: ["course_title", "course_description"]
    processor: "gpt"
    prompt: |
      Based on the following course information, generate 4-6 specific learning objectives:
      
      Course Title: {{course_title}}
      Course Description: {{course_description}}
      Topic: {{topic}}
      Learning Goals: {{learning_goals}}
      
      Each learning objective should:
      1. Start with an action verb (e.g., "Analyze", "Create", "Implement")
      2. Be specific and measurable
      3. Focus on what the learner will be able to do after completing the course
      4. Align with the overall learning goals
      
      Format the output as a JSON array of strings.
    parse_json: true
    save_output: true
  
  - id: "course_outline" 
    description: "Generate a course outline"
    depends_on: ["course_title", "course_description", "learning_objectives"]
    processor: "gpt"
    prompt: |
      Create a detailed course outline for:
      
      Course Title: {{course_title}}
      Course Description: {{course_description}}
      Learning Objectives: {{learning_objectives}}
      
      The course should have 4-6 modules, each with:
      1. A descriptive title
      2. 3-5 lessons per module
      3. Estimated time to complete each module (in minutes)
      4. Learning objectives addressed by the module
      
      Output the result as structured JSON in the following format:
      ```json
      {
        "modules": [
          {
            "title": "Module Title",
            "estimated_time_minutes": 60,
            "learning_objectives_addressed": [0, 1],
            "lessons": [
              {
                "title": "Lesson Title",
                "description": "Brief description of the lesson content"
              }
            ]
          }
        ]
      }
      ```
    parse_json: true
    save_output: true
  
  - id: "prerequisites"
    description: "Identify prerequisites"
    depends_on: ["course_title", "learning_objectives", "course_outline"]
    processor: "gpt"
    temperature: 0.5
    prompt: |
      Based on the following course information, identify any prerequisites or prior knowledge that would help students succeed in this course:
      
      Course Title: {{course_title}}
      Learning Objectives: {{learning_objectives}}
      Course Outline: {{course_outline}}
      
      Consider:
      1. Technical skills or knowledge required
      2. Experience level recommended
      3. Tools or software familiarity needed
      
      Format your response as a JSON array of strings, with each prerequisite as a separate item.
      If no prerequisites are necessary, return an empty array.
    parse_json: true
    save_output: true
  
  - id: "keywords"
    description: "Generate relevant keywords"
    depends_on: ["course_title", "course_description", "learning_objectives"]
    processor: "gpt"
    temperature: 0.6
    prompt: |
      Generate 10-15 relevant keywords and phrases for the following course:
      
      Course Title: {{course_title}}
      Course Description: {{course_description}}
      Learning Objectives: {{learning_objectives}}
      
      These keywords should:
      1. Include important technical terms covered in the course
      2. Reflect skills that will be developed
      3. Include terms that potential students might search for
      4. Vary in specificity (some broad, some specific)
      
      Format the output as a JSON array of strings.
    parse_json: true
    save_output: true
  
  - id: "difficulty_level"
    description: "Determine course difficulty level"
    depends_on: ["learning_objectives", "prerequisites", "course_outline"]
    processor: "python"
    code: |
      # Analyze complexity of prerequisites and learning objectives
      def calculate_difficulty(outputs):
          prereqs = outputs.get('prerequisites', [])
          objectives = outputs.get('learning_objectives', [])
          outline = outputs.get('course_outline', {})
          
          # Count advanced terms in prerequisites
          advanced_term_count = 0
          technical_prereqs = 0
          for prereq in prereqs:
              if any(term in prereq.lower() for term in ['advanced', 'expert', 'proficient', 'experience']):
                  advanced_term_count += 1
              if any(term in prereq.lower() for term in ['technical', 'programming', 'code', 'software']):
                  technical_prereqs += 1
          
          # Analyze learning objective complexity
          complex_objectives = 0
          for obj in objectives:
              if any(verb in obj.lower() for verb in ['analyze', 'evaluate', 'create', 'develop', 'design', 'implement']):
                  complex_objectives += 1
          
          # Calculate module depth
          modules = outline.get('modules', [])
          avg_lessons_per_module = sum(len(m.get('lessons', [])) for m in modules) / max(len(modules), 1)
          
          # Determine difficulty
          difficulty_score = (advanced_term_count * 2) + technical_prereqs + complex_objectives + (avg_lessons_per_module / 2)
          
          if difficulty_score < 3:
              return "Beginner"
          elif difficulty_score < 7:
              return "Intermediate"
          else:
              return "Advanced"
      
      result = calculate_difficulty(outputs)
    save_output: true
  
  - id: "estimated_completion_time"
    description: "Calculate estimated completion time"
    depends_on: ["course_outline"]
    processor: "python"
    code: |
      # Calculate total estimated time from module times
      course_outline = outputs.get('course_outline', {})
      modules = course_outline.get('modules', [])
      
      total_minutes = sum(m.get('estimated_time_minutes', 0) for m in modules)
      
      # Add 20% buffer for exercises, quizzes, etc.
      total_minutes = int(total_minutes * 1.2)
      
      # Format the result
      hours = total_minutes // 60
      minutes = total_minutes % 60
      
      result = {
          "total_minutes": total_minutes,
          "formatted": f"{hours} hours {minutes} minutes" if minutes else f"{hours} hours"
      }
    save_output: true

# Define which fields make up the final metadata
output_fields:
  - name: "title"
    source: "course_title"
  - name: "description"
    source: "course_description"
  - name: "learning_objectives"
    source: "learning_objectives"
  - name: "outline"
    source: "course_outline"
  - name: "prerequisites"
    source: "prerequisites"
  - name: "keywords"
    source: "keywords"
  - name: "difficulty_level"
    source: "difficulty_level"
  - name: "estimated_completion_time"
    source: "estimated_completion_time"
    is_property: true
    property_path: "formatted"
"""

# Function to save example configuration
def save_example_config(output_path="course_metadata_config.yaml"):
    with open(output_path, "w") as f:
        f.write(example_config)
    print(f"Example configuration saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Save example configuration
    save_example_config()
    
    # Example input data
    input_data = {
      r#]e'
      
        "topic": "Introduction to Machine Learning with Python",
        "audience": "Software developers with basic Python knowledge looking to expand their skills into AI and machine learning.",
        "learning_goals": "Understand core ML concepts, implement basic algorithms, evaluate model performance, and build practical ML applications."
    }
    
    # Generate metadata
    generator = CourseMetadataGenerator("course_metadata_config.yaml")
    metadata = generator.generate_metadata(input_data)
    
    print("\nGenerated Course Metadata:")Ꝡ
