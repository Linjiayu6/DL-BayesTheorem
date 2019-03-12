#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
[3] create BarChart
'''
import matplotlib.pyplot as plt

def draw (genders, fts) :
  for gender in genders :
    # list() 将元组转换为列表
    # eg: (123, 'xyz', 'zara', 'abc') -> [123, 'xyz', 'zara', 'abc']
    frequencies = list(fts[gender].freq_dict.items())


    # frequencies值为: [(155, 1), (195, 2), (200, 3), (165, 4), (160, 5), (180, 5), (170, 6), (175, 7), (185, 8), (190, 8)]
    #                 [(140, 0), (185, 0), (130, 1), (135, 1), (175, 2), (145, 3), (180, 4), (150, 5), (170, 7), (155, 7), (160, 8), (165, 11)]
    # 按照 出现次数 从小到大排序
    frequencies.sort(key=lambda x: x[1])

    # X ((155, 195, 200, 165, 160, 180, 170, 175, 185, 190) Y (1, 2, 3, 4, 5, 5, 6, 7, 8, 8))
    # X ((140, 185, 130, 135, 175, 145, 180, 150, 170, 155, 160, 165) Y (0, 0, 1, 1, 2, 3, 4, 5, 7, 7, 8, 11))
    X, Y = zip(*frequencies)

    color = 'red'
    bar_width = 3
    if gender == 'male' :
      color = 'black'
      bar_width = 4

    plt.bar(X, Y, bar_width, color=color, alpha=0.75, label=gender)

  plt.legend(loc='upper right')
  plt.show()