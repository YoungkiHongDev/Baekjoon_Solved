# 백준 1110번 - 더하기 사이클
# https://www.acmicpc.net/problem/1110
import sys

n = int(sys.stdin.readline())
n1, n2 = 0, 0
cnt = 0

if n >= 10:
    n = [int(i) for i in str(n)]
    n1 = n[0]
    n2 = n[1]
else:
    n1 = 0
    n2 = n

a = n1
b = n2

while True:
    s = a+b
    cnt += 1

    if s >= 10:
        sl = [int(i) for i in str(s)]
        a = b
        b = sl[1]
    else:
        a = b
        b = s

    if a == n1 and b == n2:
        print(cnt)
        break