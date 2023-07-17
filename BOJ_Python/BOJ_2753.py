a = int(input())
if a % 100 == 0:
    print('0')
elif a % 4 == 0:
    print('1')
elif a % 400 == 0:
    print('1')
elif:
    print('0')
year = int(input())

if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')
