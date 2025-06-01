# Bug Report Template

```python
import platform 

print(platform.uname())
```

```python
import os

def list_all_paths(directory):
    """Lists all file paths within a directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

if __name__ == "__main__":
    target_directory = input("Enter the directory path: ")
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        list_all_paths(target_directory)
    else:
        print("Invalid directory path.")
```

```python
import matplotlib.pyplot as plt
import os

def plot_data(data):
    fig, ax = plt.subplots(figsize=(8,2))
    ax.text(0, 1, data, fontsize=10, color='black', wrap=True, va='top', ha='left')
    ax.axis('off')
    plt.show()

plot_data(os.uname())