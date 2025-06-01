# Bug Report Template

## Historical Context
The term "bug" has been part of the engineering lexicon since the 1870s at least. At that time, it mainly appeared in reference to mechanical faults. In fact, Thomas Edison himself wrote a letter in 1878 where he made reference to "Bugs" referring to "little faults and difficulties" within machines.

## Preconditions
*List any necessary preconditions for reproducing the bug, such as:*
- Environment setup
- System configuration
- User permissions
- Required data state
- Any other relevant context

## Steps to Reproduce
*Provide a detailed, step-by-step guide to reproduce the issue:*
1. 
2. 
3. 

## Actual Result
*Describe what actually happens when following the steps above:*

## Expected Result
*Describe what should happen when following the steps above:*

## Additional Information
- **Browser/Environment:** 
- **Version:** 
- **Date Observed:** 
- **Severity:** 

## Screenshots/Logs
*If applicable, add screenshots, error logs, or other relevant attachments to help explain the problem.*

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