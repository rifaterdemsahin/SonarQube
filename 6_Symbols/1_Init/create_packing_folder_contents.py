# python /workspaces/SonarQube/6_Symbols/1_Init/create_packing_folder_contents.py
import openai
import os
from dotenv import load_dotenv
import pathlib
import json

# Configuration settings
CONFIG = {
    'BASE_DIR': '8_Packing',
    'MODEL': 'gpt-4',
    'MAX_TOKENS': 2000,
    'MODULES_COUNT': 3,
    'SCRIPT_LENGTH': '4 minute',
    'SCRIPT_TITLE': 'Code Quality With SonarQube',
    'SCRIPT_DESCRIPTION': 'Learn how to improve code quality using SonarQube.',
    'SCRIPT_LEARNING_OBJECTIVES': [
        'LEARNING OBJECTIVE 1 : Create SonarQube Environment',
        'LEARNING OBJECTIVE 2 :Scan a code base with SonarQube',
        'LEARNING OBJECTIVE 3 :Integrate CI/CD with SonarQube'
    ],
    'SCRIPT_INTRO': 'Welcome this is Erdem I worked in Accenture in charge of SonarQube for a banking application calculated technical debt with reached million man days',
    'SCRIPT_LEARNING_OBJECTIVE_1_VIDEO1': 'Create Codespaces Environment',
    'SCRIPT_LEARNING_OBJECTIVE_1_VIDEO2': 'Create a Github repository',
    'SCRIPT_LEARNING_OBJECTIVE_1_VIDEO3': 'Create SonarQube Environment in Minikube',
    'SCRIPT_LEARNING_OBJECTIVE_1_HANDSONEXERCISE': 'Create your github account and create a repository, Duration 25 minutes',
    'SCRIPT_LEARNING_OBJECTIVE_2_VIDEO1': 'Create github app',
    'SCRIPT_LEARNING_OBJECTIVE_2_VIDEO2': 'Give access to the app',
    'SCRIPT_LEARNING_OBJECTIVE_2_VIDEO3': 'Scan one repo with SonarQube',
    'SCRIPT_LEARNING_OBJECTIVE_2_HANDSONEXERCISE': 'Create your repository account and scan with SonarQube, Duration 25 minutes',   
    'SCRIPT_LEARNING_OBJECTIVE_3_VIDEO1': 'Create a github actions and a pipeline',
    'SCRIPT_LEARNING_OBJECTIVE_3_VIDEO2': 'Link Actions to SonarQube',
    'SCRIPT_LEARNING_OBJECTIVE_3_VIDEO3': 'Continus integration cycle and improve code quality',
    'SCRIPT_LEARNING_OBJECTIVE_3_HANDSONEXERCISE': 'Create a pipeline and add sonarqube step in it, Duration 25 minutes',   
    'SCRIPT_OUTRO': 'Thanks for joining in it would be great if you apply the necessary hands on exercises to get the most out of it',   
    'SCRIPT_AUDIENCE': 'Software developers, DevOps engineers, and QA professionals',
    'SCRIPT_TARGET_AUDIENCE': 'Software developers, DevOps engineers, and QA professionals',
    'SCRIPT_FORMAT': 'Video tutorial',
    'SCRIPT_DURATION': '60 minutes',
    'SCRIPT_LANGUAGE': 'English',
    'SCRIPT_LEVEL': 'Intermediate',
    'SCRIPT_PLATFORM': 'CourseEra',
    'SCRIPT_VISUALS': 'Screen recordings, slides, and code examples',
    'SCRIPT_AUDIO': 'Voiceover narration',
    'SCRIPT_SUBTITLES': 'English subtitles',
    'SCRIPT_CALL_TO_ACTION': 'Subscribe for more tutorials',
    'SCRIPT_FEEDBACK': 'Please provide feedback in the comments section.',
    'SCRIPT_RESOURCES': [
        'SonarQube official documentation',
        'GitHub repository with code examples',
        'Links to relevant articles and tutorials'
    ],
    'SCRIPT_FOOTER': 'Thank you for watching!',
    'SCRIPT_CREDITS': 'Produced by Rifat Erdem Sahin',
    'SCRIPT_LICENSE': 'Creative Commons Attribution-ShareAlike 4.0 International License',
    'SCRIPT_VERSION': '1.0',
    'SCRIPT_DATE': 'Today',
    'SCRIPT_AUTHOR': 'Rifat Erdem Sahin',
    'FILENAME_PREFIX': '8.1.1.'
    
}

# Load environment variables
load_dotenv()

def call_gpt(prompt):
    """Call the OpenAI GPT model with the given prompt."""
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=CONFIG['MODEL'],
        messages=[{"role": "user", "content": prompt}],
        max_tokens=CONFIG['MAX_TOKENS']
    )
    return response.choices[0].message.content

def generate_outline(topic):
    """Generate a course outline for the given topic."""
    prompt = f"""
    Create a detailed {CONFIG['MODULES_COUNT']}-module course outline for a course titled: "{topic}"
    
    Course details:
    - Description: {CONFIG['SCRIPT_DESCRIPTION']}
    - Audience: {CONFIG['SCRIPT_AUDIENCE']}
    - Level: {CONFIG['SCRIPT_LEVEL']}
    - Format: {CONFIG['SCRIPT_FORMAT']}
    - Duration: {CONFIG['SCRIPT_DURATION']}
    
    Learning objectives:
    {', '.join(CONFIG['SCRIPT_LEARNING_OBJECTIVES'])}
    
    Each module should focus on one major aspect of {topic} and include:
    1. Module title
    2. Key topics covered
    3. A brief description
    
    Format the outline in Markdown.
    """
    return call_gpt(prompt)

def generate_script(module_title, module_number, total_modules):
    """Generate a script for a module."""
    prompt = f"""
    Write a {CONFIG['SCRIPT_LENGTH']} script for Module {module_number} of {total_modules}: "{module_title}"
    
    Course information:
    - Course title: {CONFIG['SCRIPT_TITLE']}
    - Description: {CONFIG['SCRIPT_DESCRIPTION']}
    - Audience: {CONFIG['SCRIPT_AUDIENCE']}
    - Level: {CONFIG['SCRIPT_LEVEL']}
    - Format: {CONFIG['SCRIPT_FORMAT']}
    
    Script should include:
    - Introduction to the module
    - Clear explanations of concepts
    - Practical examples or demonstrations
    - Summary of key points
    - Transition to the next module (if not the final module)
    
    The script should be suitable for {CONFIG['SCRIPT_VISUALS']} and {CONFIG['SCRIPT_AUDIO']}.
    Format the script in Markdown with clear section headers and speaker notes.
    """
    return call_gpt(prompt)

def generate_shot_list(script, module_title):
    """Generate a shot list from a script."""
    prompt = f"""
    Create a detailed shot list from this script for the module "{module_title}":
    
    {script}
    
    The shot list should include:
    1. Shot number
    2. Shot type (Talking head,screen capture, slides)
    3. Description of what is shown visually
    4. Script excerpt or narration for that shot
    5. Duration estimate for each shot
    
    Visual requirements:
    - {CONFIG['SCRIPT_VISUALS']}
    
    Format the shot list in a clean, organized table using Markdown.
    """
    return call_gpt(prompt)

def create_file(file_path, content):
    """Create a file with the given content."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created file: {file_path}")

def generate_full_course(topic):
    """Generate a full course and save files."""
    base_dir = CONFIG['BASE_DIR']
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Save configuration
    config_path = os.path.join(base_dir, "config.json")
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(CONFIG, f, indent=4)
    print(f"Created file: {config_path}")
    
    # Generate course metadata
    metadata = f"""# {topic}

## Course Information
- **Description:** {CONFIG['SCRIPT_DESCRIPTION']}
- **Audience:** {CONFIG['SCRIPT_AUDIENCE']}
- **Level:** {CONFIG['SCRIPT_LEVEL']}
- **Format:** {CONFIG['SCRIPT_FORMAT']}
- **Duration:** {CONFIG['SCRIPT_DURATION']}
- **Language:** {CONFIG['SCRIPT_LANGUAGE']}
- **Platform:** {CONFIG['SCRIPT_PLATFORM']}

## Learning Objectives
{chr(10).join(['- ' + obj for obj in CONFIG['SCRIPT_LEARNING_OBJECTIVES']])}

## Resources
{chr(10).join(['- ' + res for res in CONFIG['SCRIPT_RESOURCES']])}

## Credits
- **Author:** {CONFIG['SCRIPT_AUTHOR']}
- **Version:** {CONFIG['SCRIPT_VERSION']}
- **Date:** {CONFIG['SCRIPT_DATE']}
- **License:** {CONFIG['SCRIPT_LICENSE']}
"""
    metadata_path = os.path.join(base_dir, "metadata.md")
    create_file(metadata_path, metadata)
    
    # Generate and save course outline in a single file
    outline = generate_outline(topic)
    outline_path = os.path.join(base_dir, "course_outline.md")
    create_file(outline_path, outline)
    
    # Parse outline to extract module titles
    module_titles = []
    for line in outline.split('\n'):
        if "Module" in line and ":" in line:
            module_title = line.split(":")[1].strip()
            module_titles.append(module_title)
    
    # If parsing failed, create default module titles
    if not module_titles or len(module_titles) < CONFIG['MODULES_COUNT']:
        module_titles = [f"Module {i+1}: {obj}" for i, obj in enumerate(CONFIG['SCRIPT_LEARNING_OBJECTIVES'])]
        if len(module_titles) > CONFIG['MODULES_COUNT']:
            module_titles = module_titles[:CONFIG['MODULES_COUNT']]
    
    # Generate and save content for each module
    scripts_dir = os.path.join(base_dir, "scripts")
    shot_lists_dir = os.path.join(base_dir, "shot_lists")
    
    for i, title in enumerate(module_titles, 1):
        # Generate script and save in scripts directory
        script = generate_script(title, i, len(module_titles))
        script_filename = f"module_{i}_script.md"
        script_path = os.path.join(scripts_dir, script_filename)
        create_file(script_path, script)
        
        # Generate shot list and save in shot_lists directory
        shot_list = generate_shot_list(script, title)
        shot_list_filename = f"module_{i}_shot_list.md"
        shot_list_path = os.path.join(shot_lists_dir, shot_list_filename)
        create_file(shot_list_path, shot_list)
    
    # Generate README
    readme = f"""# {topic} Course Materials

This repository contains materials for the "{topic}" course.

## Contents
- [Course Metadata](metadata.md)
- [Course Outline](course_outline.md)
- [Scripts Directory](scripts/)
- [Shot Lists Directory](shot_lists/)
{chr(10).join(['- [Module ' + str(i) + ': ' + title + '](scripts/module_' + str(i) + '_script.md)' for i, title in enumerate(module_titles, 1)])}

## Description
{CONFIG['SCRIPT_DESCRIPTION']}

## Author
{CONFIG['SCRIPT_AUTHOR']}

## License
{CONFIG['SCRIPT_LICENSE']}
"""
    readme_path = os.path.join(base_dir, "README.md")
    create_file(readme_path, readme)

if __name__ == "__main__":
    topic = CONFIG['SCRIPT_TITLE']
    generate_full_course(topic)