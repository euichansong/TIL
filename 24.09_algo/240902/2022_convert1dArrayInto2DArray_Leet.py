from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        print(m,n,original)
        ori = len(original)
        answer = []
        if m*n == ori:
            cnt = 0
            for i in range(m):
                row = []
                for j in range(n):
                    row.append(original[cnt])
                    cnt += 1
                answer.append(row)
        return answer