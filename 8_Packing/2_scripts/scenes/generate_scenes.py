#!/usr/bin/env python3

import sys
import yaml
import os
from pathlib import Path
import re
from typing import Dict, List, Any, Optional

def slugify(text: str) -> str:
    """Convert text to URL-friendly slug.
    
    Args:
        text (str): Text to convert to slug
        
    Returns:
        str: URL-friendly slug
    """
    # Remove special characters and convert to lowercase
    text = text.lower()
    # Replace spaces and special characters with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

def validate_metadata(data: Dict[str, Any]) -> None:
    """Validate required fields in metadata.
    
    Args:
        data (Dict[str, Any]): Metadata dictionary to validate
        
    Raises:
        ValueError: If required fields are missing or invalid
    """
    required_fields = {
        'scene': int,
        'title': str,
        'video_id': str,
        'intro_talking_head': str,
        'slides': str,
        'screen_capture': str,
        'summary_talking_head': str
    }
    
    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    
    # Validate field types
    for field, expected_type in required_fields.items():
        if not isinstance(data[field], expected_type):
            raise ValueError(f"Field '{field}' must be of type {expected_type.__name__}")
    
    # Validate scene number range
    if not 1 <= data['scene'] <= 15:
        raise ValueError("Scene number must be between 1 and 15")
    
    # Validate video ID format
    if not re.match(r'^SQ_\d{3}$', data['video_id']):
        raise ValueError("Video ID must be in format 'SQ_XXX' where XXX is a 3-digit number")

def get_learning_objectives(scene_num: int) -> str:
    """Get learning objectives based on scene number.
    
    Args:
        scene_num (int): Scene number (1-15)
        
    Returns:
        str: Formatted learning objectives
    """
    setup_objectives = {
        1: "Understand SonarQube's core features and benefits",
        2: "Learn how to create and configure a new project",
        3: "Master SonarQube server installation and setup",
        4: "Configure quality gates and project settings",
        5: "Understand basic code quality metrics"
    }
    
    integration_objectives = {
        6: "Learn to integrate SonarQube with development workflows",
        7: "Master code quality analysis and issue resolution",
        8: "Configure custom quality profiles and rules",
        9: "Set up team collaboration features",
        10: "Integrate SonarQube with CI/CD pipelines"
    }
    
    scanning_objectives = {
        11: "Implement custom rules and plugins",
        12: "Perform system maintenance and optimization",
        13: "Troubleshoot common issues and errors",
        14: "Apply security scanning best practices",
        15: "Implement long-term quality improvement strategies"
    }
    
    objectives = []
    if scene_num in setup_objectives:
        objectives.append(f"1. {setup_objectives[scene_num]}")
    if scene_num in integration_objectives:
        objectives.append(f"2. {integration_objectives[scene_num]}")
    if scene_num in scanning_objectives:
        objectives.append(f"3. {scanning_objectives[scene_num]}")
    
    return "\n".join(objectives)

def format_section_content(content: str) -> str:
    """Format section content with proper indentation and line breaks.
    
    Args:
        content (str): Raw content to format
        
    Returns:
        str: Formatted content
    """
    # Split into lines and remove empty lines
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    # Join with proper spacing
    return '\n\n'.join(lines)

def generate_markdown(data: Dict[str, Any]) -> str:
    """Generate markdown content from metadata.
    
    Args:
        data (Dict[str, Any]): Scene metadata
        
    Returns:
        str: Generated markdown content
    """
    scene_num = data['scene']
    title = data['title']
    video_id = data['video_id']
    
    # Format scene number with leading zero
    num_str = f"{scene_num:02}"
    
    # Get learning objectives
    learning_objectives = get_learning_objectives(scene_num)
    
    # Format section contents
    intro = format_section_content(data['intro_talking_head'])
    slides = format_section_content(data['slides'])
    screen_capture = format_section_content(data['screen_capture'])
    summary = format_section_content(data['summary_talking_head'])
    
    # Create footer HTML with smaller font
    footer = f"""
<div style="position: fixed; bottom: 20px; right: 20px; text-align: right; font-size: 0.8em; color: #666;">
<p style="margin: 0;">Page {scene_num}/15</p>
<p style="margin: 0;">Video ID: {video_id}</p>
<p style="margin: 0;">Learning Objectives:</p>
{learning_objectives.replace('\\n', '<br>')}
</div>
"""
    
    # Create script sections
    def create_script_sections(section_name: str) -> str:
        return f"""
### Script for Course Creator
- Mention scene {num_str} and {section_name}

### Script for Instructor Read
- Read the following script while recording:
- "Welcome to Scene {num_str} of our SonarQube course. {section_name}"
"""
    
    # Generate markdown content with footer and scripts after each section
    content = f"""# Scene {num_str} – {title}
Video ID: {video_id}

## Learning Objectives
{learning_objectives}

{create_script_sections("introduce the learning objectives")}

{footer}

---

## 1. 🎥 Intro Talking Head
Mention the scene number and tell the audience about:

{intro}

{create_script_sections("introduce the key points")}

{footer}

---

## 2. 📊 Slides
Mention the scene number and show:

{slides}

{create_script_sections("present the visual content")}

{footer}

---

## 3. 🖥️ Screen Capture (Map Interaction)
Mention the scene number and do:

{screen_capture}

{create_script_sections("demonstrate the interactive elements")}

{footer}

---

## 4. 🎬 Summary Talking Head
Mention the scene number and summarize:

{summary}

{create_script_sections("summarize the main takeaways")}

{footer}
"""
    return content

def process_yaml_file(file_path: str) -> Dict[str, Any]:
    """Process YAML file and return metadata.
    
    Args:
        file_path (str): Path to YAML file
        
    Returns:
        Dict[str, Any]: Parsed metadata
        
    Raises:
        yaml.YAMLError: If YAML parsing fails
        ValueError: If metadata validation fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        validate_metadata(data)
        return data
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    except ValueError as e:
        raise ValueError(f"Validation error: {e}")

def main(file_path: str) -> None:
    """Main function to process YAML and generate markdown.
    
    Args:
        file_path (str): Path to YAML metadata file
    """
    try:
        # Process YAML file
        data = process_yaml_file(file_path)
        
        # Generate markdown content
        content = generate_markdown(data)
        
        # Create scenes directory if it doesn't exist
        scenes_dir = Path('scenes')
        scenes_dir.mkdir(exist_ok=True)
        
        # Generate output filename
        filename = scenes_dir / f"scene{data['scene']:02}-{slugify(data['title'])}.md"
        
        # Write markdown file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully generated: {filename}")
        
    except (yaml.YAMLError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate-scene-md.py metadata/sceneXX.yaml")
        sys.exit(1)
    main(sys.argv[1])