---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**System Information:**
 - OS: [e.g. iOS]
 - Browser: [e.g. chrome, safari]
 - Version: [e.g. 22]

**Additional context**
Add any other context about the problem here.

```python
import matplotlib.pyplot as plt
import os

def plot_data(data):
    fig, ax = plt.subplots(figsize=(8,2))
    ax.text(0, 1, data, fontsize=10, color='black', wrap=True, va='top', ha='left')
    ax.axis('off')
    plt.show()

plot_data(os.uname())
```