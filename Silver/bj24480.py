# 백준 24480번 - 알고리즘 수업 - 깊이 우선 탐색 2
# https://www.acmicpc.net/problem/24480
import sys

def dfs(start): # DFS 함수 (스택구조)
    stack = [start] # 시작노드 스택에 넣기
    cnt = 1 # 방문 순서 카운트 변수
    while stack: # 스택이 빌 때까지 반복
        node = stack.pop() # 스택에서 노드 꺼내기
        visit[node] = True # 방문 처리
        if count[node] == 0: # 방문한 노드가 첫방문이라면
            count[node] = cnt # 순서 기록
            cnt += 1 # 순서 카운트 증가
        for next in graph[node]: # 인접노드 순회
            if not visit[next]: # 방문하지 않은 인접노드라면
                stack.append(next) # 스택에 넣기
    return count[1:len(count)+1] # 결과에 필요없는 0번 인덱스를 제외하고 리턴

n, m, r = map(int, sys.stdin.readline().rstrip().split()) # 정점수, 간선수, 시작노드 입력
graph = [[] for _ in range(n+1)] # 간선을 입력받을 리스트
visit = [False for _ in range(n+1)] # 방문 체크할 리스트
count = [0 for _ in range(n+1)] # 방문 순서를 기록할 리스트

for _ in range(m): # 간선수만큼 반복
    key, value = map(int, sys.stdin.readline().rstrip().split()) # 노드, 인접노드 입력
    graph[key].append(value) # 간선 잇기
    graph[value].append(key) # 간선 잇기

for i in range(len(graph)): # 정점수만큼 반복
    graph[i].sort() # 인접노드 오름차순 정렬

result = dfs(r) # DFS 함수 호출
print(*result, sep='\n') # 결과 출력