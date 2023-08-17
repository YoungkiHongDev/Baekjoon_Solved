# 백준 2503 - 숫자야구
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/2503

count = int(input())
hint = [list(map(int, input().split())) for _ in range(count)]
result = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            
            if a == b or a == c or b == c:
                continue

            num = str(a) + str(b) + str(c)

            clear = 0
            for arr in hint:
                number, strike, ball = arr
                number = str(number)
                
                strike_cnt = sum(1 for i in range(3) if number[i] == num[i])
                ball_cnt = sum(1 for i in range(3) if number[i] in str(num) and number[i] != num[i])

                if strike_cnt == strike and ball_cnt == ball:
                    clear += 1

            if clear == count:
                result += 1

print(result)
