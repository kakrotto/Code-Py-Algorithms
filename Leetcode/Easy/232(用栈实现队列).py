#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/23 4:13 下午
# @Author :  Allen

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # stack1 里的数据是先进后出的, 所以在取值的时候需要把 stack1 里的数据放到 stack2里，
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        value = self.stack2.pop()
        # 再恢复数据序列，
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return value

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 返回数据再添加数据到 top
        value = self.stack2.pop()
        self.stack2.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return value

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
def test():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    assert obj.empty() == False
    assert obj.pop() == 1
    assert obj.peek() == 2
    assert obj.empty() == False
    assert obj.pop() == 2
    assert obj.empty() == False
    assert obj.pop() == 3
    assert obj.empty() == True


if __name__ == '__main__':
    pass
