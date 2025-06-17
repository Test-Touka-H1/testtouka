import os
import logging
import argparse
from pathlib import Path
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_directory(directory: str) -> bool:
    """
    Validate if the directory exists and is accessible.
    """
    path = Path(directory)
    try:
        if not path.exists():
            logger.error(f"Directory does not exist: {directory}")
            return False
        if not path.is_dir():
            logger.error(f"Path is not a directory: {directory}")
            return False
        if not os.access(directory, os.R_OK):
            logger.error(f"Directory is not readable: {directory}")
            return False
        return True
    except Exception as e:
        logger.error(f"Error validating directory {directory}: {str(e)}")
        return False

def validate_search_text(text: str) -> bool:
    """
    Validate search text to prevent injection attacks.
    """
    if not text or len(text.strip()) == 0:
        logger.error("Search text cannot be empty")
        return False
    if len(text) > 1000:  # Reasonable limit for search text
        logger.error("Search text exceeds maximum length")
        return False
    return True

def search_text_in_files(target_text: str, start_directory: str, 
                        excluded_dirs: Optional[List[str]] = None) -> List[str]:
    """
    Search for text in files with improved security and error handling.
    
    Args:
        target_text: Text to search for
        start_directory: Directory to start search from
        excluded_dirs: List of directory names to exclude from search
    
    Returns:
        List of file paths containing the target text
    """
    if not validate_directory(start_directory) or not validate_search_text(target_text):
        return []

    excluded_dirs = excluded_dirs or ['.git', 'node_modules', 'venv']
    found_files = []
    
    try:
        for root, dirs, files in os.walk(start_directory):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Skip files larger than 10MB
                    if os.path.getsize(file_path) > 10_000_000:
                        logger.warning(f"Skipping large file: {file_path}")
                        continue
                        
                    # Skip binary files
                    if not is_text_file(file_path):
                        continue
                        
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line_num, line in enumerate(f, 1):
                            if target_text in line:
                                found_files.append(file_path)
                                logger.info(f"Found match in {file_path} at line {line_num}")
                                break
                except (IOError, UnicodeDecodeError) as e:
                    logger.warning(f"Error reading file {file_path}: {str(e)}")
                except Exception as e:
                    logger.error(f"Unexpected error processing {file_path}: {str(e)}")
    except Exception as e:
        logger.error(f"Error during file search: {str(e)}")
    
    return found_files

def is_text_file(file_path: str) -> bool:
    """
    Check if a file is likely to be a text file.
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            return not bool(b'\x00' in chunk)
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description='Securely search for text in files')
    parser.add_argument('--text', required=True, help='Text to search for')
    parser.add_argument('--directory', default='.', help='Directory to search in')
    parser.add_argument('--exclude', nargs='+', help='Directories to exclude')
    
    args = parser.parse_args()
    
    results = search_text_in_files(args.text, args.directory, args.exclude)
    
    if results:
        print("\nText found in the following file(s):")
        for path in results:
            print(path)
    else:
        print("\nNo files contain the specified text.")

if __name__ == '__main__':
    main()