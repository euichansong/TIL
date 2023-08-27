# 신호등 갯수, 도로의 길이                                                                 
n, L = map(int, input().split())                                                 
# 인덱스 값 맞추기 위해 앞에 0 라인, 뒤에 L 길이 추가                                               
arr = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)] + [[L,0,0]]
# 첫 신호등 까지                                                                       
time = arr[1][0]                                                                 
# 주어진 신호등 , red,green 시간                                                         
for i in range(1,n+1):                                                           
    red_cnt = arr[i][1]                                                          
    gr_cnt = arr[i][2]                                                           
    # 다음 신호등 까지 거리                                                               
    passroad = arr[i+1][0] - arr[i][0]                                           
    # 신호등이 빨간색일때                                                                 
    while time % (red_cnt+gr_cnt) < red_cnt:                                     
        # 시간 증가                                                                  
        time += 1                                                                
    # 신호등이 초록색이면 출발                                                              
    while red_cnt <= time % (red_cnt+gr_cnt):                                    
        time += passroad                                                         
        break                                                                    
print(time)                                                                      