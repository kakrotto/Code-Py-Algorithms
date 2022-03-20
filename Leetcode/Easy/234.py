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


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while head:
            if not head.val == stack.pop():
                return False
            head = head.next
        return True


class Solution3:
    """
    内存O(1)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        n1 = head
        n2 = head
        while n2.next and n2.next.next:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next
        n1.next = None

        while n2:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        n3 = n1
        n2 = head
        res = True
        while n1 and n2:
            if n1.val != n2.val:
                res = False
                break
            n1 = n1.next
            n2 = n2.next
        n1 = n3.next
        n3.next = None
        while n1:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2
        return res

s = Solution3()
print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
