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


# Scene 09 – Technical Debt & Focus – Fix, Update, and Power On with Confidence
Video ID: video2

## Learning Objectives
2. Set up team collaboration features

---

<!-- _class: slide-content -->
# 1. 🎥 Intro Talking Head
In this scene, we'll explore strategies for managing technical debt while maintaining focus on development goals. We'll learn how to effectively fix issues, update systems, and move forward with confidence.

<!-- _class: lower-third -->
Scene 09 - Introduction

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
Video ID: video2
</div>

<!-- _class: script -->
In this scene, we'll explore strategies for managing technical debt while maintaining focus on development goals. We'll learn how to effectively fix issues, update systems, and move forward with confidence.

<!-- _class: screencapture -->
N/A

<div class="page-number">1/4</div>

---

<!-- _class: slide-content -->
# 2. 📊 Slides
- Technical Debt Management

- Debt identification

- Impact assessment

- Resolution planning

- Focus Strategies

- Priority setting

- Resource allocation

- Progress tracking

- Confidence Building

- Quality assurance

- Testing strategies

- Documentation

<!-- _class: lower-third -->
Scene 09 - Key Points

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
- Technical Debt Management

- Debt identification

- Impact assessment

- Resolution planning

- Focus Strategies

- Priority setting

- Resource allocation

- Progress tracking

- Confidence Building

- Quality assurance

- Testing strategies

- Documentation

<!-- _class: screencapture -->
N/A

<div class="page-number">2/4</div>

---

<!-- _class: slide-content -->
# 3. 🖥️ Screen Capture
1. Analyze technical debt

2. Prioritize fixes

3. Implement updates

4. Verify changes

5. Document progress

<!-- _class: lower-third -->
Scene 09 - Demonstration

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
1. Analyze technical debt

2. Prioritize fixes

3. Implement updates

4. Verify changes

5. Document progress

<!-- _class: screencapture -->
1. Analyze technical debt

2. Prioritize fixes

3. Implement updates

4. Verify changes

5. Document progress

<div class="page-number">3/4</div>

---

<!-- _class: slide-content -->
# 4. 🎬 Summary Talking Head
We've covered effective strategies for managing technical debt while maintaining focus. You now know how to fix issues, update systems, and move forward with confidence. In the next scene, we'll explore yak shaving and debugging, learning how to leverage AI and intuition for smart testing.

<!-- _class: lower-third -->
Scene 09 - Summary

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
We've covered effective strategies for managing technical debt while maintaining focus. You now know how to fix issues, update systems, and move forward with confidence. In the next scene, we'll explore yak shaving and debugging, learning how to leverage AI and intuition for smart testing.

<!-- _class: screencapture -->
N/A

<div class="page-number">4/4</div>
