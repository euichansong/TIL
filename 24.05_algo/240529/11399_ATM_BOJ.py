"""
피보나치?
"""
n = int(input())
peo = list(map(int, input().split()))
peo.sort()
time = 0
nu = 0
for i in peo:
    nu += i
    time += nu
print(time)