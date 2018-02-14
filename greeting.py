# -*- coding: utf-8 -*-

import numpy as np
import jieba
import pandas
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import wordcloud
import codecs

__verbose__ = True
__debug_mode__ = False

# 分词
if __verbose__:
    print('读取语料库文件')
file = codecs.open('./Corpus/monolingual_greeting_corpus_clean.txt', 'r', encoding='utf-8')
content = file.read()
if __verbose__:
    print('文件读取结束')
file.close()
segment = []
# 使用`jieba`分词
segs = jieba.cut(content)
if __verbose__:
    print('分词结果输出')
for seg in segs:
    if len(seg) > 1 and seg != '\n':
        segment.append(seg)
print(segment)