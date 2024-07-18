import sys
dict = {}
total = 0
while True:
    # strip 안걸면 안끝남
    word = sys.stdin.readline().strip()
    # 빈칸 줄때까지
    if word == '':
        break
    # 딕셔너리에 없으면 1로 value 추가 총 갯수 추가
    if word not in dict:
        dict.setdefault(word, 1)
        total += 1
    else:
        dict[word] += 1
        total += 1
# value 기준로 알파벳순?
dict = sorted(dict.items(),key=lambda x:x[0])
print(dict)

for k,v in dict:
    v = float(v / total * 100)
    # 소수점 4자리까지
    # a = 0.55555
    # print(f"{a:0.4f}")
    # print(k, f"{v:.4f}")
    print(k, round(v,4))