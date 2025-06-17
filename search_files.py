import os

def search_text_in_files(keyword, start_directory='.'):
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if keyword in line:
                            print(f"\n📁 Directory : {root}")
                            print(f"📄 Filename  : {file}")
                            print(f"📌 Line {i+1} : {line.strip()}")
            except:
                pass  # skip unreadable files

# Hardcoded search word
KEYWORD = "BRENTON"
SEARCH_DIRECTORY = "."  # current di_