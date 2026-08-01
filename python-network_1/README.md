# Python - Network #1

Python scripts that fetch and manipulate internet resources, first with the
standard library `urllib` and then with the third-party `requests` package:
GET/POST requests, reading response headers, handling HTTP errors, parsing
JSON, Basic Authentication, and using the GitHub API.

## Requirements

- Interpreted on Ubuntu using `python3`
- First line of every file is `#!/usr/bin/python3`
- PEP 8 (pycodestyle) compliant; all files end with a new line
- All files are executable and documented (module docstrings)
- Dictionary values are read with `.get()`
- Code is guarded by `if __name__ == "__main__":`

## Tasks

| File | Package | Description |
|------|---------|-------------|
| `0-hbtn_status.py` | urllib | Fetch the status page, show type/content/utf8 |
| `1-hbtn_header.py` | urllib | Display the `X-Request-Id` response header |
| `2-post_email.py` | urllib | POST an `email` param, show the body |
| `3-error_code.py` | urllib | Show body or `Error code:` on `HTTPError` |
| `4-hbtn_status.py` | requests | Fetch the status page, show type/content |
| `5-hbtn_header.py` | requests | Display the `X-Request-Id` response header |
| `6-post_email.py` | requests | POST an `email` param, show the body |
| `7-error_code.py` | requests | Show body or `Error code:` when status >= 400 |
| `8-json_api.py` | requests | POST `q` to `/search_user`, print the JSON |
| `10-my_github.py` | requests | Show a GitHub id via Basic Authentication |
| `100-github_commits.py` | requests | List up to 10 repo commits (advanced) |
