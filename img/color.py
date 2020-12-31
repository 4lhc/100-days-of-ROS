#!/usr/bin/env python3

"""
Color class for gen_streak
Author: Sreejith S

palettes: [kawanet/material-colors.json]
"""

from PIL import ImageColor
import json

class Color:
    def __init__(self, palette="amber", alpha='ff'):
        self._im_bg = '#ffffff'
        self._cell_bg = '#e6e6e6'
        self._cell_outline = '#ffffff'
        self._alpha = alpha
        self._c_ids = ['50', '100', '200', '300', '400',
                       '500', '600', '700', '800', '900']

        with open("material-colors.json", 'r') as fp:
            palettes = json.load(fp)
            color_dict = palettes[palette]
            self._im_cell_fill_colors = [color_dict[c] for c in self._c_ids]

    def get_im_bg(self):
        return ImageColor.getrgb(self._im_bg + self._alpha)

    def get_cell_bg(self):
        return ImageColor.getrgb(self._cell_bg + self._alpha)

    def get_cell_outline(self):
        return ImageColor.getrgb(self._cell_outline + self._alpha)

    def get_cell_bg_maprange(self, range, value):
        # https://rosettacode.org/wiki/Map_range#Python
        if value == 0:
            return self.get_cell_bg()
        else:
            color_range = (0, len(self._im_cell_fill_colors)-1)
            (r1, r2), (c1, c2) = range, color_range
            color_id =  int(c1 + ((value - r1) * (c2 - c1) / (r2 - r1)))
            return ImageColor.getrgb(self._im_cell_fill_colors[color_id] + self._alpha)




