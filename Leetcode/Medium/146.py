#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/16 5:15 下午
# @Author :  Allen
# LRU 缓存
# 主要用到了字典以及循环双端链表


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            value = self.od[key]
            self.od.move_to_end(key)
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)
        self.od.move_to_end(key)


def test():
    lru = LRUCache(2)
    lru.put(1, 1)
    assert dict(lru.od.items()) == {1: 1}
    lru.put(2, 2)
    assert dict(lru.od.items()) == {1: 1, 2: 2}
    assert lru.get(1) == 1
    assert dict(lru.od.items()) == {2: 2, 1: 1}
    lru.put(3, 3)
    assert dict(lru.od.items()) == {1: 1, 3: 3}
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert dict(lru.od.items()) == {4: 4, 3: 3}
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    assert dict(lru.od.items()) == {1: 1}
    lru.put(2, 2)
    assert dict(lru.od.items()) == {1: 1, 2: 2}
    assert lru.get(1) == 1
    assert dict(lru.od.items()) == {2: 2, 1: 1}
    lru.put(3, 3)
    assert dict(lru.od.items()) == {1: 1, 3: 3}
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert dict(lru.od.items()) == {4: 4, 3: 3}
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)