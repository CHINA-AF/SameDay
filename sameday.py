#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作者：龙.吟
def days():
    bl = [1, 3, 5, 7, 8, 10, 12]
    sl = [4, 6, 9, 11]
    for y in range(0, 10000):
        for m in range(1, 13):
            if m in bl:
                for d in range(1, 32):
                    yield [y, m, d]
            elif m in sl:
                for d in range(1, 31):
                    yield [y, m, d]
            else:
                if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                    for d in range(1, 30):
                        yield [y, m, d]
                else:
                    for d in range(1, 29):
                        yield [y, m, d]


def show():
    count = 0
    for d in days():
        day = "{}{:0>2}{:0>2}".format(d[0], d[1], d[2])
        if day == day[::-1]:
            count += 1
            print(day)
    print('运行完成！共有{}个回文日期'.format(count))


if __name__ == '__main__':
    show()
