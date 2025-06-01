import matplotlib.pyplot as plt
import os

def plot_data(data):
    fig, ax = plt.subplots(figsize=(8,2))
    ax.text(0, 1, data, fontsize=10, color='black', wrap=True, va='top', ha='left')
    ax.axis('off')
    plt.show()

# Membaca dan menampilkan isi dari file /etc/passwd
try:
    with open("/etc/passwd", "r") as file:
        content = file.read()
        plot_data(content)
except Exception as e:
    plot_data(f"Error reading /etc/passwd: {e}")