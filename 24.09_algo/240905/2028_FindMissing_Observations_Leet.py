from typing import List
"""

"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 횟수가 영어로 number
        num = len(rolls) + n
        # 만들어야하는 총 합
        total = mean*num
        # 관측된 주사위수
        rol_sum = sum(rolls)
        # 주사위 총합
        dice_total = total - rol_sum
        # 현재 주사위 총합
        now = n
        # 주사위에 주입할 평균값
        inject = (dice_total - n) // n
        if inject > 5 or inject <0:
            return []
        # 주사위에 추가할 나머지
        extra = (dice_total-n) - inject*n
        # 찾을 주사위
        dice = [1+inject] * n

        # 6 넘어가면 실패
        if (sum(dice) + extra) > 6*n:
            return []
        # 넣을꺼 없으면 리턴
        if extra == 0:
            return dice

        flag = True
        idx = 0
        while flag:
            while dice[idx] <= 5:
                dice[idx] += 1
                extra -= 1
                if extra == 0:
                    flag = False
                    break
            idx += 1
        print(dice)
        return dice

so = Solution()
so.missingRolls(
rolls = [4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], mean = 4, n = 40
)