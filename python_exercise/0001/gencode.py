# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
__author__ = 'zengxianyu'

import random


def getrandomstr(num, strlen):
    strSet = set()
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    while strSet.__len__() < num:
        strSet.add(''.join(random.sample(chars, strlen)))

    with open("Active_code.txt", 'w') as f:
        for code in strSet:
            f.write(code + '\n')


if __name__ == '__main__':
    getrandomstr(200, 10)
