def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

flag = True
while flag:
    word = input()
    if int(word) == 0:
        flag = False
        break
    else:
        answerlist = []
        for i in range(len(word)):
            for j in range(len(word)+1):
                num = word[i:j]
                if num:
                    # 100000 보다 작은 소수
                    if len(num) <= 5 and prime(int(num)):
                        answerlist.append(int(num))
    print(str(max(answerlist)))


