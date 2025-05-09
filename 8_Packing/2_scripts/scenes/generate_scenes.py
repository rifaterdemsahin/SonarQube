import os

def create_scene_file(scene_number):
    content = f"""# Scene {scene_number:02d}

---

## 1. Intro Talking Head

### Prompt
Write a 45-second script where the presenter introduces the scene. Explain what the audience will learn and why it's relevant.

### Script
_(Paste or generate the script here)_

---

## 2. Slides

### Prompt
List 3–4 bullet points for the slides that summarize the key information for this scene. Use short phrases and avoid full sentences.

### Script
_(Paste or generate slide points here)_

---

## 3. Screen Capture (Map Interaction)

### Prompt
Write detailed instructions for what should be shown on the map in this scene:
- Where to zoom
- What overlays to show
- Any interactions like pinning, highlighting, labels

### Script
_(Paste or generate map capture instructions here)_

---

## 4. Summary Talking Head

### Prompt
Write a 30-second summary script for the presenter to wrap up the scene. Include 1 key takeaway and ask the audience a reflective question.

### Script
_(Paste or generate the script here)_
"""
    
    filename = f"scene{scene_number:02d}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")

def main():
    # Create 15 scene files
    for i in range(1, 16):
        create_scene_file(i)

if __name__ == "__main__":
    main() 