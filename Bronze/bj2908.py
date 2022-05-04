# 백준 2908번 - 상수
# https://www.acmicpc.net/problem/2908
import sys
a, b = map(int, sys.stdin.readline().split())

ra = [int(x) for x in str(a)]
rb = [int(x) for x in str(b)]

ra.reverse(), rb.reverse()

sa = str(ra[0])+str(ra[1])+str(ra[2])
sb = str(rb[0])+str(rb[1])+str(rb[2])

if int(sa) > int(sb):
    print(sa)
else:
    print(sb)
