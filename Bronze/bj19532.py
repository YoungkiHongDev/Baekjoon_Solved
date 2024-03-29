# 백준 19532 - 수학은 비대면강의입니다
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        # 연립방정식 조건에 맞는 답을 찾으면 출력한다.
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(x, y)
            break
