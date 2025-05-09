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

def generate_markdown(data):
    """Generate markdown content from metadata."""
    scene_num = data['scene']
    title = data['title']
    video_id = data['video_id']
    
    # Format scene number with leading zero
    num_str = f"{scene_num:02}"
    
    # Generate markdown content
    content = f"""# Scene {num_str} – {title}
Video ID: {video_id}

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