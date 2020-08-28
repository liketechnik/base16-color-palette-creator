# Base 16 Color Palette Creator

A tool to generate a pretty image show casing a color palette from a base16
color scheme.

Example output for the
[DanQing](https://github.com/CosmosAtlas/base16-danqing-scheme) theme.
![DanQing color palette]( ./palette.png )

## Features

- Automatically generate a palette figure from base16 scheme yaml files
- Automatically determine whether the light or dark text color should be used
  for each color block

## Run

The script depends on `pillow` and `pyyaml`. You'll also need to supply your
own font. If you're on Linux, you can find your system fonts at
`/usr/share/fonts/`.

At the moment, everything is pretty hardcoded inside the script, so you'll need
to modify the script to get the output. Right now, if everything is supplied
correct, the output will be stored as `palette.png` in the same directory.

## TODO

Probably won't happen, but here are some possible things to improve on.

- [ ] Refactor the drawing for each color block
- [ ] Make the script self-contained (e.g., do not require editing to produce
  results)
- [ ] More styles of color palette output
