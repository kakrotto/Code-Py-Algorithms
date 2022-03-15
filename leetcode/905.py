#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/15 11:40 下午
# @Author :  Allen
# 按奇偶排序数组
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        beg, end = 0, len(nums)-1
        while beg <= end:
            while nums[beg] % 2 == 0 and beg < end:
                beg += 1
            while nums[end] % 2 != 0 and beg < end:
                end -= 1
            if beg >= end:
                break
            nums[beg], nums[end] = nums[end], nums[beg]
        return nums


if __name__ == '__main__':
    l = [3, 1, 2, 4]
    s = Solution()
    print(s.sortArrayByParity(l))
