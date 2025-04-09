# python /workspaces/SonarQube/6_Symbols/1_Init/create_packing_folder_contents.py
import openai
import os
from dotenv import load_dotenv
import pathlib

# Load environment variables
load_dotenv()

def call_gpt(prompt):
    """
    Call the OpenAI GPT model with the given prompt.
    
    Args:
        prompt (str): The text prompt to send to the model
        
    Returns:
        str: The generated response
    """
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content

def generate_outline(topic):
    """
    Generate a 5-module course outline for the given topic.
    
    Args:
        topic (str): The course topic
        
    Returns:
        str: A 5-module course outline
    """
    return call_gpt("Create a 3-module course outline : " + topic)

def generate_script(module_title):
    """
    Generate a script for a module.
    
    Args:
        module_title (str): The title of the module
        
    Returns:
        str: A 4 minute script for the module
    """
    return call_gpt(f"Write a 4 minute script for the module: {module_title}")

def generate_shot_list(script):
    """
    Generate a shot list from a script.
    
    Args:
        script (str): The module script
        
    Returns:
        str: A shot list based on the script
    """
    return call_gpt(f"Create a shot list from this script:\n{script}")

def create_file(file_path, content):
    """
    Create a file with the given content.
    
    Args:
        file_path (str): The path for the file
        content (str): The content to be written to the file
    """
    # Create directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        
    # Write content to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created file: {file_path}")

def generate_full_course(topic):
    """
    Generate a full course and save files to the 8_Packing folder.
    
    Args:
        topic (str): The course topic
    """
    base_dir = "8_Packing"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Generate course outline
    outline = generate_outline(topic)
    create_file(os.path.join(base_dir, "outline.md"), outline)
    
    # Parse outline to extract module titles
    module_titles = []
    for line in outline.split('\n'):
        if "Module" in line and ":" in line:
            module_title = line.split(":")[1].strip()
            module_titles.append(module_title)
    
    # Generate and save content for each module
    for i, title in enumerate(module_titles, 1):
        module_dir = os.path.join(base_dir, f"module_{i}")
        
        # Generate script
        script = generate_script(title)
        script_path = os.path.join(module_dir, "script.md")
        create_file(script_path, script)
        
        # Generate shot list
        shot_list = generate_shot_list(script)
        shot_list_path = os.path.join(module_dir, "shot_list.md")
        create_file(shot_list_path, shot_list)

# Example usage
if __name__ == "__main__":
    # Check if .env file exists, create if it doesn't
    env_path = ".env"
    if not os.path.exists(env_path):
        with open(env_path, 'w') as f:
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
        print(f"Created {env_path} file. Please edit it to add your actual OpenAI API key.")
    else:
        print(f"{env_path} file already exists.")
    
    topic = "Data Visualization with Python"
    generate_full_course(topic)