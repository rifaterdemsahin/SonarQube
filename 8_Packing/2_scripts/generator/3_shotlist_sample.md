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

# Welcome to *Data Science 101*  
### Your journey starts here  

![bg right:40% 80%](https://placehold.co/400x300/FFFFFF/667eea/png?text=Instructor)  

<!-- _class: footer -->
🎬 **SHOT ID:** INTRO-01  
📌 **LOs:** Hook audience, introduce topic  
🎥 **Video:** intro_01.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - INTRO-01]  
"Welcome to Data Science 101! I'm excited to guide you through this journey where you'll learn to transform raw data into meaningful insights. In this course, we'll cover everything from basic statistical concepts to advanced machine learning models."
```

---

### **2. 📊 Slides (Concept Explanation)**  
```markdown
---
marp: true
theme: default
style: |
  section {
    background: #f9f9f9;
    color: #333;
    font-family: 'Arial', sans-serif;
  }
  h1 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
  }
  .header {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.5em;
    font-weight: bold;
    color: #3498db;
  }
  .footer {
    position: absolute;
    right: 40px;
    bottom: 20px;
    font-size: 0.8em;
    color: #7f8c8d;
    text-align: right;
  }
  .script {
    position: absolute;
    left: 40px;
    bottom: 20px;
    font-size: 0.8em;
    color: #7f8c8d;
    text-align: left;
    width: 60%;
    font-style: italic;
  }
---

<!-- _class: header -->
📊 CORE CONCEPT  

# How Regression Works  

- Predicts continuous values (e.g., sales, temperature)  
- Finds relationships between variables  
- `y = mx + b` (simple linear case)  

![bg right:40% 90%](https://placehold.co/400x300/EEE/3498db/png?text=Graph+Example)  

<!-- _class: footer -->
🎬 **SHOT ID:** SLIDE-03  
📌 **LOs:** Explain regression basics  
🎥 **Video:** regression_slides.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Slides - SLIDE-03]  
"Regression is a powerful technique that allows us to predict continuous values. Unlike classification which categorizes data, regression helps us understand relationships between variables. At its simplest form, linear regression follows the equation y = mx + b, where m represents the slope and b is the y-intercept."
```

---

### **3. 💻 Screen Capture (Code Demo)**  
```markdown
---
marp: true
theme: default
style: |
  section {
    background: #282c34;
    color: #abb2bf;
    font-family: 'Fira Code', monospace;
  }
  .header {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.5em;
    font-weight: bold;
    color: #61afef;
  }
  .footer {
    position: absolute;
    right: 40px;
    bottom: 20px;
    font-size: 0.8em;
    color: #5c6370;
    text-align: right;
  }
  .script {
    position: absolute;
    left: 40px;
    bottom: 20px;
    font-size: 0.8em;
    color: #5c6370;
    text-align: left;
    width: 60%;
    font-style: italic;
  }
  code {
    font-size: 1.2em;
    line-height: 1.5;
  }
---

<!-- _class: header -->
💻 CODE DEMO  

```python
# Calculate correlation coefficient
import numpy as np

def pearson_r(x, y):
    """Compute Pearson correlation."""
    corr_matrix = np.corrcoef(x, y)
    return corr_matrix[0, 1]
```

![bg right:40% 80%](https://placehold.co/400x300/3e4451/61afef/png?text=IDE+Preview)  

<!-- _class: footer -->
🎬 **SHOT ID:** CODE-02  
📌 **LOs:** Show correlation calculation  
🎥 **Video:** code_demo_02.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Code Demo - CODE-02]  
"Let me show you how to calculate the Pearson correlation coefficient using NumPy. First, we import the library, then define a function that takes two arrays as input. The np.corrcoef function creates a correlation matrix, and we extract the correlation value at position [0,1] which represents the correlation between our two variables."
```

---

### **4. 🎤 Summary Talking Head**  
```markdown
---
marp: true
theme: default
style: |
  section {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    color: white;
    font-family: 'Arial', sans-serif;
  }
  h1 {
    text-align: center;
    margin-top: 1em;
  }
  ul {
    width: 60%;
    margin: 0 auto;
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
    opacity: 0.9;
    text-align: right;
  }
  .script {
    position: absolute;
    left: 40px;
    bottom: 20px;
    font-size: 0.8em;
    opacity: 0.9;
    text-align: left;
    width: 60%;
    font-style: italic;
  }
---

<!-- _class: header -->
🎤 KEY TAKEAWAYS  

# What You Learned Today  

1. Regression predicts continuous values  
2. Correlation measures linear relationships  
3. Python's NumPy simplifies math operations  

![bg right:40% 70%](https://placehold.co/400x300/FFFFFF/4facfe/png?text=Recap)  

<!-- _class: footer -->
🎬 **SHOT ID:** SUM-04  
📌 **LOs:** Reinforce 3 key points  
🎥 **Video:** summary_01.mp4  

<!-- _class: script -->
📝 **SCRIPT:** [Talking Head - SUM-04]  
"Let's recap what we've covered today. First, we learned that regression helps us predict continuous values like sales or temperature. Second, we explored correlation as a measure of linear relationships between variables. Finally, we saw how Python's NumPy library makes these mathematical operations straightforward. Next time, we'll build on these foundations to create our first predictive model."
```

---

### **Key Features of These Templates:**  
1. **Consistent Structure**  
   - Header (shot type + emoji)  
   - Body (content tailored to format)  
   - Footer (metadata aligned to right)
   - Script (aligned to left bottom, includes shot type and shot ID)

2. **Purpose-Built Styling**  
   - Gradient backgrounds for talking heads  
   - Dark mode for code demos  
   - Clean layouts for slides  

3. **Production-Ready Metadata**  
   - Unique shot IDs (e.g., `INTRO-01`)  
   - Learning objectives (LOs)  
   - Linked video filenames
   
4. **Script Section Added**
   - Located at bottom left of each slide
   - Includes shot type and shot ID reference
   - Contains sample script text aligned with slide content
   - Formatted in italic to distinguish from other content