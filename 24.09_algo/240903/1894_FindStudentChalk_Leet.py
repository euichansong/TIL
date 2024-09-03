from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idx = 0
        gil = len(chalk)
        # 이거 안넣으면 시간초과
        total = sum(chalk)
        k = k % total
        flag = True
        while flag:
            idx = idx % gil
            k -= chalk[idx]
            if k < 0:
                flag = False
                break
            idx += 1
        return idx