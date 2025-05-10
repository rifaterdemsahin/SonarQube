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
  code {
    font-size: 1.2em;
    line-height: 1.5;
  }
---

<!-- _class: header -->
💻 CODE DEMO  
#### Shot Type: Screen Capture

```python
# Calculate correlation coefficient
import numpy as np

def pearson_r(x, y):
    """Compute Pearson correlation."""
    corr_matrix = np.corrcoef(x, y)
    return corr_matrix[0, 1]