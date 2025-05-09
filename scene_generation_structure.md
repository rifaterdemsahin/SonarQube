# Scene Generation System

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