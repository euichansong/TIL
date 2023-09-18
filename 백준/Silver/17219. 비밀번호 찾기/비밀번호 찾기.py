import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sitedict = {}
for i in range(n):
    site, password = input().split()
    sitedict[site] = password
# print(sitedict)
for i in range(m):
    wantsite = input().rstrip()
    print(sitedict[wantsite])