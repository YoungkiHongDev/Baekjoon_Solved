# 백준 2675번 - 문자열 반복
# https://www.acmicpc.net/problem/2675
import sys

t = int(sys.stdin.readline())
p = ''

for x in range(t):
    si, ss = sys.stdin.readline().split()
    ss = list(ss)
    
    for y in ss:
        p = p+(y*int(si))
        
    print(p)
    p = ''
