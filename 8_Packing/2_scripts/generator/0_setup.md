# 🎬 ShotList System Setup
- 🎯 Goal Create a production guide using outline and script and having a shot list output

## 📁 Core Files
\SonarQube\8_Packing\2_scripts\generator\0_setup.md
\SonarQube\8_Packing\2_scripts\generator\1_outline.yaml
\SonarQube\8_Packing\2_scripts\generator\2_script.yaml
\SonarQube\8_Packing\2_scripts\generator\3_shotlist.md


## 📚 Course Structure
- 3 main objectives
- 3 lessons per objective
- 3 video scenes per lesson
- Total: 15 video scenes

## 🎥 Shot Structure
Each scene (4 minutes total) consists of:
1. 🎤 Intro Talking Head (45 seconds)
2. 📊 Slides (90 seconds)
3. 💻 Screen Capture (120 seconds)
4. 🎤 Summary Talking Head (45 seconds)


## ⚙️ Shot List Marp Configuration
- Each shot markdown file will use the following Marp configuration:
- Each shot should have ots own style of marp 
- the video and learning objectives should be on the right bottom
- mention the type of the shot top center
- Different emoji type for 
- different styles for each shot type. I've created distinct visual treatments for each type while maintaining consistency in the overall structure
- Add a unique shot it on the right bottom 


1. 🎤 Intro Talking Head 
2. 📊 Slides
3. 💻 Screen Capture
4. 🎤 Summary Talking Head 

## ⏱️ Estimation time 
- use 120 words per minute
- two words a second
- Estimate using the comfortable time 
 


## 🎯 Shot Strategy
- Make each marp different than each other 
### 1. 🎤 Intro Talking Head
- Duration: 45 seconds
- Purpose: Set context and engage viewers
- Key Elements:
  - Hook the audience
  - Introduce the topic
  - Preview what they'll learn
  - Explain why it matters
- MENTION THIS IS AS HOOK ON MARP SLIDES

### 2. 📊 Slides
- Quantity: 3-4 key points
- Format: Bullet points
- Content Focus:
  - Visual support for intro
  - Key statistics
  - Main concepts
  - Supporting data
- MENTION THIS IS OBJECTIVES IN THE MARP SLIDE

### 3. 💻 Screen Capture (Map Interaction)
- Duration: 1-2 minutes
- Elements:
  - Starting point/zoom level
  - Required overlays
  - Interactive elements
  - Key locations to highlight
  - Transitions/animations
  - MENTION THIS IS THE FLEX IN THE MARP SLIDES

### 4. 🎤 Summary Talking Head
- Duration: 30 seconds
- Components:
  - Key takeaway
  - Connection to next scene
  - Engaging question
  - Call to action
- MENTION THIS IS THE CLOSING IN THE MARP SLIDE



## ✨ Best Practices

### 📝 Content Guidelines
- Keep scripts concise and engaging
- Use clear, active voice
- Include specific map coordinates
- Maintain consistent tone throughout
- Link scenes thematically

### 🔧 Technical Guidelines
- Use relative paths in metadata
- Validate YAML syntax
- Include error handling
- Maintain consistent formatting
- Version control all files

### 🎨 Production Tips
- Test map interactions before recording
- Prepare backup content
- Time each section
- Create storyboard for complex interactions
- Document any special requirements

## 👣 Next Steps
1. Generate metadata files for all 15 scenes
2. Run the generation scripts
3. Review and refine content
4. Prepare for production

## 🎵 Guidance for Editors
- **Music**: Upbeat, motivational track suggestions
- Sound Effect suggestions
- Visual effect suggestions

## 📌 Markers on The Slides
- **Length**: 45-60 seconds total
- **Style**: Mix of live-action, text animations, and dynamic transitions

## 📋 Formatting
- Use markdown
- Use Marp



## Example Talking Head Marp 

<div class="shot-type" data-type="talkinghead">🎬 COURSE INTRODUCTION</div>

# Mastering SonarQube: From Technical Debt to Development Excellence


<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Welcome to our SonarQube course!</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">🎥</div>
    <div class="picture-idea">Course Overview</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Video 1: Course Introduction</div>
    <div class="learning-objective">LO1: Set up and configure GitHub Codespaces for development</div>
  </div>
</div>

<div class="script">
Welcome to our SonarQube course! In today's software world, technical debt is the silent killer of speed, quality, and innovation. Managing it isn't optional—it's essential. SonarQube helps you catch debt early, fix it fast, and keep your projects healthy for the long run.
</div>
---


## Example Slides

<div class="shot-type" data-type="slides">🎬 COURSE OBJECTIVES</div>

# Mastering SonarQube: From Technical Debt to Development Excellence


<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>OKR Objective and Key Results</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">🎥</div>
    <div class="picture-idea">Course Overview</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Video 2: Course Objectives</div>
    <div class="learning-objective">LO2: Integration</div>
  </div>
</div>

<div class="slide-content">
- Setup in Codespaces
- Integrate with Github
- Scan the repository
</div>

<div class="script">
Here is the 3 objectives > setup,integrate and scan</div>
---


## Example ScreenCapture

<div class="shot-type" data-type="screencapture">🎬 INTEGRATE WITH GITHUB APP</div>

# Mastering the integrations


<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Set Client ID</span>
</div>

  
  <div class="right-bottom">
    <div class="video-info">Video 4: Course Objectives</div>
    <div class="learning-objective">LO2: Integrate</div>
  </div>
</div>

<div class="capture-ideas-and Steps">
- Goto in Codespaces
- Go to Sonarqube
- get the ClientID
</div>

<div class="script">
Here is how we are going to be able to add an app and this would be able get the client id and client secret</div>
---