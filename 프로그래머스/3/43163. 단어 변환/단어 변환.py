"""
단어 나눠서 단어길이 -1 만큼 같은지 확인
"""
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    visited = [0] * len(words)
    ans = []
    def dfs(s_word,answer,visited):
        if s_word == target:
            ans.append(answer)
            return 
        for i in range(len(words)):
            cnt = 0
            for j in range(len(s_word)):
                if s_word[j] == words[i][j]:
                    cnt += 1
            if (cnt == len(s_word)-1) and visited[i] == 0:
                visited[i] = 1
                dfs(words[i],answer +1,visited)
                visited[i] = 0
    dfs(begin,answer,visited)
    answer = min(ans)
    return answer