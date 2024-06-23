"""
딕셔너리 써서 숫자 매기고 하면 될거 같은데?
    아닌듯
도시 갯수 어떻게 구함?
항공권도 다 써야 하네;
"""

def solution(tickets):
    dict = {}
    for start, end in tickets:
        dict.setdefault(start, [])
        # 방문 확인용 0 추가
        dict[start].append([end,0])

    for key in dict.keys():
        dict[key].sort()

    def DFS(start):
        stack = []
        # 경로
        path = []
        # 스택에 시작점 추가
        stack.append(start)
        while True:
            aa = len(path)
            bb = len(tickets)
            if len(path) == len(tickets) + 1 :
                break
            # 경로에 시작점 추가
            path.append(start)
            # 딕셔너리에서 갈 수 있는 공항
            for next in dict[start]:
                # 방문 처리 있어야 된다
                if (next[0] != path[-1]) and next[1] == 0:
                    a = next[0]
                    # 마지막 경로이기 때문에 추가하고 끝낸다
                    if len(path) == len(tickets):
                        path.append(a)
                        break
                    # 이 부분 처리 어떻게 할지 고민 해야 한다 키 값으로 설정이 안되어 있기 때문에
                    if a in dict:
                        stack.append(next[0])
                        next[1] = 1
                        start = next[0]
                        break
            else:
                if stack:
                    start = stack.pop()
                else:
                    break
        return path
    answer = DFS('ICN')
    print(answer)
    return answer
#
# 예시 1 [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#
"""
예시1 [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
정답  ["ICN", "JFK", "HND", "IAD"]
예시2 [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
정답 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
테케 [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
정답 ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
"""
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
solution(tickets)