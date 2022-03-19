#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/19 17:39
# @Author :  Allen
# 翻转链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prenode = None
        curnode = head
        while curnode:
            nextnode = curnode.next
            curnode.next = prenode
            prenode = curnode
            curnode = nextnode
        return prenode   # 注意返回的是 prenode

    def to_list(self, head):
        res = []
        curnode = head
        while curnode:
            res.append(curnode.val)
            curnode = curnode.next
        return res


def test():
    s = Solution()
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head = s.reverseList(ll)
    assert s.to_list(head) == [4, 3, 2, 1]

    ll = ListNode(1)
    head = s.reverseList(ll)
    assert s.to_list(head) == [1]
