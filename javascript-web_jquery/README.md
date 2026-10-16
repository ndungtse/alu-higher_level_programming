# JavaScript - Web jQuery

Front-end scripts that select and update HTML elements, first with plain
`document.querySelector` and then with jQuery 3.x: changing styles and
classes, editing text, adding elements, binding click events, and fetching
data with jQuery Ajax (`$.get`) without reloading the page.

## Requirements

- Interpreted on Chrome (version 57.0)
- jQuery 3.x, imported with
  `<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>`
- `semistandard` compliant with `semistandard *.js --global $`
- All files end with a new line
- `var` is never used

## Tasks

| File | Description |
|------|-------------|
| `0-script.js` | Set the `<header>` color to red with `document.querySelector` |
| `1-script.js` | Set the `<header>` color to red with jQuery |
| `2-script.js` | Turn the `<header>` red on click of `DIV#red_header` |
| `3-script.js` | Add the class `red` to `<header>` on click of `DIV#red_header` |
| `4-script.js` | Toggle `<header>` between `red` and `green` on click of `DIV#toggle_header` |
| `5-script.js` | Append `<li>Item</li>` to `UL.my_list` on click of `DIV#add_item` |
| `6-script.js` | Set the `<header>` text to `New Header!!!` on click of `DIV#update_header` |
| `7-script.js` | Show the name of Star Wars character 5 in `DIV#character` |
| `8-script.js` | List every Star Wars film title in `UL#list_movies` |
| `9-script.js` | Show the French "hello" in `DIV#hello` once the DOM is loaded |

## Note on task 9

`https://fourtonfish.com/hellosalut/?lang=fr` now redirects (twice) to
`https://hellosalut.stefanbohacek.com/?lang=fr`. The redirects send no
`Access-Control-Allow-Origin` header, so the browser blocks the request.
`9-script.js` therefore calls the API's current URL directly.
