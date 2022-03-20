#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/20 23:10
# @Author :  Allen
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]