#!/usr/bin/env python3

import sys
import yaml
import os
from pathlib import Path

def slugify(text):
    """Convert text to URL-friendly slug."""
    return text.lower().replace(' ', '-').replace(':', '').replace(',', '')

def validate_metadata(data):
    """Validate required fields in metadata."""
    required_fields = ['scene', 'title', 'video_id', 'intro_talking_head', 
                      'slides', 'screen_capture', 'summary_talking_head']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(data['scene'], int):
        raise ValueError("Scene number must be an integer")
    
    if not isinstance(data['video_id'], str):
        raise ValueError("Video ID must be a string")

def get_learning_objectives(scene_num):
    """Get learning objectives based on scene number."""
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

def generate_markdown(data):
    """Generate markdown content from metadata."""
    scene_num = data['scene']
    title = data['title']
    video_id = data['video_id']
    
    # Format scene number with leading zero
    num_str = f"{scene_num:02}"
    
    # Get learning objectives
    learning_objectives = get_learning_objectives(scene_num)
    
    # Generate markdown content
    content = f"""# Scene {num_str} – {title}
Video ID: {video_id}

## Learning Objectives
{learning_objectives}

---

## 1. 🎥 Intro Talking Head
Mention the scene number and tell the audience about:

{data['intro_talking_head'].strip()}

---

## 2. 📊 Slides
Mention the scene number and show:

{data['slides'].strip()}

---

## 3. 🖥️ Screen Capture (Map Interaction)
Mention the scene number and do:

{data['screen_capture'].strip()}

---

## 4. 🎬 Summary Talking Head
Mention the scene number and summarize:

{data['summary_talking_head'].strip()}

---

## Script for Course Creator
Scene {num_str}: {title}
Video ID: {video_id}

1. Intro Talking Head: Mention scene {num_str} and tell the audience about the key points
2. Slides: Mention scene {num_str} and show the visual content
3. Screen Capture: Mention scene {num_str} and demonstrate the interactive elements
4. Summary Talking Head: Mention scene {num_str} and summarize the main takeaways
"""
    return content

def main(file_path):
    """Main function to process YAML and generate markdown."""
    try:
        # Read and parse YAML file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Validate metadata
        validate_metadata(data)
        
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
        
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate-scene-md.py metadata/sceneXX.yaml")
        sys.exit(1)
    main(sys.argv[1])