# 백준 11720번 - 숫자의 합
# https://www.acmicpc.net/problem/11720
import sys

n = int(sys.stdin.readline())
num = sys.stdin.readline()

sum = 0
for i in num:
    if i != '\n':
        sum += int(i)

print(sum)
