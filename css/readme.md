# CSS(Cascading Style Sheets)

<h1>캐스캐이딩 원칙</h1>

1. 스타일 우선순위
    - 동일한 스타일이라도 선언된 곳에 따라 우선순위가 정해진다. 브라우저 < 개발자 < 사용자(게임 색약모드)
    - 적용 범위가 적을수록 우선시 된다. tag < class < id < inline->css파일을 무시해버려
    - 소스코드의 순서가 뒤에 있으면 덮어쓴다
2. 스타일 상속
    - 부모 요소에 있는 스타일 속성들이 자식 요소로 전달된다
    - 상속이 되지 않는 속성도 있다. 배경이미지, 배경색 등..

# 선택자

1. <code>속성값</code> : 태그 안에 특정 요소를 포함한 애만 스타일링 하고 싶어! 👉 <code>a[target]</code> 처럼 태그 + [속성값] 을 쓰면 돼! (텍스트는 그냥쓰고 속성명은 대괄호 안에 사용)
    - 가령 a태그의 href값이 일치하는 애들만 바꿔줄수도 있어!!
    - input태그의 type값이 일치하는 애들만 바꿔줄수도 있어!!
2. <code>attr^=value</code> : 정규표현식 사용 가능한가봐! ^:~로 시작하는 a[href^=http://]
3. <code>attr$=value</code> : $로 끝나는 값!! a[href$=".com"]
4. <code>attr*=value</code> : value를 포함하고 있는!! a[href="naver"]
5. <code>가상클래스 선택자</code> <code>태그이름 + : </code>로 시작해
    - li:first-child 👉 콜론(:)과 조건을 명시해서 그 부분만 스타일링해줄수 있어. 🔥주의! first-child는 해당 셀렉터의 부모요소로 가서 부모요소의 첫번째 자식을 선택하는거야. 만약 부모의 첫번쨰 자식의 class이름이 다르면 스타일링되는애는 없을 수 있지 // + last-child, <code>nth-child</code>(몇번째 자식인지/함수표현식도 가능 가령 2n, 2n-1, odd, even)
    - first-of-type 👉 first-child의 허점을 피할 수 있어. 부모요소에서 선택자의 첫번째들 모두를 선택해주는거야! // + last-of-type, nth-of-type() ...  👍👍이걸 더 많이 사용한데
    - <code>:not</code> 👉 :not(.class명) or :not([type=text])
    - 상태에 따라 변경되는 동적 가상클래스 선택자 : <code>link</code> a:link, <code>visited</code> a:visited 방문을 하기 전의 색과, 방문을 했을 떄의 색을 지정할 수 있어!
    - <code>hover, active, focus</code> 👉 마우스의 상태에 따른 스타일 변경! active는 마우스를 클릭했을 때(mouseDown) 이벤트가 발생시 일어나!(버튼 클릭시!). focus는 tab키로 이동시켰을 때 보이더라구. 아니면 input태그로 current.focus시킬때 사용
    