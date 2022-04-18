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

- 연결 리스트는 모든 행위에 있어서 검색을 먼저 하는데 검색에 있어 `O(n)`만큼의 시간복잡도를 갖는다. 따라서 배열에 비해 삽입, 삭제 연산은 빠르지만 탐색이 느린 단점이 있겠다.