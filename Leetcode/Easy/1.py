#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/18 23:07
# @Author :  Allen
# 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], idx]
            d[num] = idx


def test():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    pass
