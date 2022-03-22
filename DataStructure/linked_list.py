#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/22 10:14
# @Author :  Allen

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class DuListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


#  [1, 2, 3] 1->2->3->nil


def gen_list(nums):
    """
    创建一个单链表
    :param nums:
    :return:
    """
    if not nums:
        return None
    head = ListNode(nums[0])
    pre = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        pre.next = node
        pre = node
    return head


def print_list(head):
    """
    打印一个单链表
    :param head:
    :return:
    """
    cur = head
    while cur:
        print(f"{cur.val}->", end="")
        cur = cur.next
    print("nil")


if __name__ == '__main__':
    nums = [2, 1, 3]
    listNode = gen_list(nums)
    print_list(listNode)
