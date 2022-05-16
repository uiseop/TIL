# 알고리즘 문제를 매일 풀면서 JS 메서드들을 익혀보자.

## 목차 <hr/>
- <a href="#1">백준에서 자바스크립트 사용하는 법</a>
- <a href="#2">Graph</a>
    - <a href="#2_1">Dijkstra</a>
<hr/>
## <p id="1">백준에서 자바스크립트로 문제 풀기</p>
백준에는 자바스크립트가 없다. 그래서 node.js를 통해 문제를 풀어야 한다고 한다.  

때문에 CommonJS 라이브러리를 사용해서 문제를 풀어야 하고, 라이브러리를 import 하기 위해서는 `require("..")`를 사용한다.  

```js
let fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().split(" ")
➡️ 위의 코드는 백준 사이트에서 예제들의 채점을 위한 stdin 경로를 표시
let input = fs.readFileSync("test.txt").toString().split("\n")
➡️ 로컬에서 돌릴때는 "test.text"로 하도록 한다.
let a = parseInt(input[0])
let b = parseInt(input[1])
```
코드를 보면 Node.js의 `built-in file system module`을 사용  
dev 디렉터리의 stdin 파일을 읽어서 string의 split 메서드를 사용하기 위해 모든 input 들을 toString 시켜주고 split을 진행해주는것으로 보인다.  
그런 후 string 처리 된 Number들을 다시 parseInt/Number로 정수로 만들어준다.  

### 그럼 parseInt와 Number의 차이점은 뭐지..?
- parseInt: 문자열의 인자를 숫자로 변경해준다. 대신 `숫자로 시작`하는 경우 숫자로 변경해주고 그렇지 않으면 `NaN`을 return하게 된다.  또한 `1000원`같이 숫자로 시작하면서 string이 함께 있을 때 숫자가 끝날때 까지만 형변환을 진행해준다.  
- Number: 문자열이 숫자이면 숫자로 변형하고, 문자열이 하나라도 껴 있으면 NaN을 return하게 된다. 

✅ 결론: parseInt가 Number보다 좀 더 유연하게 형변환을 진행하기때문에 앞으로 parseInt를 자주 사용해보도록 한다.
## <p id="2">Graph</p>

### 비선형 자료구조 -> Object(객체)를 사용한다
Object의 메서드를 알아봐야지? 
- Object.keys(obj): obj객체의 모든 key값들을 배열로 반환한다
- Object.values(obj): obj객체의 모든 value값들을 배열로 반환한다
- Object.entries(obj): obj객체의 `[key,value]`로 이뤄진 이차원 배열을 반한다.

### new 연산자 -> 생성자 함수를 생성할 때 반드시 필수
```js
function User(name) {
  // this = {};  (빈 객체가 암시적으로 만들어짐)

  // 새로운 프로퍼티를 this에 추가함
  this.name = name;
  this.isAdmin = false;

  // return this;  (this가 암시적으로 반환됨)
}
```
`new` 연산자를 사용해서 User 객체를 생성하면 새로운 객체가 생성된다.

### <p id="2_1">Dijkstra 알고리즘</p>

`Single Source Shortest Path` 이란 하나의 출발점에서 각 정점까지 도달하는데 비용을 계산하여 최단 경로를 구하는 것 입니다. 

하나의 정점에서 다른 정점으로 가는데 payload를 계산하여 가장 최단 거리를 구하는건 계산에 있어 많은 이점을 주기때문에 실생활에서 가장 필요한 알고리즘이 아닐까 생각이 듭니다. 

`Single Source Shortest Path`와 대비되는 주제로는 `All Pair Shortest Path`가 있는데 ASP는 모든 정점끼리의 최단 경로를 계산합니다. 즉, SSP는 1차원 배열로써 각 정점까지 경로의 비용을 표현할 수 있지만, ASP는 2차원 배열이 필요하다고 합니다. 이는 다음에 살펴보도록 하고, 우선 하나의 정점에서 출발하여 모든 정점으로의 최단 경로를 계산하는데 있어 경로에 `음의 가중치`가 있느냐 없느냐에 따라 알고리즘이 달라진다고 합니다.  

- 음의 가중치를 허용: **Bellman-Ford**알고리즘
- 음의 가중치 허용X: **Dijkstra**알고리즘

Dijkstra 알고리즘은 한 정점에서 다른 정점들로의 최소 비용을 계산하는 알고리즘이기 떄문에 우리가 아는 최대/최소값을 빠른 속도로(`O(logN)`) 계산하는 힙(Heap) 자료구조가 필요할것으로 예상됩니다. 힙 자체가 우선순위 큐를 위해서 만들어진 자료구조이고, 우선순위를 가중치가 가장 낮을수록 높게 주면 된다.  

때문에 우리는 2개의 자료구조가 필요하게 된다. 우선 정점간의 거리를 저장하는 `Distance 객체` 그리고 우선순위 큐가 필요하다. 일단 오늘은 객체를 사용해서 값을 저장하고, 한 정점에 연결된 모든 간선들을 확인하여 최솟값을 찾으면 된다.

글로만 작성하려니 힘들긴하지만.. 나머지는 코드를 보면서 확인하자.

이 떄 최소 우선순위 큐에는 `[vertex, weight]`정보가 들어가야하고, 우선순위는 weight를 기준으로 한다. distance객체에서는 그 노드로 가는데 드는 비용을 저장하고, 한번 우선순위 큐에서 pop해서 가지치기를 한 노드는 중복 계산을 피하기 위해 Visited 객체를 생성해서 중복을 방지해준다.