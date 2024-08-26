"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def order(self, root, answer):
        if root:
            # 후위 순회니까 돌릴꺼 다 돌리고 마지막에 append
            for c in root.children:
                self.order(c, answer)
            answer.append(root.val)

    def postorder(self, root: 'Node') -> list[int]:
        answer = []
        self.order(root, answer)
        return answer



