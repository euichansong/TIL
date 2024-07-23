t = int(input())
for _ in range(t):
    n = int(input())
    sobi = []
    for i in range(n):
        school, drink = input().split()
        drink = int(drink)
        sobi.append([school,drink])
    sobi.sort(key=lambda x:x[1], reverse=True)
    print(sobi[0][0])