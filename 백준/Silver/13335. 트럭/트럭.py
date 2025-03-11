from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = deque(map(int, input().split()))

time = 0
bridge = deque([0] * w) 
bridge_weight = 0 

while truck or bridge_weight > 0:
    time += 1

    pt = bridge.pop()
    bridge_weight -= pt 

    if truck and bridge_weight + truck[0] <= l:
        new_truck = truck.popleft()
        bridge.appendleft(new_truck)
        bridge_weight += new_truck 
    else:
        bridge.appendleft(0)  

print(time)


# """ 원래 코드
# 1 초	512 MB
# n 트럭갯수
# w 다리에 올라갈수 있는 트럭갯수
# l 무게 최대
# 트럭 순서 못바꾼다

# 트럭 올린다
# 다음트럭 본다
# 다리 트럭 전진 다리에 올릴수 있고, 무게 올릴수 있으면 올린다
# 못올린다 > 다리길이 -1 만큼 시간에 더해
# 끝까지 가면 내보낸다

# """
# from collections import deque
# import sys
# input = sys.stdin.readline

# n,w,l = map(int, input().split())
# truck = list(map(int, input().split()))
# truck = deque(truck)
# time = 0
# bridge = deque([0]*w)
# bridge_t = 0
# while truck or sum(bridge) > 0:
#     time += 1
#     pt = bridge.pop()
#     if pt != 0:
#         bridge_t -= 1
#     # 다리 입장
#     if w == 1:
#         time = len(truck)
#         break
#     else:
#         # 길이 1아닌 경우
#         # 다리에 들어갈수 있고 최대 댓수 초과하지 않을때
#         if truck and sum(bridge) + truck[0] <= l and bridge_t < w:
#             np = truck.popleft()
#             bridge.appendleft(np)
#             bridge_t += 1
#         else:
#             bridge.appendleft(0)

# print(time)