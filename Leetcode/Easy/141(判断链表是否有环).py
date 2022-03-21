#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/21 3:12 下午
# @Author :  Allen
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # 定义快、慢指针
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 定义一个标记，如果再次遇到表示有环
        while head:
            if head.val == 'qwerdftp':
                return True
            else:
                head.val = 'qwerdftp'
            head = head.next
        return False
