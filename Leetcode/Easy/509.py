#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/16 6:09 下午
# @Author :  Allen
# 斐波那契数

class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


class Solution2:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c


if __name__ == '__main__':
    pass
