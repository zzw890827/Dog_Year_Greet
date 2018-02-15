# -*- coding: utf-8 -*-

import jieba
import matplotlib
import codecs
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

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


back = imread('dog.png')

wc = WordCloud(
    background_color='white',
    max_words=300,
    mask=back,
    max_font_size=200,
    font_path='SimHei.ttf',

)

jieba.add_word('李文骞')
jieba.add_word('赵仲文')
jieba.add_word('刘成巧')
jieba.add_word('蛋糕君')


def stop_word(texts):
    word_lists = []
    word_generator = jieba.cut(texts, cut_all=False)
    for word in word_generator:
        word_lists.append(word)
    return ' '.join(word_lists)


text = stop_word(content)

wc.generate(text)
image_color = ImageColorGenerator(back)
plt.show(wc)
plt.axis('off')
plt.figure()
plt.imshow(wc)
plt.axis('off')
wc.to_file('greeting.png')
