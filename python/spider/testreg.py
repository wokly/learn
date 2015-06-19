#coding:UTF-8

import  urllib
import re

__author__ = 'wwx199990'
raw_url = 'http://movie.douban.com/chart'
html = urllib.urlopen(raw_url).read().decode("utf-8")
reg_name = r'<img src=".*" alt=".*?" class=""/>'
tests = re.findall(reg_name,html)
for test in tests:
    print test.encode("gb18030")
