# 알고리즘 문제를 매일 풀면서 JS 메서드들을 익혀보자.

## 목차 <hr/>
- <a href="#1">백준에서 자바스크립트 사용하는 법</a>
- <a href="#2">Graph</a>
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
