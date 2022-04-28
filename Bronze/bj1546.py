# 백준 1546번 - 평균
import sys

n = int(sys.stdin.readline())
nl = sys.stdin.readline().split()
nl = list(map(int, nl))
score = []

for i in range(n):
    score.append(nl[i]/max(nl)*100)

print(sum(score)/len(score))

