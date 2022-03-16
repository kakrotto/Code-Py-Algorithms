#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/16 1:21 下午
# @Author :  Allen
from typing import List

from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        d = defaultdict(int)
        for num in nums1:
            d[num] += 1
        for num in nums2:
            if d[num] > 0:
                result.append(num)
                d[num] -= 1
        return result


def test():
    s = Solution()
    assert s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
