#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/23 3:44 下午
# @Author :  Allen
# 考察 栈

class Solution1:
    def isValid(self, s: str) -> bool:
        while "{}" in s or "[]" in s or "()" in s:
            s = s.replace("{}", "").replace("()", "").replace("[]", "")
        return s == ""


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False

