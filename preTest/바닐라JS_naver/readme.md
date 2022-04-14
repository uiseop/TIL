# 바닐라 JS를 다시 복기해본다.

기본 CSS를 사용하기 보다 React에서 사용하는 Styled-Components처럼 작성할 수 있는 Sass를 사용해본다. 개발하는데에 있어 효율을 증가시켜주기때문에 선택이 아닌 `필수`라는 인식이 있음.

Sass는 컴파일을 통해 CSS파일을 만들어 준다고 한다. Styled-Components처럼 `변수`사용, `중첩 객체`, `mixins` 등의 다양한 기능을 제공해준다고 한다.

## CSS코드로 스타일링의 단점
- 가독성의 저하 (프로젝트가 커지게 되면 어디부터 어디까지가 어떤 스타일링을 담당하는지 몰라)
- 첫 번째의 이유로 중복 코드를 작성하기 쉬움
- 단순 수정에도 코드확인이 필요하게 돼
- 때문에 프로젝트가 커짐에 따라 작업속도가 뎌뎌지게 된다.

## 기본 Base
- VScode의 Watch Sass를 사용해서 Sass파일을 컴파일 해
- abstracts에는 많은 색상들에 대한 변수화가 진행.
- base에는 reset.css가 적용되어있음
- components에는 프로젝트에 사용될 컴포넌트의 스타일링을 진행하지
- pages는 페이지의 스타일링!?

### 새로 알게된 것
- role 속성
role속성은 접근성을 높여주는 속성이다. 아무래도 사용자가 많기때문에 접근성을 높인 정석적인 방식을 사용한듯 함

- scroll-x 스타일링 mixin 적용
```css
@mixin scroll-x {
    overflow-x: auto;
    overflow-y: hidden;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: none; // IE 스크롤바 감추기
    scrollbar-width: none; // Firefox 스크롤바 감추기
    &::-webkit-scrollbar {
        display: none; // Chrome 스크롤바 감추기
    }
}
```
이렇게 mixin으로 만들어도 되고, 아니면 명확하게 `style`을 만들어서 공통으로 적용되는 요소는 `_preset.scss`에서 불러오게 할 수 있겠군!