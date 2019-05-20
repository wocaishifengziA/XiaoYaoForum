# -*- coding:utf-8 -*-
__author__ = 'xiaoyao'
__date__ = '2019/5/20 23:30'

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='deng')
redis.set('name', 'Bob')
print(redis.get('name'))