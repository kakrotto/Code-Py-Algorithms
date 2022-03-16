#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/15 11:40 下午
# @Author :  Allen
# 按奇偶排序数组
# 给定一个非负整数数组 A，返回一个数组，在该数组中，A 的所有偶数元素之后跟着所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

# 提示：

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-array-by-parity

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
