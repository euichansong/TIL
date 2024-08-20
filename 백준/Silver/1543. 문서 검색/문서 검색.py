word = list(input())
find = list(input())
visited = [0] * len(word)
answer = 0
for i in range(len(word)):
    if visited[i] == 1:
        continue

    if word[i:i+len(find)] == find:
        for j in range(i,i+len(find)):
            visited[j] = 1
        # print(visited)
        answer += 1
print(answer)
# print(visited)