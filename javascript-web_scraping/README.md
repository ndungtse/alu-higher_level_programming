# JavaScript - Web scraping

Node.js scripts that read and write files with the `fs` module, make HTTP
requests with the `request` module, and parse JSON responses from the Star
Wars API and JSONPlaceholder.

## Requirements

- Interpreted on Ubuntu using `node`
- First line of every file is `#!/usr/bin/node`
- `semistandard` compliant; all files end with a new line
- All files are executable
- `var` is never used
- The `request` module is installed globally:

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

| File | Description |
|------|-------------|
| `0-readme.js` | Print a file's content (utf-8), or the error object |
| `1-writeme.js` | Write a string to a file (utf-8), or print the error object |
| `2-statuscode.js` | Print `code: <status code>` of a GET request |
| `3-starwars_title.js` | Print the title of the Star Wars film with the given id |
| `4-starwars_count.js` | Count the films featuring Wedge Antilles (character 18) |
| `5-request_store.js` | Store a web page's body in a file (utf-8) |
| `6-completed_tasks.js` | Count completed tasks per user id |
