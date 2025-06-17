import os

def search_text_in_files(target_text, start_directory='.'):
    found_files = []
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    for line in f:
                        if target_text in line:
                            found_files.append(file_path)
                            break
            except:
                pass  # skip unreadable files
    return fo