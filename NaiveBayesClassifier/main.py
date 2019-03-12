#!/usr/bin/python
# -*- coding: UTF-8 -*-

from handleData1 import onData 
# 1. 数据 ---------------------------------
allData = onData()

genders = allData['genders']
persons = allData['persons']
firstnames = allData['firstnames']
heights = allData['heights']

# 2. 创建特征值 ---------------------------------
fts = {}
from FeatureClass2 import createFeature
# {'male': <__main__.Feature instance at 0x10ad8a248>, 'female': <__main__.Feature instance at 0x10ad8a3f8>}
fts = createFeature(genders, heights)

# print 当前值
fts['male'].printSelf()
fts['female'].printSelf()


# 3. draw chart ---------------------------------
from matlab3 import draw
draw (genders, fts)


# 4. Bayes ---------------------------------
from NaiveBayesClass4 import NBClass, Classifier
cls = {}
for gender in genders:
  cls[gender] = NBClass(gender, fts[gender])

c = Classifier(cls["male"], cls["female"])
# range(130, 220, 5) = [130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215]
for i in range(130, 220, 5):
  # i当前区间值 = x轴区间值
  print(i, c.prob(i))

'''
返回值
(130, [(0.0, 'male'), (1.0, 'female')])
(135, [(0.0, 'male'), (1.0, 'female')])
(140, [(0.5, 'male'), (0.5, 'female')])
(145, [(0.0, 'male'), (1.0, 'female')])
(150, [(0.0, 'male'), (1.0, 'female')])
(155, [(0.14035087719298245, 'male'), (0.85964912280701755, 'female')])
(160, [(0.37974683544303806, 'male'), (0.62025316455696211, 'female')])
(165, [(0.26265389876880985, 'male'), (0.73734610123119015, 'female')])
(170, [(0.456418383518225, 'male'), (0.54358161648177494, 'female')])
(175, [(0.77419354838709675, 'male'), (0.22580645161290325, 'female')])
(180, [(0.55045871559633031, 'male'), (0.44954128440366975, 'female')])
(185, [(1.0, 'male'), (0.0, 'female')])
(190, [(1.0, 'male'), (0.0, 'female')])
(195, [(1.0, 'male'), (0.0, 'female')])
(200, [(1.0, 'male'), (0.0, 'female')])
(205, [(0.5, 'male'), (0.5, 'female')])
(210, [(0.5, 'male'), (0.5, 'female')])
(215, [(0.5, 'male'), (0.5, 'female')])
'''