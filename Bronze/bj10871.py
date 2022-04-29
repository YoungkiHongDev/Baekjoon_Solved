# 백준 10871번 - X보다 작은 수
# https://www.acmicpc.net/problem/10871
import sys

n, x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
a = list(map(int, a))

result = [i for i in a if i < x]
print(*result, sep=' ')
