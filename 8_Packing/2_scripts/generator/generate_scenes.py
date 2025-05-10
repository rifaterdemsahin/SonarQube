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

def load_scene_topics() -> Dict[int, Dict[str, Any]]:
    """Load and parse scene topics from YAML file.
    
    Returns:
        Dict[int, Dict[str, Any]]: Dictionary mapping scene IDs to their metadata
    """
    topics_file = Path(__file__).parent / 'scene-topics.yaml'
    with open(topics_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    scenes = {}
    for lesson in data['lessons']:
        for video in lesson.get('videos', []):
            if 'sceneid' in video:
                scenes[video['sceneid']] = {
                    'title': video['title'],
                    'video_id': video['id'],
                    'lesson_id': lesson['id'],
                    'lesson_title': lesson['title']
                }
    return scenes

def validate_metadata(data: Dict[str, Any], available_scenes: Dict[int, Dict[str, Any]]) -> None:
    """Validate required fields in metadata.
    
    Args:
        data (Dict[str, Any]): Metadata dictionary to validate
        available_scenes (Dict[int, Dict[str, Any]]): Available scene IDs and their metadata
        
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
    
    # Validate scene number exists in scene-topics.yaml
    if data['scene'] not in available_scenes:
        raise ValueError(f"Scene {data['scene']} not found in scene-topics.yaml")
    
    # Validate video ID matches scene-topics.yaml
    scene_info = available_scenes[data['scene']]
    if data['video_id'] != scene_info['video_id']:
        raise ValueError(f"Video ID mismatch. Expected {scene_info['video_id']}, got {data['video_id']}")
    
    # Validate title matches scene-topics.yaml
    if data['title'] != scene_info['title']:
        raise ValueError(f"Title mismatch. Expected {scene_info['title']}, got {data['title']}")

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
    
    # Create Marp configuration
    marp_config = """---
marp: true
theme: default
paginate: true
style: |
  section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr auto auto;
    gap: 1em;
    padding: 1em;
    position: relative;
  }
  .slide-content {
    grid-column: 1;
    grid-row: 1;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .slide-content li {
    margin-bottom: 0.5em;
    animation: slideUp 0.5s ease-out;
  }
  .lower-third {
    grid-column: 1;
    grid-row: 2;
    display: flex;
    gap: 0.5em;
    align-items: center;
  }
  .right-top {
    grid-column: 2;
    grid-row: 1;
    background: #f5f5f5;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1em;
    border: 2px dashed #ccc;
  }
  .picture-placeholder {
    font-size: 2em;
    color: #999;
    margin-bottom: 0.5em;
  }
  .picture-idea {
    font-size: 0.8em;
    color: #666;
    margin-top: 0.5em;
    text-align: center;
    font-style: italic;
  }
  .right-bottom {
    grid-column: 2;
    grid-row: 2;
    background: #f0f0f0;
    padding: 0.5em;
    display: flex;
    align-items: center;
    gap: 0.5em;
  }
  .talking-head {
    font-size: 1.5em;
    background: #fff;
    border: 2px solid #1a73e8;
    border-radius: 8px;
    padding: 0.3em;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2em;
    min-height: 2em;
  }
  .script {
    grid-column: 1 / -1;
    grid-row: 3;
    font-size: 0.8em;
    color: #666;
    border-top: 1px solid #ccc;
    padding-top: 0.5em;
  }
  .script::before {
    content: "> SCRIPT: ";
    color: #e74c3c;
    font-weight: bold;
  }
  .screencapture {
    grid-column: 1 / -1;
    grid-row: 4;
    font-size: 0.8em;
    color: #666;
    border-top: 1px solid #ccc;
    padding-top: 0.5em;
    font-style: italic;
  }
  .page-number {
    position: absolute;
    bottom: 1em;
    right: 1em;
    font-size: 0.8em;
    color: #666;
  }
  h1 {
    font-size: 2em;
    color: #1a73e8;
  }
  h2 {
    font-size: 1.8em;
    color: #34a853;
  }
  h3 {
    font-size: 1.6em;
    color: #ea4335;
  }
  .emoji {
    font-size: 1.2em;
  }
  .fade {
    animation: fadeIn 1s ease-in;
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  .slide-up {
    animation: slideUp 0.5s ease-out;
  }
  @keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  .lower-third-item {
    animation: fadeIn 0.5s ease-in;
  }
---
"""
    
    # Generate markdown content with Marp structure
    content = f"""{marp_config}

# Scene {num_str} – {title}
Video ID: {video_id}

## Learning Objectives
{learning_objectives}

---

<!-- _class: slide-content -->
# 1. 🎥 Intro Talking Head
{intro}

<!-- _class: lower-third -->
Scene {num_str} - Introduction

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🎥</div>
<div class="picture-idea">
Talking Head Introduction
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Video ID: {video_id}
</div>

<!-- _class: script -->
{intro}

<!-- _class: screencapture -->
N/A

<div class="page-number">1/4</div>

---

<!-- _class: slide-content -->
# 2. 📊 Slides
{slides}

<!-- _class: lower-third -->
Scene {num_str} - Key Points

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">📊</div>
<div class="picture-idea">
Presentation Slides
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">📝</span>
Learning Objectives
</div>

<!-- _class: script -->
{slides}

<!-- _class: screencapture -->
N/A

<div class="page-number">2/4</div>

---

<!-- _class: slide-content -->
# 3. 🖥️ Screen Capture
{screen_capture}

<!-- _class: lower-third -->
Scene {num_str} - Demonstration

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🖥️</div>
<div class="picture-idea">
Screen Capture Demo
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Interactive Demo
</div>

<!-- _class: script -->
{screen_capture}

<!-- _class: screencapture -->
{screen_capture}

<div class="page-number">3/4</div>

---

<!-- _class: slide-content -->
# 4. 🎬 Summary Talking Head
{summary}

<!-- _class: lower-third -->
Scene {num_str} - Summary

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🎬</div>
<div class="picture-idea">
Talking Head Summary
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Key Takeaways
</div>

<!-- _class: script -->
{summary}

<!-- _class: screencapture -->
N/A

<div class="page-number">4/4</div>
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
        # Load available scenes from scene-topics.yaml
        available_scenes = load_scene_topics()
        
        # Process YAML file
        data = process_yaml_file(file_path)
        
        # Validate against scene-topics.yaml
        validate_metadata(data, available_scenes)
        
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