# 백준 11654번 - 아스키 코드
# https://www.acmicpc.net/problem/11654
word = input()
if word.isnumeric()==True:
    print(int(word)+48)
else :
    print(ord(word))
