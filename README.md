# Secure File Search Utility

This utility provides a secure way to search for text within files while implementing various security controls and best practices.

## Security Features

1. Input Validation
   - Directory path validation
   - Search text validation
   - Protection against directory traversal

2. Resource Controls
   - File size limits
   - Binary file detection
   - Excluded directory support

3. Error Handling & Logging
   - Comprehensive error handling
   - Detailed logging
   - Failed operation tracking

## Usage

```bash
python secure_file_search.py --text "search_text" --directory "/path/to/search" --exclude node_modules .git venv
```

### Arguments

- `--text`: (Required) Text to search for
- `--directory`: (Optional) Directory to search in (defaults to current directory)
- `--exclude`: (Optional) List of directories to exclude from search

## Security Guidelines

1. Never hardcode sensitive information in scripts
2. Always validate and sanitize input
3. Use appropriate access controls
4. Monitor and log operations
5. Implement proper error handling
6. Restrict search scope to necessary directories
7. Be cautious with large files and binary data

## Security Warnings

### Insecure Implementation Example

Below is an example of an insecure implementation that should be avoided:

```python
# DON'T DO THIS - Insecure Implementation
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
```

Security issues with the above code:
1. No input validation
2. Silently ignores all errors with bare except
3. Uses errors='ignore' which can mask security issues
4. No protection against binary files or large files
5. No logging or monitoring
6. No directory exclusion support
7. No resource controls

Always use the secure implementation provided in this utility instead.

## Note on XSS Prevention

When displaying search results in a web context, always ensure proper HTML escaping is implemented to prevent XSS attacks. For example, never directly inject user input or file contents into HTML without proper sanitization.

### Additional Security Considerations

1. Never hardcode sensitive search terms in your code
2. Always use command-line arguments or environment variables for configuration
3. Implement rate limiting for web-based search interfaces
4. Consider implementing file type restrictions
5. Use proper encoding (UTF-8) instead of ignoring encoding errors