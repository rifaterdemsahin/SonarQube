#!/usr/bin/env python3

import os
from pathlib import Path
import re

def extract_scripts_from_file(file_path: str) -> str:
    """Extract script sections from a scene file.
    
    Args:
        file_path (str): Path to the scene markdown file
        
    Returns:
        str: Extracted script content
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'# Scene \d+ – (.*?)\n', content)
    title = title_match.group(1) if title_match else "Unknown Title"
    
    # Extract all script sections
    script_sections = re.findall(r'### Script for Course Creator\n(.*?)\n\n### Script for Instructor Read\n(.*?)(?=\n\n|$)', content, re.DOTALL)
    
    # Format the extracted content
    formatted_content = f"## {title}\n\n"
    for course_creator, instructor in script_sections:
        formatted_content += "### Course Creator Script\n"
        formatted_content += course_creator.strip() + "\n\n"
        formatted_content += "### Instructor Script\n"
        formatted_content += instructor.strip() + "\n\n"
    
    return formatted_content

def main():
    """Main function to process all scene files and create consolidated script."""
    scenes_dir = Path('scenes')
    output_file = Path('all-scripts.md')
    
    # Get all scene files sorted by scene number
    scene_files = sorted(
        [f for f in scenes_dir.glob('scene*.md')],
        key=lambda x: int(re.search(r'scene(\d+)', x.name).group(1))
    )
    
    # Create header
    content = """# All Course Scripts

This document contains all the scripts for both course creators and instructors from all scenes.

"""
    
    # Process each scene file
    for scene_file in scene_files:
        content += extract_scripts_from_file(scene_file)
        content += "---\n\n"
    
    # Write the consolidated content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully created: {output_file}")

if __name__ == "__main__":
    main() 