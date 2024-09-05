from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 계속 시간초과나서 찾아봤더니 튜플 안에 튜플로만 바꿔주면 된다함;;;
        obstacle_set = set(map(tuple, obstacles))
        # 북 동 남 서
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # 현재 방향
        nd = 0
        sx, sy = 0, 0
        answer = 0
        for i in commands:
            Flag = False
            if i == -1:
                nd = (nd + 1) % 4
            elif i == -2:
                nd = (3 + nd) % 4
            else:
                # 북
                if nd == 0:
                    move = 0
                    while move < i:

                        move += 1
                        if (sx, sy + move) in obstacle_set:
                            sy = sy + move - 1
                            Flag = True
                            break
                    if Flag:
                        pass
                    else:
                        sy += move
                # 동
                elif nd == 1:
                    move = 0
                    while move < i:
                        move += 1
                        if (sx + move, sy) in obstacle_set:
                            sx = sx + move - 1
                            Flag = True
                            break
                    if Flag:
                        pass
                    else:
                        sx += move
                # 남
                elif nd == 2:
                    move = 0
                    while move < i:
                        move += 1
                        if (sx, sy - move) in obstacle_set:
                            sy = sy - move + 1
                            Flag = True
                            break
                    if Flag:
                        pass
                    else:
                        sy -= move
                # 서
                else:
                    move = 0
                    while move < i:
                        move += 1
                        if (sx - move, sy) in obstacle_set:
                            sx = sx - move + 1
                            Flag = True
                            break
                    if Flag:
                        pass
                    else:
                        sx -= move
                answer = max(answer, ((sx ** 2) + (sy ** 2)))
                print(answer)
        return answer



so = Solution()
so.robotSim(
    commands=[-2,5,9,-2,6],
    obstacles=[[-3,2],[-1,2],[-2,2],[-2,-3],[3,-5],[-4,-1],[4,-2],[-5,5],[-4,-2],[0,-1]]
)