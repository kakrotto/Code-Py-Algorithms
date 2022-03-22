#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/22 10:14
# @Author :  Allen

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class DuListNode:
    """双链表"""
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


#  [1, 2, 3] 1->2->3->nil


def create_linked_list(nums):
    """
    用 list 创建一个单链表
    :param nums: [1, 2, 3]
    :return: head
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


def linked_to_list(head):
    """
    单链表各 val 放入 list
    :param head: 1->2->3->None
    :return: [1, 2, 3]
    """
    res = []
    curnode = head
    while curnode:
        res.append(curnode.val)
        curnode = curnode.next
    return res


def print_linked_list(head):
    """
    打印一个单链表
    :param head:
    """
    cur = head
    while cur:
        print(f"{cur.val}->", end="")
        cur = cur.next
    print("nil")


def format_linked_list(head):
    """
    格式化一个单链表
    :param head:
    :return: 1->2->3->nil
    """
    s = ""
    cur = head
    while cur:
        s += f"{cur.val}->"
        cur = cur.next
    s += "nil"
    return s


if __name__ == '__main__':
    nums = [2, 1, 3]
    listNode = create_linked_list(nums)
    print_linked_list(listNode)
