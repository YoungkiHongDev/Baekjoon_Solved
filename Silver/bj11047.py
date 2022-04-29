# 백준 11047번 - 동전 0
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

nl = []
for i in range(n):
    nl.append(int(input()))
    
nl.reverse()

cnt = 0
for i in nl:
    cnt += k//i
    k = k%i

print(cnt)