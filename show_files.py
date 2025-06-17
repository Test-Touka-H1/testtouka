import os

def show_text_in_all_files(start_directory='.'):
    current_path = os.path.abspath(start_directory)
    print(f"📂 You are in: {current_path}\n")

    for root, dirs, files in os.walk(start_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    printed_header = False
                    for i, line in enumerate(lines):
                        line = line.strip()
                        if line:  # only print non-empty lines
                            if not printed_header:
                                print(f"\n📁 Directory : {root}")
                                print(f"📄 Filename  : {file}")
                                printed_header = True
                            print(f"📌 Line {i+1} : {line}")
            except:
                pass  # skip unreadable files

# Run it from the current directory
show_text_in_all_files(".")