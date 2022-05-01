# 백준 10809번 - 알파벳 찾기
# https://www.acmicpc.net/problem/10809
import sys

s = list(sys.stdin.readline())
abc = ['a', 'b', 'c', 'd', 'e',
       'f', 'g', 'h', 'i', 'j',
       'k', 'l', 'm', 'n', 'o',
       'p', 'q', 'r', 's', 't' ,
       'u', 'v', 'w', 'x', 'y',
       'z']

result = []
for word in abc:
    pos = 0
    for i in s:
        if i == word:
            result.append(pos)
            break
        elif i == '\n':
            result.append(-1)
            break
        pos += 1

print(*result)
