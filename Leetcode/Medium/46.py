#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/20 19:52
# @Author :  Allen
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        for i in itertools.permutations(nums):
            print(i)


s = Solution()
s.permute([1, 2, 3])



