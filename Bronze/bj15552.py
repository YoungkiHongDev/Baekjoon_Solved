# 백준 15552번 - 빠른 A+B
# https://www.acmicpc.net/problem/15552
import sys
case = int(sys.stdin.readline())

for i in range(0, case):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
