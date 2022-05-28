import heapq
import math

def cal_time(fuel, power, distance, time):
    if fuel * power * fuel / 2 >= distance:
        # print("등속되기전에 끝", fuel, power, distance, time)
        for t in range(time, fuel+1):
            # print("t가 올라간다~~", t)
            if power * t * t / 2 >= distance:
                return t
    else:
        t = fuel
        n_power = power*fuel
        distance -= n_power * fuel / 2
        
        temp = math.ceil(distance / n_power)
        return t + temp

def solution(fuel, powers, distances):
    answer = 0
    heap = []
    for i in range(len(powers)):
        # 총 도착시간, 파워, 거리, 연료 수
        # 총 도착시간을 우선 순위로 두고 클수록 연료를 더 줌
        heapq.heappush(heap, [-cal_time(1, powers[i], distances[i], 1), powers[i], distances[i], 1])

    fuel -= len(powers)
    while fuel:
        t, p, d, f = heapq.heappop(heap)
        heapq.heappush(heap, [-cal_time(f+1, p,d, -t), p, d, f+1])
        fuel -= 1
    answer = -heap[0][0]
    return answer

solution(100,[100, 150],[1, 1000000])