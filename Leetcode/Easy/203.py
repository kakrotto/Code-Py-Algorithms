#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/21 2:55 下午
# @Author :  Allen

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        h = ListNode(next=head)
        cur = h
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return h.next

s = Solution()
head = s.removeElements(ListNode(1, ListNode(2, ListNode(1, ListNode(2)))), 2)
print(head.val, head.next.val)



