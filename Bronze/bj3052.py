#백준 3052번 - 나머지
import sys

nl = []
for i in range(10):
    nl.append(int(sys.stdin.readline()) % 42)

result = set(nl)
print(len(result))
