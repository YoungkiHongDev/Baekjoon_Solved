# 백준 15736 - 청기 백기
# 정수론
# https://www.acmicpc.net/problem/15736

'''
최종적으로 뒤집힌 깃발은 선수 번호를 제곱한 숫자의 깃발들이다.
1,2,3,4,... 선수 번호를 제곱한 1,4,9,16,.. 이런 깃발들만 개수를 세서 출력
'''

n = int(input())
answer = 0

for turn in range(1, n+1):
    if  (turn * turn) > n:
        break
    answer += 1

print(answer)
