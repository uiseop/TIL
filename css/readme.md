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
5. <code>가상클래스 선택자</code> <code>태그이름 + : </code>로 시작해. 클래스는 없지만 있는것처럼 동작하도록!
    - li:first-child 👉 콜론(:)과 조건을 명시해서 그 부분만 스타일링해줄수 있어. 🔥주의! first-child는 해당 셀렉터의 부모요소로 가서 부모요소의 첫번째 자식을 선택하는거야. 만약 부모의 첫번쨰 자식의 class이름이 다르면 스타일링되는애는 없을 수 있지 // + last-child, <code>nth-child</code>(몇번째 자식인지/함수표현식도 가능 가령 2n, 2n-1, odd, even)
    - first-of-type 👉 first-child의 허점을 피할 수 있어. 부모요소에서 선택자의 첫번째들 모두를 선택해주는거야! // + last-of-type, nth-of-type() ...  👍👍이걸 더 많이 사용한데
    - <code>:not</code> 👉 :not(.class명) or :not([type=text])
    - 상태에 따라 변경되는 동적 가상클래스 선택자 : <code>link</code> a:link, <code>visited</code> a:visited 방문을 하기 전의 색과, 방문을 했을 떄의 색을 지정할 수 있어!
    - <code>hover, active, focus</code> 👉 마우스의 상태에 따른 스타일 변경! active는 마우스를 클릭했을 때(mouseDown) 이벤트가 발생시 일어나!(버튼 클릭시!). focus는 tab키로 이동시켰을 때 보이더라구. 아니면 input태그로 current.focus시킬때 사용
    - <code>enabled, disabled, checked</code> 👉 html 속성인 disabled인 애를 선택할 수 있어. 가령 input[type="text"]:enabled : disabled가 아닌애들만 따로 선택해서 스타일링을 하겠다!
6. <code>가상요소 선택자</code> 사용법은 클래스 선택자랑 비슷한데 얘는 더블클론(::)을 사용하는걸 추천한댜(하나만써도 동작은 혀)
    - <code>after, before</code> : CSS로 가상의 요소를 HTML에다 추가하는거야. 그러고 그 추가한 요소에 스타일링을 하는거!!
    ```
    .favorite::before{
        content:'🔥'; // 이렇게 하면 favorite클래스 앞에다가만 구분점으로 콘텐츠를 추가(꾸밈)해줘!
    }
    ```
    - <code>first-letter, first-line, selection</code> 뜻그대로 첫번쨰 글자, 첫번쨰줄에 스타일링을 줘. selection은 선택영역에 대한. <code>drag</code>한 영역을 내 입맛대로 스타일링 해줄 수 있어!
    - <code>하위, 자식, 형제 선택자, 그룹화</code> 하위 : 스페이스로 구분, 자식 <code>></code>꺽세로 범위를 좁힐 수 있어.
        - 일반 형제 선택자 결합(~) <code>span ~ p</code> 라고 하면 span의 형제 태그중 아래있는 p들을 선택해
        - 인접 형제 선택자 결합(+) <code>span + p</code> 라고 하면 span인접한 요소만(바로 뒤) 고를 수 있어!
    - <code>상속 제어하기</code> 👉 initial, inherit, unset이 있어!. how? all:initial로 상속을 끊을 수 있어 default로 돌리는거야!

# 폰트 관련 속성

1. <code>font-size/weight/family/style</code>을 가장 많이 사용. 한번에 선언하는 방법 : size,family를 입력한 후에, 그 앞에 style,weight를 입력하고 height의 경우 사이즈/높이 (슬레시 필수)로 작성해
2. <code>Letter Spacing</code> 문자 사이 간격을 조정 : letter-spaing / word-spacing의 값을 할당. ex) 3px
3. <code>text-align</code> 텍스트를 위치시키는 요소. block요소인지, inline요소인지에 따라 위치가 조정이 안될수도 있어. 왜냐! 전체 길이를 기준으로 좌,가운데,우로 정렬을 시키는것이기 때문에!
4. <code>text-indent</code> 텍스트의 시작부분을 npx; 만큼 띄워쓰게 해줄 수 있는아이. font-align과 마찬가지로 block 요소인지, inline요소인지에 따라 달라져!
5. <code>text-decoration</code> 해석 그대로 텍스트를 꾸며주는 요소. default는 solid형태고 테이블 스타일링하는거랑 비슷햐! 특징은 여러가지 요소를 함께 작성이 가능하다. 텍스트 컬러랑 꾸며놓은 요소랑 색을 바꿀 수 있어! 얘도 font처럼 한번에 작성할 수 있는데 font랑 다르게 <code>정해진 위치</code>가 따로 없어!
6. <code>word-break</code>는 berak-all, keep-all 두가지 요소가 있어. 정해진 너비 크기를 넘어가는 텍스트를 강제로 사이즈를 조정시켜줄 수 있어. break-all을 사용하면 영어를 사이즈 조정할 수 있어. keep-all은 줄바뀜되는 요소를 없애. 스페이싱이 없으면!
7. <code>text-transform</code> 적용되는 언어가 정해져잇어. 한국어는 ❌ uppercase,lowercase, capitalize(첫글자를 대문자화) 시킬 수 있어.

# CSS 값과 단위

1. <code>절대길이</code> : px을 대부분 사용하지
2. <code>상대길이</code> : em : 1em은 부모의 font-size 상대적으로 부모의 사이즈를 따라가게 되어있어(<code>사실 %랑 똑.같.다</code>),rem : root의 font-szie를 따라가. 직관적으로 이해하기가 편햐져!
    - <code>vw/vh</code> : 뷰포트란? 사이트에서 볼 수 있는 웹사이트의 화면비율. 100vw는 100% 뷰 너비, 100vh는 100% 뷰 높이 👉 디바이스의 크기에 따라 <code>반응형으로</code>웹사이트를 만들려 할 때 유용해!
    - <code>vmin/vmax</code> : vw,vh중에 작은애가 vmin, 큰애가 vmax로 지정 돼. <code>어디서 사용?</code>
    - <code>퍼센트(%)</code> : 부모 값의 상대적으로 계산이 되게 되어이썽. 

3. 함수표기법
    - <code>calc()</code> : calc(100% - 50px)로 하면 100%에서 50px만큼을 빼주면서 반응형으로 만들 수 있어 // 연산자 좌우에는 공백이 필요해
    - <code>min()/max()</code> : min(100%, 200px)로 하면 2개 값중 더 작은값을 브라우저가 자동으로 선택해줄수 잇어.