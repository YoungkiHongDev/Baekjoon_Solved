# 백준 24479번 - 알고리즘 수업 - 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479

'''
모든 입력을 받은 후 내림차순 정렬
스택 DFS로 재귀와 같은 순서를 위해 deque 사용
해당 노드를 방문할 때 방문 처리
방문 처리시 리스트 길이만큼 순회하여 시간복잡도 O(N)인 if not visit 대신에
시간복잡도 O(1)을 위해 방문 체크한 리스트로 하나씩만 확인하는 if not visit[노드변수] 사용
'''

'''
6 7 1
1 6
1 2
2 6
2 3
2 4
3 5
4 5
'''

import sys
from collections import deque

def dfs(start): # DFS 함수
    stack = deque([start]) # 재귀 DFS와 같은 순서를 위해 deque 사용
    cnt = 1 # 방문 순서 카운트 변수
    while stack: # 스택이 빌 때까지 반복
        start_node = stack.pop() # 스택에서 꺼내기
        visit[start_node] = True # 방문 처리
        if count[start_node] == 0: # 만약 방문 순서 기록이 없는 노드라면
            count[start_node] = cnt # 카운트 저장
            cnt += 1 # 카운트 증가
        for next_node in graph[start_node]: # 인접노드 모두 확인하기 위해 반복
            if not visit[next_node]: # 만약 방문하지 않은 노드라면
                stack.append(next_node) # 스택에 넣기
    return count[1:v+1] # 필요없는 0번을 제외하고 리턴

v, e, r = map(int, sys.stdin.readline().rstrip().split()) # 정점수, 간선수, 시작노드 입력
graph = [[] for _ in range(v+1)] # 간선을 입력받을 리스트
visit = [False for _ in range(v+1)] # 방문 체크할 리스트
count = [0 for _ in range(v+1)] # 노드 방문 순서를 기록할 리스트

for _ in range(e): # 간선수만큼 반복
    node, near = map(int, sys.stdin.readline().rstrip().split()) # 노드와 인접노드 입력
    graph[node].append(near) # 간선 이어주기
    graph[near].append(node) # 간선 이어주기

for i in range(v+1): # 정점수만큼 반복
    graph[i].sort(reverse=True) # 인접노드 내림차순 정렬

result = dfs(r) # dfs 함수 호출
print(*result, sep='\n') # 결과 출력