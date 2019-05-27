# -*- coding:utf-8 -*-
import functools
import time

__author__ = 'xiaoyao'
__date__ = '2019/5/25 10:21'


def time_dec(func):
    print("dec started")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


@time_dec
def add(a, b):
    time.sleep(3)
    return a + b


# if __name__ == "__main__":
#     add(1,2)
