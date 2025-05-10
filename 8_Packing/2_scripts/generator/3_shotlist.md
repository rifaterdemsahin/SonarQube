---
marp: true
theme: default
paginate: true
style: |
  section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto 1fr auto auto;
    gap: 1.5em;
    padding: 2em;
    position: relative;
    background: linear-gradient(to bottom right, #ffffff, #f8f9fa);
  }
  
  .shot-type {
    grid-column: 1 / -1;
    text-align: center;
    font-size: 1.2em;
    color: #1a73e8;
    font-weight: bold;
    padding: 0.5em;
    background: rgba(26, 115, 232, 0.1);
    border-radius: 8px;
    margin-bottom: 1em;
  }
  
  .slide-content {
    grid-column: 1;
    grid-row: 2;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .slide-content li {
    margin-bottom: 0.8em;
    padding-left: 1.5em;
    position: relative;
    animation: slideUp 0.5s ease-out;
  }
  
  .slide-content li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #1a73e8;
  }
  
  .lower-third {
    grid-column: 1;
    grid-row: 3;
    display: flex;
    gap: 1em;
    align-items: center;
    background: rgba(26, 115, 232, 0.05);
    padding: 1em;
    border-radius: 8px;
  }
  
  .right-panel {
    grid-column: 2;
    grid-row: 2 / 4;
    display: flex;
    flex-direction: column;
    gap: 1em;
  }
  
  .right-top {
    background: #ffffff;
    padding: 1.5em;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1em;
  }
  
  .right-bottom {
    background: #ffffff;
    padding: 1.5em;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .video-info {
    font-size: 1em;
    color: #1a73e8;
    font-weight: bold;
    margin-bottom: 0.5em;
  }
  
  .learning-objective {
    font-size: 0.9em;
    color: #5f6368;
    font-style: italic;
    padding: 0.5em;
    background: rgba(26, 115, 232, 0.05);
    border-radius: 6px;
  }
  
  .talking-head {
    font-size: 1.8em;
    background: #ffffff;
    border: 2px solid #1a73e8;
    border-radius: 50%;
    padding: 0.3em;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2.5em;
    min-height: 2.5em;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .script {
    grid-column: 1 / -1;
    grid-row: 4;
    font-size: 0.9em;
    color: #5f6368;
    border-top: 2px solid #e8eaed;
    padding-top: 1em;
    margin-top: 1em;
  }
  
  .script::before {
    content: "📝 SCRIPT:";
    color: #1a73e8;
    font-weight: bold;
    margin-right: 0.5em;
  }
  
  .screencapture {
    grid-column: 1 / -1;
    grid-row: 5;
    font-size: 0.9em;
    color: #5f6368;
    border-top: 2px solid #e8eaed;
    padding-top: 1em;
    font-style: italic;
  }
  
  .screencapture::before {
    content: "🎥 SCREEN CAPTURE:";
    color: #1a73e8;
    font-weight: bold;
    margin-right: 0.5em;
  }
  
  .page-number {
    position: absolute;
    bottom: 1em;
    right: 1em;
    font-size: 0.8em;
    color: #5f6368;
  }
  
  h1 {
    font-size: 2.2em;
    color: #1a73e8;
    margin-bottom: 0.5em;
    text-align: center;
  }
  
  h2 {
    font-size: 1.8em;
    color: #34a853;
  }
  
  h3 {
    font-size: 1.6em;
    color: #ea4335;
  }
  
  @keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
---

<div class="shot-type" data-type="talkinghead">🎬 COURSE INTRODUCTION</div>

# Mastering SonarQube: From Technical Debt to Development Excellence

<div class="slide-content">
- Learn how to set up your development environment using GitHub Codespaces
- Understand technical debt and its impact on development
- Master SonarQube integration and configuration
</div>

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

<div class="screencapture">
Setting up development environment with GitHub Codespaces
</div>

---

<div class="shot-type" data-type="slides">👨‍🏫 INSTRUCTOR INTRODUCTION</div>

# Meet Your Instructor

<div class="slide-content">
- Rifat Erdem Sahin
- 40+ successful IT contracts
- 80+ projects delivered globally
- Deep expertise in SDLC
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Hello, I'm Rifat Erdem Sahin</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">👨‍💻</div>
    <div class="picture-idea">Instructor Profile</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Video 2: Instructor Introduction</div>
    <div class="learning-objective">LO1: Configure secure access and environment settings</div>
  </div>
</div>

<div class="script">
Hello, I'm Rifat Erdem Sahin. With over 40 successful IT contracts and 80 projects delivered globally, I've honed deep expertise in the software development life cycle. At Accenture, this pivotal tool enabled me to ensure code quality and maintainability across large-scale projects.
</div>

<div class="screencapture">
Using Copilot with the setup
</div>

---

<div class="shot-type" data-type="screencapture">🔧 PRACTICAL CONTENT</div>

# Authentic Content

<div class="slide-content">
- Real-world challenges
- Hands-on journey
- Practical problem-solving
- Real project setup
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Real-world challenges and solutions</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">🔧</div>
    <div class="picture-idea">Practical Experience</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Video 3: Authentic Content</div>
    <div class="learning-objective">LO1: Implement secure GitHub integration</div>
  </div>
</div>

<div class="script">
In this course, we'll explore real-world challenges, focusing on navigating technical debt and achieving daily deployments. This isn't just theory—it's a hands-on journey into solving practical problems with tools like SonarQube. I have crafted the course around a real project which is setting up the sonarqube environment.
</div>

<div class="screencapture">
Setting up development environments
</div>

---

<div class="shot-type" data-type="slides">🤖 AI INTEGRATION</div>

# AI-First Implementation

<div class="slide-content">
- AI tools integration
- ChatGPT utilization
- Quality checks automation
- Portfolio development
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>AI-assisted development</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">🤖</div>
    <div class="picture-idea">AI Integration</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Video 4: AI-First Implementation</div>
    <div class="learning-objective">LO1: Set up automated code quality scanning</div>
  </div>
</div>

<div class="script">
This course includes a bonus AI-first project where you'll integrate AI tools to set up and optimize a SonarQube environment. It's designed to sharpen your skills in AI-assisted development while ensuring top-tier quality standards.
</div>

---

<div class="shot-type" data-type="screencapture">📊 PORTFOLIO DEVELOPMENT</div>

# Portfolio Development

<div class="capture-ideas-and-steps">
- Set up GitHub repository
- Configure SonarQube integration
- Run initial code analysis
- Document quality metrics
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Build your professional portfolio</span>
</div>

<div class="right-panel">
  <div class="right-bottom">
    <div class="video-info">Video 5: Portfolio Development</div>
    <div class="learning-objective">LO1: Optimize GitHub resources and costs</div>
  </div>
</div>

<div class="script">
Creating a professional portfolio is essential for IT professionals, showcasing your ability to deliver high-quality, maintainable software. By integrating SonarQube into your GitHub projects, you demonstrate a commitment to code quality and technical debt management.
</div>

---

<div class="shot-type" data-type="slides">📚 COURSE STRUCTURE</div>

# Course Structure

<div class="slide-content">
- 3 Main Objectives
- 3 Lessons per Objective
- 5 Videos per Lesson
- Total: 15 Video Scenes
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Comprehensive learning path</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">📚</div>
    <div class="picture-idea">Course Structure</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Course Overview</div>
    <div class="learning-objective">LO1-LO3: Complete course objectives</div>
  </div>
</div>

<div class="script">
Our course is structured to provide a comprehensive learning experience, with 3 main objectives, 3 lessons per objective, and 5 videos per lesson, totaling 15 video scenes. Each video is carefully crafted to build your expertise in SonarQube and technical debt management.
</div>

---

<div class="shot-type" data-type="talkinghead">🚀 COURSE CONCLUSION</div>

# Let's Get Started!

<div class="slide-content">
- Set up your environment
- Learn best practices
- Build your portfolio
- Transform your development process
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Ready to begin your journey</span>
</div>

<div class="right-panel">
  <div class="right-top">
    <div class="picture-placeholder">🎬</div>
    <div class="picture-idea">Course Start</div>
  </div>
  
  <div class="right-bottom">
    <div class="video-info">Final Video: Course Conclusion</div>
    <div class="learning-objective">Apply learned concepts to real-world scenarios</div>
  </div>
</div>

<div class="script">
By the end of this course, you'll have the skills and confidence to tackle technical debt, deliver high-quality software, and thrive in real-world development environments. Let's get started! 🚀
</div>

<div class="screencapture">
Final setup and preparation
</div>
