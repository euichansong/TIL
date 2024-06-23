def solution(array, commands):
    answer = []
    for q in range(len(commands)):
        i,j,k = commands[q]
        print(i,j,k)
        arr = []
        for w in range(i-1,j):
            arr.append(array[w])
        arr.sort()
        answer.append(arr[k-1])

    return answer