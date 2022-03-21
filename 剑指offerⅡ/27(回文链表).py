#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/21 3:04 下午
# @Author :  Allen
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head  # 为了在遍历完不破坏链表 head 指针，需要添加一个指针 cur
        while cur:
            stack.append(cur.val)
            cur = cur.next
        return stack == stack[::-1]