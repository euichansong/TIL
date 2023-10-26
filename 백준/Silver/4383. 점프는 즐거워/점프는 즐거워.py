while True:
    try:
        numlist = list(map(int, input().split()))
        n = numlist[0]
        numlist = numlist[1:]
        jolly = [0] * (n-1)
        checklist = [i for i in range(1, n)]
        for i in range(len(numlist)-1):
            jolly[i] = (abs(numlist[i] - numlist[i+1]))
        cnt = 0
        jolly.sort()
        for i in range(len(jolly)):
            if jolly[i] == checklist[i]:
                cnt += 1
        if cnt == n-1:
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break