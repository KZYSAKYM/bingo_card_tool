# Bingo Card Tool

## Overview

- the tool to create bingo cards

## Usage

```sh
$ python3 -m pip install pillow
$ cd bingo_card_tool
$ wget https://4.bp.blogspot.com/-DfQbjLw91rM/W8hDmlqAD6I/AAAAAAABPd0/LxGmmB5LQPo_A6rQqfXxnD80XEUF8eSGACLcBGAs/s800/bingo_card_template.png
$ python3 ./bingo.py
```

## Configuration

Please modify `config.json` according to your bingo card template, numbers of cards, a range of bingo numbers, fonts, etc...

- Available Keys
  - bingo_template_path: Required: a path to your bingo template
  - bingo_width_pos: Required: X positions to insert numbers. the length needs to be 5.
  - bingo_height_pos: Required: Y positions to insert numbers. the length needs to be 5.
  - num_max: Optional: default == 100: Maximun of bingo numbers
  - num_mix: Optional: default == 1: Minimum of bingo numbers
  - font: Optional: default == "arial.ttf": Font
  - font_size: Optional: default == 80: Font Size
  - font_color: Optional: default == (20, 23, 26): RGB Font Color