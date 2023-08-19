# 백준 14568 - 2017 연세대 프로그래밍 경시대회
# 완전탐색 알고리즘
# https://www.acmicpc.net/problem/14568

'''
택희, 영훈이, 남규 3명에게 사탕을 분배한다.

조건
1. 남는 사탕 없어야 한다.
2. 남규는 영훈이보다 2개 이상 많이 받는다.
3. 셋은 사탕을 1개 이상 받는다.
4. 택희가 받는 사탕은 짝수이다.

'''

candy = int(input())
result = 0

# 조건3번으로 셋 모두 사탕을 받는걸 전제로 하여 3중 for문 초기값을 1로 한다.
for a in range(1, candy+1):
    for b in range(1, candy+1):
        for c in range(1, candy+1):
            # 조건 1, 2, 4번을 한꺼번에 처리한다.
            if a+b+c == candy and a >= b+2 and c % 2 == 0:
                result = result + 1

print(result)
