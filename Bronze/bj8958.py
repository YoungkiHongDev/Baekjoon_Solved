# 백준 8958번 - OX퀴즈
# https://www.acmicpc.net/problem/8958
import sys
n = int(sys.stdin.readline())

for i in range(n):
        score = 0
        nowo = 0
        ox = list(sys.stdin.readline().strip())

        for y in ox:
            if y == 'O':
                nowo += 1
                score += nowo
            elif y == 'X':
                nowo = 0
                
        print(score)
