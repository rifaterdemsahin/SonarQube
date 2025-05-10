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
  .right-bottom {
    grid-column: 2;
    grid-row: 2;
    background: #f0f0f0;
    padding: 1em;
    display: flex;
    flex-direction: column;
    gap: 0.5em;
    border: 1px solid #ddd;
    border-radius: 8px;
  }
  .video-info {
    font-size: 0.9em;
    color: #333;
    font-weight: bold;
  }
  .learning-objective {
    font-size: 0.8em;
    color: #666;
    font-style: italic;
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

<div class="right-top">
  <div class="picture-placeholder">🎥</div>
  <div class="picture-idea">Course Overview</div>
</div>

<div class="right-bottom">
  <div class="video-info">Video 1: Course Introduction</div>
  <div class="learning-objective">LO1: Set up and configure GitHub Codespaces for development</div>
</div>

<div class="script">
Welcome to our SonarQube course! In today's software world, technical debt is the silent killer of speed, quality, and innovation. Managing it isn't optional—it's essential. SonarQube helps you catch debt early, fix it fast, and keep your projects healthy for the long run.
</div>

<div class="screencapture">
Setting up development environment with GitHub Codespaces
</div>

---

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

<div class="right-top">
  <div class="picture-placeholder">👨‍💻</div>
  <div class="picture-idea">Instructor Profile</div>
</div>

<div class="right-bottom">
  <div class="video-info">Video 2: Instructor Introduction</div>
  <div class="learning-objective">LO1: Configure secure access and environment settings</div>
</div>

<div class="script">
Hello, I'm Rifat Erdem Sahin. With over 40 successful IT contracts and 80 projects delivered globally, I've honed deep expertise in the software development life cycle. At Accenture, this pivotal tool enabled me to ensure code quality and maintainability across large-scale projects.
</div>

<div class="screencapture">
Using Copilot with the setup
</div>

---

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

<div class="right-top">
  <div class="picture-placeholder">🔧</div>
  <div class="picture-idea">Practical Experience</div>
</div>

<div class="right-bottom">
  <div class="video-info">Video 3: Authentic Content</div>
  <div class="learning-objective">LO1: Implement secure GitHub integration</div>
</div>

<div class="script">
In this course, we'll explore real-world challenges, focusing on navigating technical debt and achieving daily deployments. This isn't just theory—it's a hands-on journey into solving practical problems with tools like SonarQube. I have crafted the course around a real project which is setting up the sonarqube environment.
</div>

<div class="screencapture">
Setting up development environments
</div>

---

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

<div class="right-top">
  <div class="picture-placeholder">🤖</div>
  <div class="picture-idea">AI Integration</div>
</div>

<div class="right-bottom">
  <div class="video-info">Video 4: AI-First Implementation</div>
  <div class="learning-objective">LO1: Set up automated code quality scanning</div>
</div>

<div class="script">
This course includes a bonus AI-first project where you'll integrate AI tools to set up and optimize a SonarQube environment. It's designed to sharpen your skills in AI-assisted development while ensuring top-tier quality standards.
</div>

<div class="screencapture">
Using Copilot with the setup
</div>

---

# Portfolio Development

<div class="slide-content">
- GitHub integration
- Code quality showcase
- LinkedIn visibility
- Professional growth
</div>

<div class="lower-third">
  <span class="talking-head">👤</span>
  <span>Build your professional portfolio</span>
</div>

<div class="right-top">
  <div class="picture-placeholder">📊</div>
  <div class="picture-idea">Portfolio Building</div>
</div>

<div class="right-bottom">
  <div class="video-info">Video 5: Portfolio Development</div>
  <div class="learning-objective">LO1: Optimize GitHub resources and costs</div>
</div>

<div class="script">
Creating a professional portfolio is essential for IT professionals, showcasing your ability to deliver high-quality, maintainable software. By integrating SonarQube into your GitHub projects, you demonstrate a commitment to code quality and technical debt management.
</div>

<div class="screencapture">
Setting up development environments
</div>

---

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

<div class="right-top">
  <div class="picture-placeholder">📚</div>
  <div class="picture-idea">Course Structure</div>
</div>

<div class="right-bottom">
  <div class="video-info">Course Overview</div>
  <div class="learning-objective">LO1-LO3: Complete course objectives</div>
</div>

<div class="script">
Our course is structured to provide a comprehensive learning experience, with 3 main objectives, 3 lessons per objective, and 5 videos per lesson, totaling 15 video scenes. Each video is carefully crafted to build your expertise in SonarQube and technical debt management.
</div>

<div class="screencapture">
Course structure overview
</div>

---

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

<div class="right-top">
  <div class="picture-placeholder">🎬</div>
  <div class="picture-idea">Course Start</div>
</div>

<div class="right-bottom">
  <div class="video-info">Final Video: Course Conclusion</div>
  <div class="learning-objective">Apply learned concepts to real-world scenarios</div>
</div>

<div class="script">
By the end of this course, you'll have the skills and confidence to tackle technical debt, deliver high-quality software, and thrive in real-world development environments. Let's get started! 🚀
</div>

<div class="screencapture">
Final setup and preparation
</div>
