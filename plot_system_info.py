import matplotlib.pyplot as plt
import os

def plot_data(data):
 fig, ax = plt.subplots(figsize=(8,2))
 ax.text(0, 1, data, fontsize=10, color='black', wrap=True, va='top', ha='left')
 ax.axis('off')
 plt.show()

plot_data(os.uname())