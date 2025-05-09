#!/usr/bin/env python3

import os
from pathlib import Path
import re
from math import ceil

def calculate_reading_time(word_count: int) -> str:
    """Calculate reading time in minutes and seconds.
    
    Args:
        word_count (int): Number of words
        
    Returns:
        str: Formatted reading time
    """
    # Assuming average reading speed of 250 words per minute
    minutes = word_count / 250
    full_minutes = int(minutes)
    seconds = ceil((minutes - full_minutes) * 60)
    
    if full_minutes == 0:
        return f"{seconds} seconds"
    elif seconds == 0:
        return f"{full_minutes} minutes"
    else:
        return f"{full_minutes} minutes {seconds} seconds"

def count_words(text: str) -> int:
    """Count the number of words in a text.
    
    Args:
        text (str): Text to count words from
        
    Returns:
        int: Number of words
    """
    return len(text.split())

def extract_scripts_from_file(file_path: str) -> tuple[str, int]:
    """Extract script sections from a scene file.
    
    Args:
        file_path (str): Path to the scene markdown file
        
    Returns:
        tuple[str, int]: Extracted script content and word count
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'# Scene \d+ – (.*?)\n', content)
    title = title_match.group(1) if title_match else "Unknown Title"
    
    # Extract video ID
    video_id_match = re.search(r'Video ID: (SQ_\d+)', content)
    video_id = video_id_match.group(1) if video_id_match else "Unknown Video ID"
    
    # Extract learning objectives
    learning_obj_match = re.search(r'## Learning Objectives\n(.*?)(?=\n\n|$)', content, re.DOTALL)
    learning_obj = learning_obj_match.group(1).strip() if learning_obj_match else "No learning objectives found"
    
    # Extract all script sections
    script_sections = re.findall(r'### Script for Course Creator\n(.*?)\n\n### Script for Instructor Read\n(.*?)(?=\n\n|$)', content, re.DOTALL)
    
    # Calculate total words for this scene
    total_words = sum(count_words(creator) + count_words(instructor) for creator, instructor in script_sections)
    reading_time = calculate_reading_time(total_words)
    
    # Format the extracted content
    formatted_content = f"## {title}\n"
    formatted_content += f"Video ID: {video_id}\n\n"
    formatted_content += "### Learning Objectives\n"
    formatted_content += learning_obj + "\n\n"
    formatted_content += f"Estimated Reading Time: {reading_time}\n\n"
    
    # Group scripts by learning objective
    formatted_content += "### Scripts by Learning Objective\n\n"
    objectives = learning_obj.split('\n')
    script_count = len(script_sections)
    scripts_per_objective = max(1, script_count // len(objectives))
    
    for i, objective in enumerate(objectives):
        formatted_content += f"#### {objective.strip()}\n\n"
        start_idx = i * scripts_per_objective
        end_idx = start_idx + scripts_per_objective
        
        for creator, instructor in script_sections[start_idx:end_idx]:
            formatted_content += "##### Course Creator Script\n"
            formatted_content += creator.strip() + "\n\n"
            formatted_content += "##### Instructor Script\n"
            formatted_content += instructor.strip() + "\n\n"
    
    formatted_content += f"Total Word Count: {total_words}\n\n"
    return formatted_content, total_words

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
    
    total_word_count = 0
    # Process each scene file
    for scene_file in scene_files:
        scene_content, word_count = extract_scripts_from_file(scene_file)
        content += scene_content
        content += "---\n\n"
        total_word_count += word_count
    
    # Add total reading time and word count
    total_reading_time = calculate_reading_time(total_word_count)
    content += f"Total Word Count: {total_word_count}\n"
    content += f"Total Estimated Reading Time: {total_reading_time}\n"
    
    # Write the consolidated content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully created: {output_file}")
    print(f"Total word count: {total_word_count}")
    print(f"Total estimated reading time: {total_reading_time}")

if __name__ == "__main__":
    main() 