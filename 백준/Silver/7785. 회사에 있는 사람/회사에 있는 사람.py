n = int(input())
inoutdict = {}
remaindict = {}
for i in range(n):
    name, inout = input().split()
    inoutdict[name] = inout
# print(inoutdict)
for k, v in inoutdict.items():
    if v == 'enter':
        remaindict[k] = 1
# print(remaindict)
sortdict = sorted(remaindict.keys(), reverse = True)
# print(sortdict)
for i in sortdict:
    print(i)