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

## Note on XSS Prevention

When displaying search results in a web context, always ensure proper HTML escaping is implemented to prevent XSS attacks. For example, never directly inject user input or file contents into HTML without proper sanitization.