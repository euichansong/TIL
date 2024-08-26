# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
후위순회 가장왼쪽자식부터 왼쪽 오른쪽 부모 순서로
재귀로 풀어야 할듯?
"""


class Solution:
    # self. 만드는건 gpt의 힘을 빌렸습니다
    # 맨 뒤에 append 하면 후위순회, 중간이면 중위순회, 맨 앞이면 전위순회
    def order(self, root, answer):
        if root:
            self.order(root.left, answer)
            self.order(root.right, answer)
            answer.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        answer = []
        self.order(root, answer)
        return answer

# 테스트 코드
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
result = sol.postorderTraversal(root)
print(result)