# 배열
- 여러 개체(Entity)값을 순차적으로 나열한 선형 자료 구조
- JS에서의 배열은 다른 언어에서 말하는 일반적인 배열이 아닌 `Hash` 기반의 객체 -> `delete 키워드`로 삭제해도 배열의 크기가 줄어들지 않고 `empty item`으로 채워져
- 메모리가 연속적인 밀집 배열이 아닌 비 연속적인 `희소 배열` ➡️ `객체`다.
```javascript
console.log(Object.getOwnPropertyDescriptors(arr));
/* output:
{
    '0': { value: "...", writable: true, enumerable: true, configurable: true},
    '1': //,
    ...,
    length: { value: // ... }
}
*/
```
## 대표 속성(property)과 메서드(method)
- 배열 크기 및 배열 여부 확인: Array.length, Array.isArray()
- 배열 추가/삭제: Array.push(), Array.pop(), Array.shift(), Array.unshift(), Array.slice(), Array.splice() 등 .. 
- 배열 탐색: Array.indexOf(), Array.lastIndexOf, Array.includes()
- 배열 변형: Array.sort(), Array.reverse(), Array.join()
- 배열 반복: Array.forEach(), Array.map(), Array.find(), Array.filter(), Array.reduce()
- 배열 논리연산: Array.some(), Array.every()

# 연결 리스트(Linked List)
- 각 노드가 `데이터(data)`와 `포인터(next)`를 가지며, `한 줄`로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조
- 구현 메서드(method)
    - 노드 개수/ 비어있는지/ 노드 출력: size(), isEmpty(), printNode()
    - 노드 추가/ 삭제: append(), insert() / remove(), removeAt()
    - 데이터 위치 확인: indexOf()

## 배열과의 차이점 

- 연결 리스트는 모든 행위에 있어서 검색을 먼저 하는데 검색에 있어 `O(n)`만큼의 시간복잡도를 갖는다. 따라서 배열에 비해 삽입, 삭제 연산은 빠르지만 탐색이 느린 단점이 있겠다.

# 이중 연결 리스트
- 각 노드가 데이터와 포인터를 가지며, `두 줄`로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조.
- 한 줄로 연결되어있는 연결 리스트와 달리 `두 줄`로 연결되어있어 양방향의 탐색이 가능한 자료 구조.

- 구현 메서드(method) - `연결 리스트와 동일`
    - 노드 개수/ 비어있는지/ 출력: size(), isEmpty(), printNode(), printNodeReverse()
    - 노드 추가/삭제: append(), insert(), remove, removeAt()
    - 데이터 위치 확인: indexOf()

## 연결 리스트와 차이점

- 연결 리스트는 포인터가 하나뿐이였기 때문에 prev라는 변수를 지정하여 삭제, 삽입 연산을 진행한다. ➡️ 이중 연결 리스트는 prev 포인터가 있어서 변수를 사용하지 않아도 삽입, 삭제 연산이 가능하지만 모든 노드에 포인터를 추가해야하는 만큼 `구현의 어려움`과 `메모리 사용량 증가`라는 단점이 있지.

- 단방향의 검색 뿐만 아니라, `Tail`이라는 프로퍼티가 있어 역방향 검색이 가능하다. 이는 탐색해야하는 엘리먼트가 반으로 줄어들게 되어 더 빠른 연산이 가능핟. 때문에 현실에서 사용하는 연결 리스트는 대부분 `이중 연결 리스트`이다.