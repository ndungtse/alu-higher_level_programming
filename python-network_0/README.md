# Python - Network #0

Bash scripts using `curl` to explore HTTP: request methods, headers, status
codes, query/POST parameters, redirects, and sending a JSON body.

## Requirements

- Tested on Ubuntu 20.04 LTS
- Each Bash script is exactly 3 lines (`wc -l` prints 3)
- First line is `#!/bin/bash`; second line is a comment describing the script
- All files end with a new line and are executable
- All `curl` commands use `-s` (silent mode)

## Tasks

| File | Description |
|------|-------------|
| `0-body_size.sh` | Display the response body size in bytes |
| `1-body.sh` | Display the body of a 200 response (follows redirects) |
| `2-delete.sh` | Send a `DELETE` request and display the body |
| `3-methods.sh` | List the HTTP methods the server accepts (`OPTIONS`) |
| `4-header.sh` | Send `X-HolbertonSchool-User-Id: 98` and display the body |
| `5-post_params.sh` | `POST` `email` and `subject` params, display the body |
| `100-status_code.sh` | Display only the response status code (no pipes) |
| `101-post_json.sh` | `POST` a file's JSON contents, display the body |
| `102-catch_me.sh` | Request `/catch_me` and display "You got me!" |

## Testing

The scripts target the container's web server on port `5000`, e.g.:

```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
```
