# 백준 1181번 - 단어 정렬
# https://www.acmicpc.net/problem/1181
import sys

n = int(sys.stdin.readline())

word = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    if word.count(temp) == 0:
        word.append(temp)
        
word.sort()
word.sort(key=lambda x:len(x))

for i in word:
    print(i)