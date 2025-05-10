---
marp: true
theme: default
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-family: 'Arial', sans-serif;
  }
  h1 {
    font-size: 2.5em;
    text-align: center;
    margin-top: 1.5em;
  }
  .header {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.5em;
    font-weight: bold;
  }
  .footer {
    position: absolute;
    right: 40px;
    bottom: 20px;
    font-size: 0.8em;
    opacity: 0.8;
    text-align: right;
  }
  .script {
    position: absolute;
    left: 40px;
    bottom: 20px;
    font-size: 0.8em;
    opacity: 0.8;
    text-align: left;
    width: 60%;
    font-style: italic;
  }
---

<!-- _class: header -->
🎤 INTRO TALKING HEAD  

# Welcome to *SonarQube Mastery*  
### Your journey to code quality excellence  
#### Shot Type: Talking Head - Hook

![bg right:40% 80%](https://placehold.co/400x300/FFFFFF/667eea/png?text=Instructor)  

<!-- _class: footer -->
🎬 **SHOT ID:** INTRO-01  
📌 **LOs:** Hook audience, introduce topic  
🎥 **Video:** intro_01.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - INTRO-01]  
"Welcome to SonarQube Mastery! In today's software world, technical debt is the silent killer of speed, quality, and innovation. Managing it isn't optional—it's essential. SonarQube helps you catch debt early, fix it fast, and keep your projects healthy for the long run."

---

<!-- _class: header -->
📊 CORE CONCEPT  
#### Shot Type: Slides

# Understanding Technical Debt  

- Accumulated cost of shortcuts and quick fixes  
- Impacts code quality and maintainability  
- SonarQube helps identify and manage debt  

![bg right:40% 90%](https://placehold.co/400x300/EEE/3498db/png?text=Technical+Debt+Graph)  

<!-- _class: footer -->
🎬 **SHOT ID:** SLIDE-01  
📌 **LOs:** Explain technical debt concept  
🎥 **Video:** intro_01.mp4  

---

<!-- _class: header -->
💻 CODE DEMO  
#### Shot Type: Screen Capture

```bash
# Install SonarQube
docker run -d --name sonarqube \
  -p 9000:9000 \
  -e SONAR_JDBC_URL=jdbc:postgresql://localhost/sonar \
  -e SONAR_JDBC_USERNAME=sonar \
  -e SONAR_JDBC_PASSWORD=sonar \
  sonarqube:latest
```

<!-- _class: footer -->
🎬 **SHOT ID:** SCREEN-01  
📌 **LOs:** Demonstrate SonarQube setup  
🎥 **Video:** intro_01.mp4  

---

<!-- _class: header -->
🎤 CLOSING TALKING HEAD  

# Ready to Begin!  
### Let's transform your code quality  
#### Shot Type: Talking Head - Closing 

![bg right:40% 80%](https://placehold.co/400x300/FFFFFF/11998e/png?text=Instructor)  

<!-- _class: footer -->
🎬 **SHOT ID:** OUTRO-01  
📌 **LOs:** Summarize key points, motivate  
🎥 **Video:** intro_01.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - OUTRO-01]  
"By the end of this course, you'll have the skills to identify, manage, and reduce technical debt using SonarQube. Let's start this journey together and transform your code quality!"


<!-- _class: header -->
🎤 INTRO TALKING HEAD  

# GitHub Codespaces Setup  
### Your cloud development environment  
#### Shot Type: Talking Head - Hook

![bg right:40% 80%](https://placehold.co/400x300/FFFFFF/667eea/png?text=Instructor)  

<!-- _class: footer -->
🎬 **SHOT ID:** INTRO-02  
📌 **LOs:** Introduce GitHub Codespaces  
🎥 **Video:** intro_02.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - INTRO-02]  
"Today we're going to transform infrastructure debt into a powerful development setup using GitHub Codespaces. This cloud-based development environment will help us manage technical debt more effectively."

---

<!-- _class: header -->
📊 CORE CONCEPT  
#### Shot Type: Slides

# GitHub Codespaces Benefits  

- Cloud-based development environment  
- Consistent setup across team  
- Integrated with GitHub workflow  
- Pre-configured for SonarQube  

![bg right:40% 90%](https://placehold.co/400x300/EEE/3498db/png?text=Codespaces+Diagram)  

<!-- _class: footer -->
🎬 **SHOT ID:** SLIDE-02  
📌 **LOs:** Explain Codespaces benefits  
🎥 **Video:** intro_02.mp4  

---

<!-- _class: header -->
💻 CODE DEMO  
#### Shot Type: Screen Capture

```yaml
# .devcontainer/devcontainer.json
{
  "name": "SonarQube Development",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "SonarSource.sonarlint-vscode"
      ]
    }
  }
}
```

<!-- _class: footer -->
🎬 **SHOT ID:** SCREEN-02  
📌 **LOs:** Configure development environment  
🎥 **Video:** intro_02.mp4  

---

<!-- _class: header -->
🎤 CLOSING TALKING HEAD  

# Environment Ready!  
### Let's start coding with quality  
#### Shot Type: Talking Head - Closing 

![bg right:40% 80%](https://placehold.co/400x300/FFFFFF/11998e/png?text=Instructor)  

<!-- _class: footer -->
🎬 **SHOT ID:** OUTRO-02  
📌 **LOs:** Summarize setup, preview next steps  
🎥 **Video:** intro_02.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - OUTRO-02]  
"Great! Our development environment is ready. Next, we'll focus on securing our setup and configuring SonarQube for optimal performance." 