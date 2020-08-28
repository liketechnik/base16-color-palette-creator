""" Create a pretty image base on a base16 color scheme file

This script allow users to create pretty color palette images based on the
base16 color schemes.

A `color-scheme.yaml` is parsed to get the colors
"""

import yaml
from PIL import Image, ImageDraw, ImageFont

BASE16_YAML = "/home/cosmos/Repos/base16-danqing-scheme/danqing.yaml"
BORDER_GAP = 20
SQUARE_SIZE = 250
FONT_SIZE = 36
FONT_FILE = "./sarasa-semibolditalic.ttc"


def get_color(colors, index):
    if index < 0 or index > 15:
        raise Exception(
            "Index should be between 0 (0x00) and 15 (0x0F) inclusive")
    return '#' + colors['base0' + hex(index)[-1].upper()]


def hex2rgb(v):
    v = v.lstrip('#')
    lv = len(v)
    return tuple(int(v[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def is_light_bg(color_hex):
    """
    Determine whether the color is considered light or dark. To be used to set
    font color.

    Reference:
    https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
    """
    rgb = list(hex2rgb(color_hex))
    new_rgb = []
    for c in rgb:
        c = c / 255.0
        if c <= 0.03928:
            c = c / 12.92
        else:
            c = ((c + 0.055) / 1.055)**2
        new_rgb.append(c)
    r, g, b = new_rgb[0], new_rgb[1], new_rgb[2]
    L = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return L > 0.179


if __name__ == "__main__":
    # Read the base16 color scheme
    with open(BASE16_YAML, 'r', encoding='utf-8') as f:
        colors = yaml.load(f, Loader=yaml.FullLoader)

    font = ImageFont.truetype(FONT_FILE, FONT_SIZE)

    color_bg = get_color(colors, 0)
    color_fg = get_color(colors, 5)

    color_names = [
        "", "", "", "", "", "素", "", "", "酡颜", "姜黄", "缃色", "蟹壳青", "湖蓝", "雪青",
        "丁香紫", "琥珀"
    ]

    # Image setup
    image_width = BORDER_GAP * 9 + SQUARE_SIZE * 8
    image_height = BORDER_GAP * 4 + SQUARE_SIZE * 2 + FONT_SIZE

    im = Image.new('RGBA', (image_width, image_height), get_color(colors, 0))
    draw = ImageDraw.Draw(im)

    # Palatte Name
    draw.text((BORDER_GAP, BORDER_GAP),
              colors['scheme'] + " 丹青",
              color_fg,
              font=font)

    # Draw each color block
    for i in range(2):
        for j in range(8):
            color_index = i * 8 + j
            color_hex = get_color(colors, color_index)
            color_name = color_names[color_index]
            text_color = color_bg if is_light_bg(color_hex) else color_fg

            draw.rectangle(
                (BORDER_GAP *
                 (j + 1) + SQUARE_SIZE * j, FONT_SIZE + BORDER_GAP *
                 (i + 2) + SQUARE_SIZE * i, BORDER_GAP *
                 (j + 1) + SQUARE_SIZE * (j + 1), FONT_SIZE + BORDER_GAP *
                 (i + 2) + SQUARE_SIZE * (i + 1)),
                fill=color_hex,
                outline=None)
            color_text_size = font.getsize(color_hex)
            draw.text((BORDER_GAP * (j + 2) + SQUARE_SIZE * j,
                       FONT_SIZE + BORDER_GAP * (i + 3) + SQUARE_SIZE * i),
                      color_hex,
                      text_color,
                      font=font)
            if color_name:
                color_name_size = font.getsize(color_name)
                draw.text(
                    (BORDER_GAP * (j) + SQUARE_SIZE *
                     (j + 1) - color_name_size[0], FONT_SIZE + BORDER_GAP *
                     (i + 1) + SQUARE_SIZE * (i + 1) - color_name_size[1]),
                    color_name,
                    text_color,
                    font=font)

    im.save('palette.png', quality=100)
