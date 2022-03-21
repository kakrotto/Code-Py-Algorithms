#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/21 3:56 下午
# @Author :  Allen
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        def list_str_to_num(ll):
            ltr = ''
            for i in ll:
                ltr += str(i)
            return int(ltr)

        num1 = list_str_to_num(s1)
        num2 = list_str_to_num(s2)
        num_add = num1 + num2
        num_add_list = [int(i) for i in str(num_add)]
        num_add_list = num_add_list[::-1]
        head = ListNode()
        cur = head
        for i in num_add_list:
            if cur.next is None:
                cur.val = i
                cur.next = ListNode()
            else:
                cur = cur.next
        return head

s = Solution()

s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(9))), ListNode(5, ListNode(6, ListNode(4, ListNode(9)))))
