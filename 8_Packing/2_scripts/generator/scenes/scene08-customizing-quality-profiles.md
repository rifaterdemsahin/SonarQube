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


# Scene 08 – Customizing Quality Profiles
Video ID: SQ_008

## Learning Objectives
2. Configure custom quality profiles and rules

---

<!-- _class: slide-content -->
# 1. 🎥 Intro Talking Head
Every team has different coding standards and requirements. In this scene, we'll learn how to customize SonarQube's quality profiles to match your team's specific needs and coding standards.

<!-- _class: lower-third -->
Scene 08 - Introduction

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🎥</div>
<div class="picture-idea">
Talking Head Introduction
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Video ID: SQ_008
</div>

<!-- _class: script -->
Every team has different coding standards and requirements. In this scene, we'll learn how to customize SonarQube's quality profiles to match your team's specific needs and coding standards.

<!-- _class: screencapture -->
N/A

<div class="page-number">1/4</div>

---

<!-- _class: slide-content -->
# 2. 📊 Slides
- Quality Profile Basics

- Built-in profiles

- Language-specific rules

- Rule severity levels

- Rule parameters

- Customization Options

- Creating custom profiles

- Rule activation/deactivation

- Severity adjustments

- Parameter configuration

<!-- _class: lower-third -->
Scene 08 - Key Points

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">📊</div>
<div class="picture-idea">
Presentation Slides
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">📝</span>
Learning Objectives
</div>

<!-- _class: script -->
- Quality Profile Basics

- Built-in profiles

- Language-specific rules

- Rule severity levels

- Rule parameters

- Customization Options

- Creating custom profiles

- Rule activation/deactivation

- Severity adjustments

- Parameter configuration

<!-- _class: screencapture -->
N/A

<div class="page-number">2/4</div>

---

<!-- _class: slide-content -->
# 3. 🖥️ Screen Capture
1. Access quality profiles

2. Create new profile

3. Configure rule sets

4. Adjust rule parameters

5. Set severity levels

6. Apply profile to project

<!-- _class: lower-third -->
Scene 08 - Demonstration

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🖥️</div>
<div class="picture-idea">
Screen Capture Demo
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Interactive Demo
</div>

<!-- _class: script -->
1. Access quality profiles

2. Create new profile

3. Configure rule sets

4. Adjust rule parameters

5. Set severity levels

6. Apply profile to project

<!-- _class: screencapture -->
1. Access quality profiles

2. Create new profile

3. Configure rule sets

4. Adjust rule parameters

5. Set severity levels

6. Apply profile to project

<div class="page-number">3/4</div>

---

<!-- _class: slide-content -->
# 4. 🎬 Summary Talking Head
You now know how to customize quality profiles to match your team's needs. In the next scene, we'll learn how to set up and configure quality gates to enforce your quality standards.

<!-- _class: lower-third -->
Scene 08 - Summary

<!-- _class: right-top -->
<div class="right-top">
<div class="picture-placeholder">🎬</div>
<div class="picture-idea">
Talking Head Summary
</div>
</div>

<!-- _class: right-bottom -->
<div class="right-bottom">
<span class="talking-head">👨‍💻</span>
Key Takeaways
</div>

<!-- _class: script -->
You now know how to customize quality profiles to match your team's needs. In the next scene, we'll learn how to set up and configure quality gates to enforce your quality standards.

<!-- _class: screencapture -->
N/A

<div class="page-number">4/4</div>
