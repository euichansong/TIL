import sys
n = int(sys.stdin.readline())
wordlist = []
for _ in range(n):
    # 옆에 빈 공백 제거
    wordlist.append(sys.stdin.readline().rstrip())
# 중복 제거
word = list(set(wordlist))

# 길이로 정렬하고 길이가 같으면 알파벳 순으로 정렬
word.sort(key=lambda x : (len(x), x))


for i in word:
    print(i)