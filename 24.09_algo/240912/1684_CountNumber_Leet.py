# from typing import List
# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         a = list(allowed)
#         cnt = 0
#         for i in words:
#             answer = False
#             for j in a:
#                 if j not in list(i):
#                     answer = True
#                     break
#             if answer:
#                 cnt += 1
#             if i == allowed:
#                 cnt += 1
#         print(cnt)
#         return cnt
"""

"""
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = list(allowed)
        cnt = 0
        for i in words:
            for j in list(i):
                if j not in a:
                    cnt += 1
                    break
        answer = len(words) - cnt
        print(answer)
        return answer
s = Solution()
s.countConsistentStrings(
    allowed = "cad",
    words = ["b","acd","cc","ba","bac","bad","ac","d"]
)