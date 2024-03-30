from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # 小于0则不是回文数
            return False
