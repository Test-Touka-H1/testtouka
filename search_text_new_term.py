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
    return found_files

# Hardcoded values
TEXT_TO_SEARCH = "brenton121345"
SEARCH_DIRECTORY = "."  # current folder

# Run search
results = search_text_in_files(TEXT_TO_SEARCH, SEARCH_DIRECTORY)

# Output results
if results:
    print("Text found in the following file(s):")
    for path in results:
        print(path)
else:
    print("No files contain the specified text.")