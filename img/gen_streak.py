#!/usr/bin/env python3

"""
Generate a streak chart from commit dates

MIT License

Copyright (c) 2020 Sreejith Sasidharan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PIL import Image, ImageDraw
import subprocess
from datetime import datetime, timedelta
from collections import Counter
from color import Color
import sys

start_date = '2020-12-25' #yyyy-mm-dd
local_repos = ['/home/sj/Projects/ROS/ROS',
               '/home/sj/Projects/ROS/AMR_omnibot',
               '/home/sj/Projects/Code/2021/100-days-of-ROS']

# image options
try:
    c = Color(palette=sys.argv[1], alpha='ff')
except IndexError:
    c = Color(palette='yellow', alpha='ff')

im_shape = (1001, 161)
im_cell_width = 40


# Creating 100 days
date_format = '%Y-%m-%d'
sd = datetime.strptime(start_date, date_format)
dates = [(sd + timedelta(days=i+1)).strftime(date_format) for i in range(100)]
date_count = Counter(dates)

# Counting commits in local_repos
cmd = 'git log --date=short --pretty=format:%cd --since=' + start_date
for cwd in local_repos:
    output = subprocess.run(cmd.split(), stdout=subprocess.PIPE, cwd=cwd)
    dates_stdout = output.stdout.decode('utf-8').split()
    date_count.update(dates_stdout)


img = Image.new('RGBA', im_shape, c.get_im_bg())
draw = ImageDraw.Draw(img)
iw = im_cell_width

commit_range = (0, max(date_count.values())-1)
day = 0

for j in range(4):
    for i in range(25):
        date_str = dates[day]
        commit_count = date_count[date_str] - 1
        color = c.get_cell_bg_maprange(commit_range, commit_count)
        border_color = c.get_cell_outline()
        draw.rectangle([0+i*iw, 0+j*iw, iw+i*iw, iw+j*iw], fill=color,
                       outline=border_color, width=3)
        day += 1

img.save('streak.png', 'PNG')

