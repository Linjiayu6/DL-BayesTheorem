#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 为了解决 int / int 只返回int问题 详见 https://docs.pythontab.com/learnpython/103/
from __future__ import division

'''
An NBclass contains one or more Feature classes. 
The name of the NBclass will be stored in self.name.
'''
class NBClass :
  def __init__ (self, name, *features) :
    self.name = name # gender 例如 'female'
    self.features = features # female的特征值, 例如 xxx区间 出现多少次值

  # probability: 发生的概率 
  # feature_value 可以理解为x轴当前坐标值
  def probability_value_By_given_features (self, feature_value, feature) :
    # freq_sum 出现次数值的总数
    if feature.freq_sum == 0:
      return 0
    else :
      '''
        已知每个区间出现次数 / 总次数
      '''
      y = feature.frequency(feature_value)
      total = feature.freq_sum
      # print('probability_value_By_given_features [y/total]', self.name, y, total, y / total)
      return y / total


# 分类器: 使用到 NaiveBayesClass 和 FeatureClass
class Classifier :
  def __init__ (self, *nbclasses) :
    self.nbclasses = nbclasses

  # best_only=True
  def prob(self, *d):
    nbclasses = self.nbclasses
    probability_list = []
    '''
    例如: 
        在155该区间, female值为6, male为1
        prob为 6/48 = 0.125 (female总数) 和 1/49(male总数) = 0.020408163265306 计算在该区间 男女出现的概率
        probability_list: [(0.020408163265306121, 'male'), (0.125, 'female')]
    '''
    for nbclass in nbclasses:            
      ftrs = nbclass.features
      prob = 1
      for i in range(len(ftrs)):
        prob *= nbclass.probability_value_By_given_features(d[i], ftrs[i])
      probability_list.append((prob, nbclass.name))

    '''
      例如: 在155区间
        probability_list: [(0.020408163265306121, 'male'), (0.125, 'female')]
        prob_values: [0.020408163265306121, 0.125]
        prob_sum: 0.020408163265306121 + 0.125 = 0.14540816326530612
    '''
    prob_values = [f[0] for f in probability_list]
    prob_sum = sum(prob_values)

    # 如果总和为0, 说明他们出现的概率相同 例如: ([(0.5, 'male'), (0.5, 'female')])

    '''
    求在该区间, female 和 male占比多少
      0.020408163265306121 / 0.14540816326530612 = 0.14035087719298245
      0.125 / 0.14540816326530612 = 0.8596491228070176
    
    [(0.14035087719298245, 'male'), (0.85964912280701755, 'female')]
    '''
    if prob_sum==0 :
        number_classes = len(self.nbclasses)
        pl = []
        for prob_element in probability_list:
            pl.append( ((1 / number_classes), prob_element[1]))
        probability_list = pl
    else :
      probability_list = [ (p[0] / prob_sum, p[1])  for p in probability_list]
    return probability_list
