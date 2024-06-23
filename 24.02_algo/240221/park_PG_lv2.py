import math
def solution(fees, records):
    # print(records)
    dict = {}
    dict_time = {}
    for i in records:
        time, num, inout = i.split()
        if inout == "IN":
            dict[num] = [time, "IN"]
        elif inout == "OUT":
            try :
                dict_time[num] += time_cal(time, dict[num][0])
                dict[num][1] = "OUT"
            except:
                dict_time[num] = time_cal(time, dict[num][0])
                dict[num][1] = "OUT"
    for k,v in dict.items():

        if v[1] == "IN":
            try:
                dict_time[k] += time_cal("23:59",v[0])
            except:
                dict_time[k] = time_cal("23:59", v[0])
    print(dict_time)
    answer_sort = []
    answer = []
    for k,v in dict_time.items():
        if v >= fees[0]:
            fee = fees[1] + (math.ceil((v-fees[0]) / fees[2]) * fees[3])
        else:
            fee = fees[1]
        answer_sort.append([k,fee])
    answer_sort.sort()
    for i in answer_sort:
        answer.append(i[1])
    return answer

def time_cal(big, small):
    bigh, bigm = big.split(":")
    smallh, smallm = small.split(":")
    totalbig = int(bigh)*60 + int(bigm)
    totalsmall = int(smallh)*60 + int(smallm)
    total = totalbig - totalsmall
    return total


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees,records))