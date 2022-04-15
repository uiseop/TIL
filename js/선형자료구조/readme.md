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