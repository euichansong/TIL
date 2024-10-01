"""
aeiou
aaeeiioouu 조합 2개?

"""
from itertools import product
def solution(word):
    answer = 0
    aeiou = ['A','E','I','O','U']
    w = 'AEIOU'
    total = []
    for i in range(1,6):
        li = list(map(''.join, product(aeiou,repeat=i)))
        total+= li
    total.sort()
    answer = total.index(word) + 1
    return answer