import matplotlib.pyplot as plt
import getpass  # safer for getting the current username

def plot_data(data):
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.text(0, 1, data, fontsize=10, color='black', wrap=True, va='top', ha='left')
    ax.axis('off')
    plt.show()

# Replaces `os.uname()` with the current username
plot_data(getpass.getuser())