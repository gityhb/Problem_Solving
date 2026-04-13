def solution(bandage, health, attacks):
    answer = health #현재 체력은 20
    count = 0 #연속성공 카운트
    time = 0 #시간 카운트
    i = len(attacks)-1
    
    attacks.sort(reverse=True)
    
    while(i>=0):
        time += 1
        if attacks[i][0] == time:
            answer -= attacks[i][1]
            count = 0
            attacks.pop()
            i -= 1
            if answer <= 0:
                return -1
        else:
            count += 1
            if count == bandage[0]:
                answer = answer+bandage[1] + bandage[2]
                if answer > health:
                    answer = health
                count = 0
            else:
                answer = answer+bandage[1]
                if answer > health:
                    answer = health
                
    return answer