# -*- coding: utf-8 -*-

from string import punctuation
import re
import codecs

__verbose__ = True
__debug_mode__ = False

# 标点符号（中英文）
punc = punctuation + u'.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：'

if __verbose__:
    print('输出标点符号')
if __debug_mode__:
    print(punc)

if __verbose__:
    print('打开元语料库')
file = codecs.open('./Corpus/monolingual_greeting_corpus.txt', encoding='utf-8')
if __verbose__:
    print('打开目标语料库')
out = codecs.open('./Corpus/monolingual_greeting_corpus_clean.txt', 'w', encoding='utf-8')

# 正则表达式去除标点符号
if __verbose__:
    print('写入文件')
for line in file:
    line = re.sub(r'[{}]+'.format(punc), ' ', line)
    if __debug_mode__:
        print(line)
    out.write(line + ' ')

if __verbose__:
    print('写入文件成功！')
file.close()
out.close()
