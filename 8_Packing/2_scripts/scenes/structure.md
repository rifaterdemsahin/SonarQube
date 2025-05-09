# Scene Generation System

## Course Structure
- The course consists of 3 main objectives
- Each objective contains 3 lessons
- Each lesson includes 3 video scenes

## Overview
This document outlines the structure and strategy for generating 15 video scenes, each containing 4 key sections:
1. Intro Talking Head
2. Slides
3. Screen Capture (Map Interaction)
4. Summary Talking Head

## File Structure
```
project/
├── metadata/
│   ├── scene01.yaml
│   ├── scene02.yaml
│   └── ... (scene03.yaml to scene15.yaml)
├── scenes/
│   ├── scene01-overview.md
│   ├── scene02-history.md
│   └── ... (scene03.md to scene15.md)
├── generate-scene-md.py
└── generate-from-yaml.sh
```

## Marp Configuration
Each scene's markdown file will use the following Marp configuration:

```yaml
---
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
```

## Marp Slide Structure
Each scene will be structured as a Marp presentation with the following layout:

1. **Slide Content (Left Top)**
   - Main bullet points
   - Key information
   - Animated list items

2. **Lower Third (Left Bottom)**
   - Scene title
   - Section identifier
   - Navigation elements

3. **Right Top**
   - Image placeholder
   - Visual content area
   - Supporting graphics

4. **Right Bottom**
   - Talking head indicator
   - Key metrics
   - Status indicators

5. **Script Section (Bottom)**
   - Narration text
   - Speaker notes
   - Timing cues

6. **Screen Capture Section (Bottom)**
   - Map interaction instructions
   - UI element highlights
   - Navigation steps

### Example Slide Structure
```markdown
<!-- _class: slide-content -->
- 🎯 Main Point 1
- 📊 Main Point 2
- 🔍 Main Point 3

<!-- _class: Lower Third -->
# Scene Title

<!-- _class: Right Top -->
<div class="right-top">
<div class="picture-placeholder">🖼️</div>
<div class="picture-idea">
[Visual content description]
</div>
</div>

<!-- _class: Right Bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Key Metric 1
Key Metric 2
</div>

<!-- _class: Script -->
<div class="script">
[Speaker script goes here]
</div>

<div class="screencapture">
[Screen capture instructions]
</div>

<div class="page-number">1</div>
```

## Scene Topics
1. Overview of Region
2. Historical Background
3. Geography & Terrain
4. Demographics
5. Urban Areas
6. Natural Resources
7. Climate Zones
8. Transportation Routes
9. Cultural Sites
10. Environmental Challenges
11. Economic Activity
12. Political Divisions
13. Education & Institutions
14. Health & Infrastructure
15. Future Plans & Vision

## YAML Metadata Structure
Each scene's metadata file (sceneXX.yaml) follows this structure:

```yaml
scene: 1
title: "Overview of the Region"
intro_talking_head: >
  [45-second script introducing the topic]
slides: >
  - [Bullet point 1]
  - [Bullet point 2]
  - [Bullet point 3]
  - [Bullet point 4]
screen_capture: >
  [Detailed map interaction instructions]
summary_talking_head: >
  [30-second closing script]
```

## Prompt Strategy

### 1. Intro Talking Head
- Duration: 45 seconds
- Purpose: Set context and engage viewers
- Key Elements:
  - Hook the audience
  - Introduce the topic
  - Preview what they'll learn
  - Explain why it matters

### 2. Slides
- Quantity: 3-4 key points
- Format: Bullet points
- Content Focus:
  - Visual support for intro
  - Key statistics
  - Main concepts
  - Supporting data

### 3. Screen Capture (Map Interaction)
- Duration: 1-2 minutes
- Elements:
  - Starting point/zoom level
  - Required overlays
  - Interactive elements
  - Key locations to highlight
  - Transitions/animations

### 4. Summary Talking Head
- Duration: 30 seconds
- Components:
  - Key takeaway
  - Connection to next scene
  - Engaging question
  - Call to action

## Generation Process

1. Create metadata files for each scene
2. Run the Python script to generate markdown files
3. Review and refine content
4. Export final scenes

## Python Script Usage
```bash
python3 generate-scene-md.py metadata/sceneXX.yaml
```

## Bash Script Usage
```bash
./generate-from-yaml.sh
```

## Best Practices

### Content Guidelines
- Keep scripts concise and engaging
- Use clear, active voice
- Include specific map coordinates
- Maintain consistent tone throughout
- Link scenes thematically

### Technical Guidelines
- Use relative paths in metadata
- Validate YAML syntax
- Include error handling
- Maintain consistent formatting
- Version control all files

### Production Tips
- Test map interactions before recording
- Prepare backup content
- Time each section
- Create storyboard for complex interactions
- Document any special requirements

## Next Steps
1. Generate metadata files for all 15 scenes
2. Run the generation scripts
3. Review and refine content
4. Prepare for production