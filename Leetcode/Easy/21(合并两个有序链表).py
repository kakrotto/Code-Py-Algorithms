#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/22 11:50
# @Author :  Allen
from typing import Optional

from DataStructure.linked_list import create_linked_list, format_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0)
        cur = pre
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return pre.next


def test():
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    print()
    print(f"创建的链表为：{format_linked_list(l1)}  {format_linked_list(l2)}")
    s = Solution()
    head = s.mergeTwoLists(l1, l2)
    print(f"合并后： {format_linked_list(head)}")
    assert format_linked_list(head) == "1->1->2->3->4->4->nil"
