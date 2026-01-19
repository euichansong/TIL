"""
0.3 초 (하단 참고)	512 MB

길이 100,000 까지
명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.


import sys
input = sys.stdin.readline

string = list(input().rstrip()) + [" "]
m = int(input())
cursor = string.index(' ')

for _ in range(m):
    # n이 변함
    n = len(string)-1
    # print(n)
    order = input().rstrip().split(' ')
    if order[0] == 'L':
        if cursor != 0:
            string[cursor], string[cursor-1] = string[cursor-1], string[cursor]
            cursor -= 1
    if order[0] == 'D':
        if cursor != n:
            string[cursor], string[cursor+1] = string[cursor+1], string[cursor]
            cursor += 1
    if order[0] == 'B':
        if cursor != 0:
            del string[cursor-1]
            cursor -= 1
    if order[0] == 'P':
        add_word = order[1]
        # 첫번째 인자 위치에 2번째 인자 삽입
        string.insert(cursor, add_word)
        cursor += 1
    # print(string)

for i in string:
    if i != " ":
        print(i, end="")
시간초과
>> 추가 삭제 o1 되는건 pop append 말곤 없나?
>> 스택으로 해보자
"""
import sys
input = sys.stdin.readline
from collections import deque

string = list(input().rstrip())
m = int(input())
string = deque(string)
cursor_right = deque()

for _ in range(m):
    order = input().rstrip().split(' ')
    if order[0] == 'L':
        if string:
            now = string.pop()
            cursor_right.append(now)
    if order[0] == 'D':
        if cursor_right:
            now = cursor_right.pop()
            string.append(now)
    if order[0] == 'B':
        if string:
            now = string.pop()
    if order[0] == 'P':
        add_word = order[1]
        string.append(add_word)
# print(string, cursor_right)

print("".join(string) + "".join(reversed(cursor_right)))