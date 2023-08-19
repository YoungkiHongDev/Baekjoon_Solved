# 백준 2503 - 숫자야구
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/2503

'''
조건
1. 서로 다른 세자리수
2. 같은자리, 같은숫자라면 스트라이크
3. 다른자리, 같은숫자라면 볼

주어진 힌트를 모두 통과하는 세자리수 숫자는 정답일 가능성이 생긴다.
그러한 세자리수 숫자를 모두 골라내서 총 개수를 출력시킨다.
'''

count = int(input())
hint = [list(map(int, input().split())) for _ in range(count)]
result = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            
            # 조건 1번에 맞지 않아 넘어간다.
            if a == b or a == c or b == c:
                continue

            # 숫자 세자리를 문자열로 합친다.
            num = str(a) + str(b) + str(c)

            clear = 0 # 힌트를 몇개나 만족시키나 카운트하는 변수
            for arr in hint:
                number, strike, ball = arr
                number = str(number) # 합친 세자리수와 비교하기 위해 똑같이 문자열로 만든다.

                # if 조건에 맞을때마다 sum에 더할 값 1씩 증가하여 스트라이크, 볼 카운트
                strike_cnt = sum(1 for i in range(3) if number[i] == num[i])
                ball_cnt = sum(1 for i in range(3) if number[i] in str(num) and number[i] != num[i])

                # 카운트한 스트라이크, 볼과 힌트의 스트라이크, 볼이 같으면 힌트 통과한걸로 카운트
                if strike_cnt == strike and ball_cnt == ball:
                    clear += 1

            # 힌트를 모두 통과했으면 정답 가능성이 있으므로 카운트
            if clear == count:
                result += 1

print(result)
