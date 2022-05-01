# 백준 1157번 - 단어 공부
# https://www.acmicpc.net/problem/1157
import sys
alpha = ['A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y',
         'Z']

word = list(sys.stdin.readline().strip().upper())
cnt = 0
same = 0
result = 'a'

for x in range(26):
    if word.count(alpha[x]) > 0 and word.count(alpha[x]) > cnt:
        cnt = word.count(alpha[x])
        result = alpha[x]
    elif word.count(alpha[x]) > 0 and word.count(alpha[x]) == cnt:
        same += 1
        result = '?'
        
print(result)
