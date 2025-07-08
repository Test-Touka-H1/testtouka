import matplotlib.pyplot as plt
import os

def plot_id():
    user_id = os.getuid()  # get your Unix-based user ID
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.text(0, 1, f"User ID: {user_id}", fontsize=12, color='black', va='top', ha='left')
    ax.axis('off')
    plt.show()

plot_id()