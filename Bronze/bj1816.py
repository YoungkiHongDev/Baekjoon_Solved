# 백준 1816 - 암호키
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/1816

n = int(input())
target = 1000000
result = "YES"

for _ in range(n):
    num = int(input())
    
    for i in range(2, target+1):
        if num % i == 0:
            result = "NO"
            break
        
    print(result)
    result = "YES"
