from collections import deque
def solution(people, limit):
    people.sort(reverse = True)
    people = deque(people)
    
    # print(people)
    answer = 0

    while people:
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                people.pop()
                people.popleft()
                answer += 1
                
            else:
                people.popleft()
                answer += 1
                
        else:
            people.pop()
            answer += 1
                
    return answer