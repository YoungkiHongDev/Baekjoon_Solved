# 백준 2475번 - 검증수
# https://www.acmicpc.net/problem/2475
import sys
num = list(map(int, sys.stdin.readline().split()))
num = [ x*y for x, y in zip(num, num) ]
print(sum(num)%10)
