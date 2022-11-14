# 프로그래머스 레벨3 단속카메라 그리디

def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    camera = -30001

    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1

    return answer

if __name__ == "__main__":
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	
    print(solution(routes))