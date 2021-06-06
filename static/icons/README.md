# Phosphor Icons

Phosphor Icons from <https://github.com/phosphor-icons/phosphor-icons>. Last update from 5th June 2021.

## How to Update Icons
- Go to the repository of Phosphor Icons: <https://github.com/phosphor-icons/phosphor-icons>
- Copy `phosphor.svg`, `phosphor.ttf`, and `phosphor.woff` from `src/font` into this directory.
- Copy `phosphor.css` from `src/css` into this directory and change lines 1 to 8 as following to point to the local icon assets:

```CSS
@font-face {
  font-family: "Phosphor";
  src: url("./phosphor.ttf")
      format("truetype"),
    url("./Phosphor.woff")
      format("woff"),
    url("./Phosphor.svg")
      format("svg");
```