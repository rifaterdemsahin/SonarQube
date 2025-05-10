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