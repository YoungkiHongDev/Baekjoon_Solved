# 백준 4344번 - 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
import sys
c = int(sys.stdin.readline())

for i in range(c):
    n = list(map(int, sys.stdin.readline().split()))
    nsum = 0
    for y in range(1, n[0]+1):
        nsum += n[y]
        
    avg = nsum/n[0]
    cnt = 0
    
    for z in range(1, n[0]+1):
        if avg<n[z]:
            cnt += 1

    print('{:.3f}%'.format(round(cnt/n[0]*100, 3)))
        
