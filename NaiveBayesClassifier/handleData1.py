#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1. Getting the Data Ready
数据处理: 
  It contains 100 random person data, male and female, 
  with body sizes, weights and gender tags

原始数据说明:
  persons = [
    # firstname,   secondname,  height,   weight,  gender
    [ 'Randy',     'Carter',    '184',    '73',   'male'],
    [ 'Stephanie', 'Smith',     '149',    '52',   'female'],
    ...
  ]
'''
# 引入模块: Numpy是Python的一个科学计算的库，提供了矩阵运算的功能
import numpy as np

genders = ['male', 'female']
persons = []
firstnames = {}
heights = {}

def onData () :
  # 原始数据获取
  with open("data/classifer.txt") as fh:
    for line in fh:
      # strip() 移除字符串头尾指定的字符, eg:('0')
      persons.append(line.strip().split())
  
  # 获取到以gender为区分 条件 分类其他条件
  for gender in genders :
    # 初始化为[]
    # heights[gender] = []
    # firstnames[gender] = []

    firstnames[gender] = [ x[0] for x in persons if x[4] == gender ]
    heights[gender] = [ x[2] for x in persons if x[4] == gender ]
    # np.array: 创建数组, 指定数据 dtype
    heights[gender] = np.array(heights[gender], np.int)

    # for itemPerson in persons : 
    #   if (itemPerson[4] == gender) :
    #     # 身高
    #     heights[gender].append(intp(itemPerson[2]))
    #     # 名字
    #     firstnames[gender].append(itemPerson[0])

  # print(firstnames)
  # print(heights)

  return dict({
    'firstnames': firstnames,
    'heights': heights,
    'persons': persons,
    'genders': genders
  })

'''
返回数据
firstnames
{
  'male': ['Randy', 'Jessie', 'David', 'Stephen', 'Jerry', 'Billy', 'Earl', 'Todd', 'Martin', 'Kenneth', 'Frank', 'Wayne', 'Henry', 'Alan', 'Paul', 'Jack', 'Bobby', 'Keith', 'Carl', 'Brian', 'Anthony', 'Peter', 'Willie', 'Albert', 'Benjamin', 'Steve', 'Gerald', 'Craig', 'Douglas', 'Joshua', 'Raymond', 'Eric', 'Shawn', 'Justin', 'Arthur', 'Adam', 'Fred', 'George', 'Jessie', 'William', 'Andrew', 'Richard', 'Harry', 'Chris', 'Edward', 'Donald', 'Thomas', 'Johnny', 'Matthew', 'Louis'], 
  'female': ['Stephanie', 'Cynthia', 'Katherine', 'Elizabeth', 'Carol', 'Christina', 'Beverly', 'Sharon', 'Denise', 'Rebecca', 'Alice', 'Ashley', 'Sarah', 'Betty', 'Kimberly', 'Julie', 'Donna', 'Marie', 'Paula', 'Irene', 'Barbara', 'Evelyn', 'Kelly', 'Jessie', 'Laura', 'Marilyn', 'Jessie', 'Diana', 'Jessie', 'Sandra', 'Ann', 'Helen', 'Nicole', 'Lisa', 'Julia', 'Louise', 'Anna', 'Brenda', 'Deborah', 'Angela', 'Sara', 'Maria', 'Debra', 'Lillian', 'Theresa', 'Phyllis', 'Jessie', 'Emily', 'Doris', 'Janice']
}
heights
{
	'male': ['184', '175', '187', '192', '204', '180', '184', '174', '177', '200', '193', '189', '188', '187', '187', '190', '180', '155', '201', '171', '163', '191', '175', '170', '178', '191', '176', '168', '169', '173', '180', '212', '189', '174', '167', '193', '164', '171', '165', '198', '185', '175', '195', '164', '187', '192', '175', '190', '164', '161'],
	'female': ['149', '174', '183', '138', '145', '161', '179', '162', '148', '196', '163', '159', '150', '170', '169', '167', '168', '170', '167', '152', '155', '151', '166', '165', '158', '152', '159', '163', '174', '131', '154', '159', '159', '177', '180', '164', '163', '161', '183', '170', '167', '166', '180', '161', '170', '172', '168', '156', '167', '167']
}
'''
