#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/20 15:59
# @Author :  Allen
# 拿硬币

import math
from typing import List


class Solution1:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        for c in coins:
            count += math.ceil(c / 2)
        return count


class Solution2:
    def minCount(self, coins: List[int]) -> int:
        return sum([(x + 1) // 2 for x in coins])


class Solution3:
    def minCount(self, coins: List[int]) -> int:
        return sum((x + 1) >> 1 for x in coins)


def test():
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution2()
    assert s1.minCount([9]) == 5
    assert s2.minCount([9]) == 5
    assert s3.minCount([9]) == 5
