# python /workspaces/SonarQube/6_Symbols/1_Init/create_packing_folder_contents.py
import openai
import os
from dotenv import load_dotenv
import pathlib

# Configuration settings
CONFIG = {
    'BASE_DIR': '8_Packing',
    'MODEL': 'gpt-4',
    'MAX_TOKENS': 2000,
    'MODULES_COUNT': 3,
    'SCRIPT_LENGTH': '4 minute'
    'SCRIPT_TITLE': 'Code Quality With SonarQube',
    'SCRIPT_DESCRIPTION': 'Learn how to improve code quality using SonarQube.',
    'SCRIPT_LEARNING_OBJECTIVES': [
        'Create SonarQube Environment',
        'Scan a code base with SonarQube',
        'Integrate CI/CD with SonarQube'
    ],
    'SCRIPT_AUDIENCE': 'Software developers, team leads, and project managers,devops',
    'SCRIPT_FORMAT': 'Video tutorial',
    'SCRIPT_DURATION': '60 minutes',
    'SCRIPT_LANGUAGE': 'English',
    'SCRIPT_LEVEL': 'Intermediate',
    'SCRIPT_PLATFORM': 'YouTube',
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
    'SCRIPT_DATE': '2023-10-01',
    'SCRIPT_AUTHOR': 'Rifat Erdem Sahin'
}

# Load environment variables
load_dotenv()

def call_gpt(prompt):
    """
    Call the OpenAI GPT model with the given prompt.
    """
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=CONFIG['MODEL'],
        messages=[{"role": "user", "content": prompt}],
        max_tokens=CONFIG['MAX_TOKENS']
    )
    return response.choices[0].message.content

def generate_outline(topic):
    """Generate a course outline for the given topic."""
    return call_gpt(f"Create a {CONFIG['MODULES_COUNT']}-module course outline : {topic}")

def generate_script(module_title):
    """Generate a script for a module."""
    return call_gpt(f"Write a {CONFIG['SCRIPT_LENGTH']} script for the module: {module_title}")

def generate_shot_list(script):
    """Generate a shot list from a script."""
    return call_gpt(f"Create a shot list from this script:\n{script}")

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
    if not os.path.exists(CONFIG['BASE_DIR']):
        os.makedirs(CONFIG['BASE_DIR'])
    
    # Generate course outline
    outline = generate_outline(topic)
    create_file(os.path.join(CONFIG['BASE_DIR'], "outline.md"), outline)
    
    # Parse outline to extract module titles
    module_titles = []
    for line in outline.split('\n'):
        if "Module" in line and ":" in line:
            module_title = line.split(":")[1].strip()
            module_titles.append(module_title)
    
    # Generate and save content for each module
    for i, title in enumerate(module_titles, 1):
        module_dir = os.path.join(CONFIG['BASE_DIR'], f"module_{i}")
        
        script = generate_script(title)
        script_path = os.path.join(module_dir, "script.md")
        create_file(script_path, script)
        
        shot_list = generate_shot_list(script)
        shot_list_path = os.path.join(module_dir, "shot_list.md")
        create_file(shot_list_path, shot_list)

if __name__ == "__main__":
    topic = CONFIG['SCRIPT_TITLE']
    generate_full_course(topic)
