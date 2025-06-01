import os

def plot_data(data):
    print(data)

directories = [
    "/proc",
    "/usr",
    "/home",
    "/"
]

for dir_path in directories:
    try:
        contents = os.listdir(dir_path)
        plot_data(str(contents))
    except Exception as e:
        plot_data(f"Error accessing {dir_path}: {e}")

plot_data("Hello, world!")