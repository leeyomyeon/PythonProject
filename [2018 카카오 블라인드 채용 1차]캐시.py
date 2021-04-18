def solution(cacheSize, cities):
    answer = 0
    # 동일한 문자로 처리
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    if cacheSize == 0:
        return len(cities) * 5

    cache = []

    # LRU = 가장 오랫동안 참조되지 않은 페이지를 교체
    for str in cities:
        if not str in cache:
            if len(cache) < cacheSize:
                cache.append(str)
                answer += 5
            else:
                cache.pop(0)
                cache.append(str)
                answer += 5
        else:
            cache.pop(cache.index(str))
            cache.append(str)
            answer += 1

    return answer


cacheSizes = [3, 3, 2, 5, 2, 0]
city = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
        ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
        ["Jeju", "Pangyo", "NewYork", "newyork"],
        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]

for i in range(len(cacheSizes)):
    print(solution(cacheSizes[i], city[i]))