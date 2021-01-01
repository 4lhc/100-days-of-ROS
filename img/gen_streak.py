#!/usr/bin/env python3

"""
Generate a streak chart from commit dates

Author: Sreejith S
"""

from PIL import Image, ImageDraw
import subprocess
from datetime import datetime, timedelta
from collections import Counter
from color import Color


start_date = '2020-12-25' #yyyy-mm-dd
local_repos = ['/home/sj/Projects/ROS/ROS',
               '/home/sj/Projects/ROS/AMR_omnibot',
               '/home/sj/Projects/Code/2021/100-days-of-ROS']

# image options
c = Color(palette='purple', alpha='ff')
im_shape = (1001, 161)
im_cell_width = 40


# Creating 100 days
date_format = '%Y-%m-%d'
sd = datetime.strptime(start_date, date_format)
dates = [(sd + timedelta(days=i+1)).strftime(date_format) for i in range(100)]
print(dates)
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
        print(day, dates[day], commit_count)
        color = c.get_cell_bg_maprange(commit_range, commit_count)
        border_color = c.get_cell_outline()
        draw.rectangle([0+i*iw, 0+j*iw, iw+i*iw, iw+j*iw], fill=color,
                       outline=border_color, width=3)
        day += 1

img.save('streak.png', 'PNG')

