# JavaScript - Objects, Scopes and Closures

JavaScript classes and modules run with Node.js: defining classes with the
`class` notation, instance attributes and methods, `this`, inheritance with
`extends` and `super()`, module-level scope, and closures.

## Requirements

- Interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- First line of every file is `#!/usr/bin/node`
- `semistandard` compliant; all files end with a new line
- All files are executable
- `var` is never used

## Tasks

| File | Description |
|------|-------------|
| `0-rectangle.js` | Empty class `Rectangle` |
| `1-rectangle.js` | `Rectangle` with `width` and `height` set from `w` and `h` |
| `2-rectangle.js` | Empty object when `w` or `h` is not a positive integer |
| `3-rectangle.js` | Adds `print()`, drawing the rectangle with `X` |
| `4-rectangle.js` | Adds `rotate()` (swap sides) and `double()` (scale by 2) |
| `5-square.js` | `Square` extends `Rectangle` of `4-rectangle.js` via `super()` |
| `6-square.js` | `Square` extends `5-square.js`, adds `charPrint(c)` (default `X`) |
| `7-occurrences.js` | `nbOccurences(list, searchElement)` counts matches |
| `8-esrever.js` | `esrever(list)` returns the list reversed, without `reverse` |
| `9-logme.js` | `logMe(item)` prints `<count already printed>: <item>` |
| `10-converter.js` | `converter(base)` returns a closure converting base 10 to `base` |
