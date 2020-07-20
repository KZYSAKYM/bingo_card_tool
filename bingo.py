#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw
import json
import random

# Use template located in https://www.irasutoya.com/2018/11/blog-post_86.html for test
BINGO_TEMPLATE_PATH = "bingo_card_template.png"
BINGO_NUM_MAX = 100
BINGO_NUM_MIN = 1
BINGO_CARD_NUM = 100
BINGO_WIDTH_POS = (66, 174, 281, 391, 502)
BINGO_HEIGHT_POS = (220, 330, 440, 550, 660)
BINGO_FONT = "arial.ttf"
BINGO_FONT_SIZE = 80
BINGO_FONT_COLOR = (20, 23, 26)

def load_global_config(path):
    global BINGO_TEMPLATE_PATH, BINGO_NUM_MAX, \
        BUNGO_NUM_MIN, BINGO_CARD_NUM, \
        BINGO_WIDTH_POS, BINGO_HEIGHT_POS, \
        BINGO_FONT, BINGO_FONT_SIZE, BINGO_FONT_COLOR
    d = None
    with open(path) as f:
        d = json.load(f)
    configs = (
        # required?, var_name, key_name, type
        (True,  BINGO_TEMPLATE_PATH,   "bingo_template_path",  str),
        (True,  BINGO_WIDTH_POS,       "bingo_width_pos",      (list or tuple)),
        (True,  BINGO_HEIGHT_POS,      "bingo_height_pos",     (list or tuple)),
        (False, BINGO_NUM_MAX,         "num_max",              int),
        (False, BINGO_NUM_MIN,         "num_min",              int),
        (False, BINGO_CARD_NUM,        "card_num",             int),
        (False, BINGO_FONT,            "font",                 str),
        (False, BINGO_FONT_SIZE,       "font_size",            int),
        (False, BINGO_FONT_COLOR,      "font_color",           (list or tuple)),
    )
    # common check
    for config in configs:
        err = None
        var = None
        try:
            var = d[config[2]]
        except KeyError:
            err = KeyError("%s" % (config[2])) if config[0] else None
        if not isinstance(var, config[3]):
            err = TypeError("%s: %s != %s" % (config[2], config[3], type(var)))
        if err is not None:
            raise err
    
    # specific check
    if BINGO_NUM_MIN >= BINGO_NUM_MAX:
        raise ValueError("BINGO_NUM_MIN is larger than BINGO_NUM_MAX")
    if len(BINGO_WIDTH_POS) != 5:
        raise ValueError("BINGO_WIDTH_POS's length needs to be 5")
    if len(BINGO_HEIGHT_POS) != 5:
        raise ValueError("BINGO_HEIGHT_POS's length needs to be 5")

def open_bingo_template():
    return Image.open(BINGO_TEMPLATE_PATH).copy()

def _create_bingo_card(img):
    w = BINGO_WIDTH_POS
    h = BINGO_HEIGHT_POS
    positions = (
        (w[0], h[0]), (w[1], h[0]), (w[2], h[0]), (w[3], h[0]), (w[4], h[0]),
        (w[0], h[1]), (w[1], h[1]), (w[2], h[1]), (w[3], h[1]), (w[4], h[1]),
        (w[0], h[2]), (w[1], h[2]),               (w[3], h[2]), (w[4], h[2]),
        (w[0], h[3]), (w[1], h[3]), (w[2], h[3]), (w[3], h[3]), (w[4], h[3]),
        (w[0], h[4]), (w[1], h[4]), (w[2], h[4]), (w[3], h[4]), (w[4], h[4]),
    )
    font_color = BINGO_FONT_COLOR
    font = ImageFont.truetype(font=BINGO_FONT, size=BINGO_FONT_SIZE)
    draw = ImageDraw.Draw(img)
    nums = [i for i in range(BINGO_NUM_MIN, BINGO_NUM_MAX, 1)]
    for pos in positions:
        num = random.choice(nums)
        draw.text(pos, "%02d" % (num), font_color, font=font)

def create_bingo_card(card_num):
    for i in range(card_num):
        img  = open_bingo_template()
        _create_bingo_card(img)
        img.save("bingo_card%d.png" % (i))

if __name__ == "__main__":
    load_global_config("config.json")
    create_bingo_card(BINGO_CARD_NUM)