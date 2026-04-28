"""
30만?
공식 있을거 같은데
최소 레벨? > 이진탐색 그리디? 


퍼즐 틀리면 이전 퍼즐 다시 풀고 와야 한다 
다시 풀때는 난이도 상관없이 안틀린다관없이 안틀린다
"""
def puz(dif,time,limit,level):
    clear = 0
    for i in range(len(dif)):
        if dif[i] <= level:
            clear += time[i]
        elif dif[i] > level:
            clear += (dif[i] - level)*(time[i-1]+time[i]) + time[i]
        if clear > limit:
            return False
    return True

def solution(diffs, times, limit):
    l = 1
    r = max(diffs)
    while l <= r:
        mid = (l+r) // 2
        if puz(diffs,times,limit,mid):
            r = mid-1
        else:
            l= mid+1
    answer = l
    return answer