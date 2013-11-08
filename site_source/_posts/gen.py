# -*- coding: utf-8 -*-
content = '''
---
title: "滥竽充数的日志%s"
tags: 
  - 充数%s
  - 充数日志
---

今天无意家发现了个有趣的辅助学习Python的游戏——[Python Challenge](http://www.pythonchallenge.com/)。

总共33关，有些题实在得有柯南的脑力才能解开额>_<。

参考着官方答案思考动手一路下来，对Python的熟悉和理解绝对是大有裨益的，在此记录下闯关过程。

闯关代码放在Github上了。[这里](https://github.com/lingyunyumo/pythone-chanllenge-code)
'''

for no in range(11):
    fn = '1987-12-06-sample-post-a' + str(no) +'.md'
    fc = content % ('a' + str(no), 'A')
    open(fn, 'w').write(fc)
