#!/usr/bin/env python3

"""
Generate a streak chart from commit dates

Author: Sreejith S
"""

from PIL import Image, ImageDraw, ImageColor
import subprocess
from datetime import datetime, timedelta
from collections import Counter
from math import ceil

start_date = '2020-12-25' #yyyy-mm-dd
date_format = '%Y-%m-%d'
local_repos = ['/home/sj/Projects/ROS/ROS',
	       '/home/sj/Projects/ROS/AMR_omnibot',
	       '/home/sj/Projects/Code/2021/100-days-of-ROS']

# image options
im_shape = (1001, 161)
im_cell_width = 40
im_bg = (255, 255, 255, 255)
im_cell_fill_empty = (230, 230, 230, 255)
colors = ['#b2dfdb', '#80cbc4', '#4db6ac', '#26a69a']
alpha = 'ff' #200
im_cell_fill_full = [ImageColor.getrgb(c + alpha) for c in colors]
im_cell_outline = im_bg#ImageColor.getrgb('#00796b' + alpha)


# Creating 100 days
sd = datetime.strptime(start_date, date_format)
dates = [(sd + timedelta(days=i)).strftime(date_format) for i in range(100)]
date_count = Counter(dates)

# Counting commits in local_repos
cmd = 'git log --date=short --pretty=format:%cd --since=' + start_date
for cwd in local_repos:
    output = subprocess.run(cmd.split(), stdout=subprocess.PIPE, cwd=cwd)
    dates_stdout = output.stdout.decode('utf-8').split()
    date_count.update(dates_stdout)
# print(date_count)


def maprange(a, b, s):
    # https://rosettacode.org/wiki/Map_range#Python
    (a1, a2), (b1, b2) = a, b
    return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))


img = Image.new('RGBA', im_shape, im_bg)
draw = ImageDraw.Draw(img)
iw = im_cell_width

commit_range = (1, max(date_count.values()))
color_range = (0, len(im_cell_fill_full)-1)
day = 0

for j in range(4):
    for i in range(25):
        date_str = dates[day]
        day += 1
        commit_count = date_count[date_str] - 1
        if commit_count == 0:
            color = im_cell_fill_empty
            border_color = im_bg
        else:
            color_num = maprange(commit_range, color_range, commit_count)
            color = im_cell_fill_full[ceil(color_num)]
            border_color = im_cell_outline
        draw.rectangle([0+i*iw, 0+j*iw, iw+i*iw, iw+j*iw], fill=color,
                       outline=border_color, width=3)

from PIL import ImageFilter
img.filter(ImageFilter.GaussianBlur(10))
img.save('streak.png', 'PNG')

