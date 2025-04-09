"""
48분간 진행 2880
"""
n = int(input())
records = []

for _ in range(n):
    team_num, ti = input().split()
    mi, sec = ti.split(":")
    goal_time = int(mi) * 60 + int(sec)
    records.append((int(team_num), goal_time))
records.append((0, 48 * 60))

one = 0
two = 0
score_one = 0
score_two = 0

for i in range(n):
    team_num, time = records[i]
    next_time = records[i + 1][1]

    if team_num == 1:
        score_one += 1
    else:
        score_two += 1

    if score_one > score_two:
        one += next_time - time

    elif score_two > score_one:
        two += next_time - time

one_min = one // 60
one_sec = one % 60
two_min = two // 60
two_sec = two % 60

print(f"{one_min:02}:{one_sec:02}")
print(f"{two_min:02}:{two_sec:02}")




    