#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/16 6:09 下午
# @Author :  Allen

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


s = Solution()
print(s.fib(3))

"0 + 1 + 1 + 2 + 3"