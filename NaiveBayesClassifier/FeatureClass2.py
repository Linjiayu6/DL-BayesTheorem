#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
[2] Designing a Feature class
有了数据之后, 我们需要处理当前的数据, 并创建模型
1. 分类
2. 每个类需要label, label是 height, firstnames
'''

from collections import Counter
import numpy as np

class Feature:
  '数据特征值处理' # 类文档字符串
  def __init__ (self, data, name = None, bin_width = None) :
    self.name = name
    self.bin_width = bin_width

    '''
    原始数据
    [ 184 175 187 192 204 180 184 174 177 200 193 189 188 187 187 190 180 155
      201 171 163 191 175 170 178 191 176 168 169 173 180 212 189 174 167 193
      164 171 165 198 185 175 195 164 187 192 175 190 164 161
    ]

    [ 149 174 183 138 145 161 179 162 148 196 163 159 150 170 169 167 168 170
      167 152 155 151 166 165 158 152 159 163 174 131 154 159 159 177 180 164
      163 161 183 170 167 166 180 161 170 172 168 156 167 167
    ]
    '''
    
    # 定义该 x轴 可分区间
    if bin_width :
      # [1] 分区间, 先找最大, 最小值
      self.min = min(data)
      self.max = max(data)

      # [2] 分区间 eg: 区间范围 np.arange(3,7,2) =>  array([3, 5])
      # 最小155, 最大212 
      bins = np.arange(
        (self.min // bin_width) * bin_width, 
        (self.max // bin_width) * bin_width, # 取整数
        bin_width
      )
      # bins该区间为 [155 160 165 170 175 180 185 190 195 200 205]

      # [3] [数该区间中, 出现的 ******次数****** ]
      #     例如 155-160是一个区间, 出现次数为1
      #
      # np.histogram *返回值有两个
      # eg: np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
      #     0-1: 无 0; 1-2: 2(因为有2个1); 2-3: 1
      #     返回值为 array([0, 2, 1])
      freq, bins = np.histogram(data, bins)

      # [4] 将区间值 和 对应区间出现次数 创建obj(dictionary)
      # [a, b], [10, 66] => { a: 10, b: 66 }

      '''
        返回数据
        freq_dict: {160: 5, 195: 2, 165: 4, 200: 3, 170: 6, 175: 7, 180: 5, 185: 8, 155: 1, 190: 8}
        freq_dict: {160: 8, 130: 1, 165: 11, 135: 1, 170: 7, 140: 0, 175: 2, 145: 3, 180: 4, 150: 5, 185: 0, 155: 7}

        freq_sum: 都是49
      '''
      self.freq_dict = dict(zip(bins, freq))
      self.freq_sum = sum(freq)

    else:
      self.freq_dict = dict(Counter(data))
      self.freq_sum = sum(self.freq_dict.values())
  
  def printSelf (self) :
    print('[Feature Data]', self.name, self.freq_dict, self.freq_sum)

  def frequency (self, value, bin_width = 5) :
    if self.bin_width:
      value = (value // self.bin_width) * self.bin_width
    if value in self.freq_dict:
      return self.freq_dict[value]
    else :
      return 0



# 创建特征值
# x轴: gender
# y轴: 特征值出现的次数
def createFeature (genders, heights) :
  fts = {}
  # eg: gender => 'male'
  for gender in genders :
    fts[gender] = Feature(heights[gender], name = gender, bin_width = 5)

  return fts