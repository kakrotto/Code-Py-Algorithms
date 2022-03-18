#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/18 23:11
# @Author :  Allen
# 回文数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return [i for i in str(x)] == [i for i in reversed(str(x))]


def test():
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False


if __name__ == '__main__':
    pass
