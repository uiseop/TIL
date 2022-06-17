# Vanilla Redux를 배워본다.

비록 CRA환경이지만, 우선 Vanilla JS 환경에서 Redux를 사용하는 방법을 배워보자.
Why? Redux는 React를 위한 라이브러리가 아니니까! JS환경이라면 어디서든 사용할 수 있엄.

우선 Redux를 사용하기 위해선 node를 통해 redux를 설치해줘야해.

```bash
npm i redux
```

그런 후 redux를 사용해서 변수를 저장하고 싶은 곳에다 이렇게 선언하면 돼.

```javascript
import { createStore } from "redux";
```

그럼 `createStore`를 통해 만들어진 `store`란 녀석이 뭘까? `store`는 우리가 사용하는 `state`변수들을 관리해주는 창고 같은 녀석이야. `state`는 우리의 Application에서 `바뀌는` data지. 그래서 만약 어떤 함수를 통해 변경이 발생하면 이것이 변경되었다는 사실을 알려줘야해.

Javascript에선 어떻게 하지??

가령 + 버튼이 있어서 Count변수를 증가시키려고 해.

그러면

```javascript
let count = 0;

const handleAdd = () => {
    count += 1;
    updateCount();
};
```

여기서 우리는 `handleAdd`함수에서 오직 `count += 1`만들 해 주기만 하면 되는데, 변경사항을 적용시켜주기 위해 `updateCount()`라는 녀석이 들어가. 그래서 우리의 함수는 더하고, 업데이트해주는 함수가 되어 버려서 한눈에 이 함수가 `어떤 일을 하는지` 모호하게 만들어버려..🤦‍♂️

그래서 등장한것이 바로 상태 관리 라이브러리다. 나는 그것들 중 `Redux`를 사용할것이야.

지금(2022/06/18)에는 `createStore`방식이 Legacy한 방법이라고 오류가 뜨지만 불가 몇 달전까지만 해도 사용하던 방법이니까 이렇게 해서 저장하는 방법도 알면 좋을것 같아.

## Store 생성하기

우선 우리는 `CreateStore`를 import해 왔어. 얘가 바로 store을 만들어주는 함수야.(닉값하네!)

그럼 만들어 보자.

```javascript
const reducer = () => {};

const store = createStore(reducer);
```

이렇게 하면 된데. 근데 reducer가 뭐냐고?? `createStore`는 말 그대로 `store`만 만들어 줘. 그러면 나머지 각 상황별로 `state`변수들을 관리하는 함수는 바로 콜백함수인 `reducer`함수인거야. That's it!!

`reducer`를 통해서 `store`에 저장된 값이 저장된다고 했어.
그러면 이 코드의 결과를 한번 봐바

```javascript
const reducer = () => {
    return "Hello";
};

const store = createStore(reducer);

console.log(store.getState()); // "Hello"
```

신기하지?? `reducer`가 `state`의 값을 `Hello`라고 했으니까 초기값은 Hello이고, 앞으로도 Hello지! 즉, `reducer`가 `return`한 값은 `store`의 초기값인거야.

그러면 이제 store에 연결된 reducer에게 어떻게 해서 일을 하라고 알려줄까? 그건 바로 store의 dispatch 함수를 사용하면 돼

```javascript
const reducer = (state=0, action) => {
    switch(action.type) {
        case "ADD":
            return state + 1;
        ...
    }
}

const onChage = () => {
    num.innerText = store.getState();
}

store.subscribe(onChage)

add.addEventListener("click", () => store.dispatch({ type: "ADD" }));
```

이런싟으로 작성하면 돼. 그리고 `store`에서 저장한 state의 변화는 `store`의 `subscribe함수`에서 감지하지. 우리가 Y튜브를 구독하면 새로운 영상이 올라올때마다 알람이 뜨잖아?? 그 `subscribe`와 똑같은 기능이야!
