# 목차

-   <a href="#1">웹팩이란?</a>
    -   <a href="#1_2">모듈이란?</a>
    -   <a href="#1_3">번들러란?</a>
-   <a href="#2">Redux를 공부해보자!</a>

# <p id="1">웹팩이란?</p>

웹팩은 **모듈**을 위한 **번들러**라고 소개되어 있다. 웹팩에 대해 자세히 알아보려면 이 '모듈'과 '번들러'가 무엇인지 알아보자.

> webpack is a **bundler** for **modules**. The main purpose is to bundle JavaScript files for usage in a browser, yet it is also capable of transforming, bundling, or packaging just about any resource or asset.

## <p id="1_2">모듈은 무엇일까?</p>

모듈(module)은 재사용 가능한 코드조각이다. 아주 쉽게 풀어쓰면 걍 `.js`파일이다. 모듈은 자신만의 파일 스코프를 갖고, `export, import` 할 수 있다. 우리는 `export, import` 라는 것을 ES6부터 확인할 수 있고, 이는 최신 브라우저가 제공하는 모듈 기능이다. 따라서 구형 브라우저에서(ES5 이하)는 사용할 수 없다. 따라서 브라우저에서 단독으로 모듈을 사용하기 보다는 `번들링`해서 배포서버에 올리는 방식을 주로 사용한다고 한다.

어쨋든, 초기 자바스크립트는 크기도 작고, 기능도 단순해서 하나의 `.js`파일 안에 모든 코드를 작성하는것이 가능했지만 Client단의 기능이 많아짐에 따라 코드가 점점커지고, 이 거대한 코드를 관리하기 위해 다른 언어에 있는 모듈이라는 기능을 가져온다.

브라우저가 본격적으로 모듈을 지원하기 전에는 자바스크립트를 사용하는 커뮤니티에서 CommonJS(`훗날의 Node.js...`)라는 모듈을 지원하는 라이브러리를 만들었다. `모듈시스템`은 전역에 선언된 var(전역 레벨 스코프를 갖는 변수..)의 사용으로 발생하는 부작용을 예방할 수 있기도 하다.

일반 스크립트와 구별되는 모듈의 특징은 다음과 같다.

> 1. 모듈은 항상 defer 속성을 붙인 것처럼 지연 실행된다. (굳이 body 끄트머리에 적지 않아도 된다.)
> 2. 모듈은 strict mode 로 실행된다.
> 3. 모듈은 자신만의 스코프를 갖는다. (파일 스코프)
> 4. 모듈은 단 한 번만 평가(실행)되고 필요한 곳에서 공유된다.
> 5. 모듈 최상위 레벨 this는 undefined이다.
> 6. import.meta 객체로 정보를 얻을 수 있다. (e.g. import.meta.url

## <p id="1_3">번들러는 무엇일까</p>

JS, CSS, 이미지 등의 파일을 묶어주는 작업을 `"번들링"`이라고 하고, 작업의 결과물을 `"번들"`이라고 한다. 웹팩 자체는 이름처럼 묶어주는 역할을 하기 때문에 `"번들러"`라고 한다고 한다.

번들링 과정이 끝나면 기존 스크립트에서 import/export가 사라지기 때문에 `type="module"`이 필요 없어진다. 따라서 번들링 과정을 거친 스크립트는 일반 스크립트처럼 취급한다.

## 그래서 웹팩은 왜 쓰는걸까

2012년 처음 등장한 웹팩은 2020년 version 5를 발표하기까지 꾸준한 성장세를 그리고 있다. 웹팩이 이렇게까지 사랑받는 이유는 무엇일까? 더 많은 장점이 있겠지만 내가 이해할 수 있는 수준의 장점은 다음과 같다.

우선, 웹팩은 여러 개의 파일을 하나로 번들링하기 때문에 `HTTP 요청 횟수`를 줄일 수 있다. 이는 빠른 서비스 제공에 도움이 된다.(브라우저마다 <a href="https://joshua1988.github.io/webpack-guide/motivation/problem-to-solve.html#%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EB%B3%84-http-%EC%9A%94%EC%B2%AD-%EC%88%AB%EC%9E%90%EC%9D%98-%EC%A0%9C%EC%95%BD" rel="noreferrer" target="_blank">HTTP 요청 횟수에 제한</a>을 두고 있기도 하다.) 또한, 자바스크립트 외의 리소스 포맷의 모듈도 사용할 수 있게 해 준다. CSS든, 이미지든 사용하려는 곳에 해당 리소스를 import 해주기만 하면 웹팩이 알아서 빌드해준다!! 웹팩이 알아서 자동화해주는 덕분에, 코드를 수정했을 때 다시 빌드하고 `새로고침 하지 않아도` 바로바로 빌드 결과를 확인할 수 있다. 또, 코드 스플리팅으로 원하는 Require.js와 같은 라이브러리 없이도 통째로 로딩하지 않고, 필요한 순간에 원하는 모듈을 불러올 수 있다고 한다(`Dynamic Loading`, `Lazy Loading`)

# <p id="2">Redux를 배워보자!</p>

## Redux Toolkit

`Redux Toolkit`은 Redux를 쉽게 사용할 수 있도록 제공하는 Toolkit이다. Redux는 아주 작은 라이브러리(2KB)이기 때문에 다른 필요한 라이브러리들이 많다. 하지만 Redux toolkit은 CRA를 사용할때 단 한번의 설치로 편리하게 Redux의 모든 기능을 사용할 수 있다고 한다.

그리고 무엇보다도 Redux사용의 `표준`으로 정의하고 있기때문에 Redux를 사용하기 보다는 Redux Toolkit을 사용해보도록 하자!!

### 처음에 설치

```bash
# Redux + Plain JS template
npx create-react-app my-app --template redux

# Redux + TypeScript template
npx create-react-app my-app --template redux-typescript
```

### 기존 애플리케이션에 추가

```bash
# NPM
npm install @reduxjs/toolkit

# or

# Yarn
yarn add @reduxjs/toolkit
```

### Redux Toolkit Query(= RTK Query)

Redux Toolkit Query는 Redux Toolkit에서 제공하는 `API interface`이다. 이걸 사용하면 직접 data를 fetch하거나 caching하는 로직을 작성할 수고를 줄여준다고 한다. 또한 브라우저 Extension을 설치하면 서버에서 받아온 데이터들이 어떻게 저장되고 움직이는지 확인할 수 있다고 해😎

```bash
import { createApi } from '@reduxjs/toolkit/query'

/* React-specific entry point that automatically generates
   hooks corresponding to the defined endpoints */
import { createApi } from '@reduxjs/toolkit/query/react'
```
