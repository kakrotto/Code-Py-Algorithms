#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/19 17:39
# @Author :  Allen
# 翻转链表
from DataStructure.linked_list import create_linked_list, format_linked_list, linked_to_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None  # 前一个节点
        cur = head  # 当前节点
        while cur:
            nextnode = cur.next  # 保存下一个节点的指针
            cur.next = pre  # 当前节点指向上一个节点
            pre = cur  # 移动前一个节点到当前节点
            cur = nextnode  # 移动当前节点到下一个节点
        return pre   # 注意返回的是 pre


def test():
    nums = [1, 2, 3, 4]
    s = Solution()
    # 创建链表方法一
    head = create_linked_list(nums)
    print()  # 这行无意义，请忽略
    print(f"链表翻转前：{format_linked_list(head)}")
    head = s.reverseList(head)
    print(f"链表翻转后：{format_linked_list(head)}")
    assert linked_to_list(head) == [4, 3, 2, 1]
    # 创建链表方法二
    ll = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    head = s.reverseList(ll)
    assert linked_to_list(head) == [1, 2, 3, 4]
