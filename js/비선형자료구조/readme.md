# 우선순위 큐
- 우선순위를 고려하여 먼저 넣은 데이터가 먼저 나오는 `FIFO(First In FIsrt Out)` 기반의 선형 자료구조
- FIFO는 Stack의 특성인데 Stack이랑 비슷하게 먼저 넣은 데이터가 먼저 나온다고 해. (단, 우선순위 기반으로 나중에 들어와도 우선순위가 높으면 앞에 위치함.)
- 우선순위 정렬 방식: 배열 기반, 연결리스트 기반, 힙(Heap) 기반 등의 정렬 방식이 존재.

## 구현 메서드
- 데이터 전체 획득 / 비어있는지 확인: getBuffer(), isEmpty()
- 데이터 추가 / 삭제: enqueue(), dequeue()
- 첫번째 데이터 / 사이즈 / 전체 삭제: front(), size(), clear()

# 원형 큐
- 원형 형태를 가지면서 큐랑 같은 성질을 갖어.
- 딱히 차이가 없기때문에.. 구현은 하지 않겟따. 큐 최적화 하는 과정에서 index로 head와 tail을 줬었는데 사실 이 과정이 원형큐랑 비슷.
- 크기가 정해져있기때문에 `isFull()`이라는 메서드를 갖음.

# 데크(Dequeue)
- 파이썬에서 많이 사용했었던 데크.
- 삽입과 삭제가 양쪽 끝에서 모두 발생할 수 있는 선형 자료 구조. // 파이썬에서 `appendleft(), popleft(), ...`

## 구현 메서드
- 데이터 전체 획득 / 비어있는지 확인: getBuffer(), isEmpty()
- 데이터 추가 / 삭제: pushFront(), popFront(), pushBack(), popBack()
- 첫번째 & 끝 데이터 반환 / 사이즈 / 전체 삭제: front(), back(), size(), clear() 

# 딕셔너리
- 파이썬 언어에서는 기본 자료형으로 제공되고 있는 key-value형태로 다양한 자료형 개체를 저장하는 자료구조. (JS에서의 Map)
- 일반 객체는 key값으로 `string`만 가능하지만 딕셔너리나 Map의 경우는 `다양한 자료형 개체를 key값으로` 선언할 수 있다는 장점이 있찌.

## 구현 메서드
- 전체 개체 획득 / 초기화 / 크기 반환: getBuffer(), clear(), size()
- 개체 추가 / 삭제 / 반환 / 여부: set(), remove(), get(), has()
- key,value 배열 반환 / 고차 함수: keys(), value(), each()

# 해시 테이블 / 해시 함수
- Hash 함수를 사용하여 탐색시 평균 O(1)의 시간 복잡도를 갖는 특정 값을 신속하게 찾는 자료구조.
- Hash 함수란, 임의의 입력값을 넣으면 고정된 길이의 값을 반환하는 함수.
- 고정된 길이는 제한적이기 때문에 Hash 테이블에서는 중복된 `해시값`을 갖는 `Collision`문제가 발생한다고 한다.

## Collision 해결법
- 선형 조사법: 중복된 해시값을 갖고있으면 +1,+1, ... 하면서 빈 공간을 찾는 방법
- 이중 해시: 말 그대로 해시함수를 2번 적용해서 다른 값이 나타나도록 함 -> 고정된 길이는 역시 제한적이기때문에 Collision 발생할 수 있지.
- 체이닝: 해시 테이블의 중복값을 Linked List로 연결해서 차례대로 넣는방법

# 트리 (Tree)
- 그래프의 일종으로 `두 노드 사이에 하나의 간선만 연결되어 있는`, 최소 연결과 계층 형태의 비선형 자료구조
- 주요 특징: 
    - 최소 연결 트리라고 불림
    - 계층 모델
    - 방향 `비순환 그래프`의 한 종류
- 트리 종류:
    - 이진 트리
    - 이진 탐색 트리
    - AVL 트리
    - 힙(Heap)

# 그래프 (Graph)
- 정점과 간선으로 구성되어 `네트워크 구조`를 추상화한 비선형 자료구조
- 특징
    - 정점(Vertex)과 간선(Edge)의 집합
    - 다양한 그래프 종류를 혼합하여 표현 가능
- 종류
    - 방향 그래프(Directed Graph): 간선에 특정 방향이 존재하는 그래프(A->B로 표현, A에서 B로만 이동 가능)
    - 무방향 그래프(Undirected Graph): 간선에 특정 방향이 존재하지 않는 그래프(A-B로 표현, 양방향 이동 가능)
        - 연결 그래프(Connected Graph): 무방향 그래프에 있는 모든 정점들에 대한 경로가 항상 존재하는 그래프 -> 한붓그리기가 가능한 그래프
        - 비연결 그래프(Disconnected Grpah): 무방향 그래프에서 한붓그리기가 불가능한 그래프
    - 가중치 그래프(Weighted Graph): 간선에 비용이나 가중치가 할당된 그래프
    - 순환/ 비순환 그래프: 시작 정점과 종료 정점이 동일하면 순환, 아니면 비순환
    - 완전 그래프: 모든 정점이 서로 연결되어 있는 그래프

## 그래프의 표현/구현
- 인접 리스트(Adjacent List): 정점에 연결된 다른 정점을 리스트로 표현 (A는 B,C,D와 연결, B는 A,E,F와 연결 ...)
- 인접 행렬(Adjacent Matrix): 정점에 연결된 다른 정점을 정점*정점 크기의 매트릭스로 표현(\[[0,1,1], [1,0,0], [1,0,0]]...\)

# 자바스크립트 2차원 배열 만들기

```javascript
const visited = Array.from(Array(width), () => Array(width).fill(false))
// false로 채워진 width*width 배열을 만들 수 있음.
// 만약 빈 배열을 만들고 싶으면 그냥 fill없이 사용하면 돼
```

# 힙 (Heap)
- 최대값 혹은 최솟값을 빠르게 찾기 위해 완전 이진트리 형태로 연산을 수행하는 구조.
- 정렬: 각 노드의 값은 자식 노드가 가진 값보다 작거나 혹은 큰 순서대로 정렬
- 최대힙: 최대값이 root
- 최소힙: 최소값이 root

# 트라이 (Trie)
- 탐색 트리의 일종으로, 문자열이나 연관 배열을 저장하는 데 사용되는 트리 자료 구조
- 트라이의 특징
    - 문자열 검색에 특화된 자료 구조
    - 문자열 길이가 M일 경우 O(M)의 시간 복잡도로 검색 가능

- 가령 ["be", "bee", "cat", "can", "cd"]의 문자열을 저장하는데 Trie자료구조를 사용하면 `8개의 노드만 사용하면 됨`