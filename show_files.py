import os

def show_text_in_all_files(start_directory='.'):
    current_path = os.path.abspath(start_directory)
    print(f"📂 You are in: {current_path}\n")

    for root, dirs, files in os.walk(start_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"\n=== File: {file_path} ===")
                    print(content)
                    print("="*40)
            except Exception as e:
                print(f"Could not read {file_path}: {str(e)}")

if __name__ == "__main__":
    show_text_in_all_files()