# https://data-analysis-expertise.tistory.com/107
def solution(cacheSize, cities):
    
    cache = []
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    else:
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.remove(city)
                cache.append(city) # 최근에 사용할수록 리스트 마지막에 더해짐
                answer += 1
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)  # 가장 덜 사용될수록 리스트 첫번째에 오게 됨
                cache.append(city)
                answer += 5
            
    return answer
