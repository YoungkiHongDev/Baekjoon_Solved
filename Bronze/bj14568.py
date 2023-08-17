# 백준 14568 - 2017 연세대 프로그래밍 경시대회
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/14568

candy = int(input())
result = 0

for a in range(1, candy+1):
    for b in range(1, candy+1):
        for c in range(1, candy+1):
            if a+b+c == candy and a >= b+2 and c % 2 == 0:
                result = result + 1

print(result)
