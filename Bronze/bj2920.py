# 백준 2920번 - 음계
# https://www.acmicpc.net/problem/2920
import sys
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]
num = list(map(int, sys.stdin.readline().split()))

if num == asc:
    print("ascending")
elif num == des:
    print("descending")
else:
    print("mixed")
