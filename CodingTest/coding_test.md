# CodingTest

* [Algorithms](./algorithms/algorithms.md)

## Cheetsheet

* 시간이 오래 걸릴 경우 -> parametric search (이분 탐색), heapq 이용
* 연쇄되는 규칙 -> dynamic programing
* 경로 탐색
  * depth first search
  * breath first search
  * Dijkstra
* dynamic programing
  * 점화식을 세우기
  * dp table 채우는 순서 확인하기
* 기타 알고리즘
  * Kruskal: greedy, 모든 정점을 최소 비용으로 연결

## Example Code
* Reference Sites:
  * [Github: TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)

* Binary Search Lower Bound
  ```python
  def binary_search_lower_bound(array, target):
    left = 0
    right = len(array)
    while left < right:
      mid = (left + right) // 2
      if target <= array[mic]:
        right = mid
      else:
        left = mid + 1
    return left
  ```

* Binary Search Upper Bound
  ```python
  def binary_search_lower_bound(array, target):
    left = 0
    right = len(array)
    while left < right:
      mid = (left + right) // 2
      if target >= array[mid]:
        left = mid + 1
      else:
        right = mid
    return left
  ```

* Dijkstra Algorithm
  ```python
  def dijkstra(start):
    pq = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
      dist, node = heapq.heappop(q)
      
      # continue if already processed node
      if distnace[node] < dist:
        continue
      
      for cost, next_node in graph[node]:
        next_dist = cost + dist
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if next_dist < distance[next_node]:
          distnace[next_node] = next_dist
          heapq.heappush(q, (next_dist, next_node))
  ```

* Depth First Search
  * Iterative Implementation
    ```python
    def dfs_iteration(graph, root):
      # visited = 방문한 꼭지점들을 기록한 리스트
      visited = set()
      # dfs는 stack, bfs는 queue개념을 이용한다.
      stack = [root]
      
      while stack: #스택에 남은것이 없을 때까지 반복
          node = stack.pop() # node : 현재 방문하고 있는 꼭지점
          
          #현재 node가 방문한 적 없다 -> visited에 추가한다.
          #그리고 해당 node의 자식 node들을 stack에 추가한다.
          if node not in visited:
              visited.add(node)
              stack.extend(graph[node])
      return visited
    ```

  * Kruskal Algorithm
    ```python
    def kruskal(
      num_nodes: int, edges: list[tuple[int, int, int]]
      ) -> list[tuple[int, int, int]]:
      """
      >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
      [(2, 3, 1), (0, 1, 3), (1, 2, 5)]
      >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
      [(2, 3, 1), (0, 2, 1), (0, 1, 3)]
      >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
      ... (2, 1, 1)])
      [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
      """
      edges = sorted(edges, key=lambda edge: edge[2])

      parent = list(range(num_nodes))

      def find_parent(i):
          if i != parent[i]:
              parent[i] = find_parent(parent[i])
          return parent[i]

      minimum_spanning_tree_cost = 0
      minimum_spanning_tree = []

      for edge in edges:
          parent_a = find_parent(edge[0])
          parent_b = find_parent(edge[1])
          if parent_a != parent_b:
              minimum_spanning_tree_cost += edge[2]
              minimum_spanning_tree.append(edge)
              parent[parent_a] = parent_b

      return minimum_spanning_tree
    ```