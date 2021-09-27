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
    - <code>enabled, disabled, checked</code> 👉 html 속성인 disabled인 애를 선택할 수 있어. 가령 input[type="text"]:enabled 👉 disabled가 아닌애들만 따로 선택해서 스타일링을 하겠다!
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
6. <code>word-break</code>는 berak-all, keep-all 두가지 요소가 있어. 정해진 너비 크기를 넘어가는 텍스트를 강제로 사이즈를 조정시켜줄 수 있어. break-all을 사용하면 영어를 사이즈 조정할 수 있어. keep-all은 줄바뀜되는 요소를 없애. 스페이싱이 없으면! 줄바꿈 할 때 단어 기준으로 할 지 글자 기준으로 할 지 정하는 속성! 댓글이나 포스팅 쓸 때 태그 속성으로 정할 수 있어!
7. <code>text-transform</code> 적용되는 언어가 정해져잇어. 한국어는 ❌ uppercase,lowercase, capitalize(첫글자를 대문자화) 시킬 수 있어.

# CSS 값과 단위

1. <code>절대길이</code> : px을 대부분 사용하지
2. <code>상대길이</code> : em : 1em은 부모의 font-size 상대적으로 부모의 사이즈를 따라가게 되어있어(<code>사실 %랑 똑.같.다</code>),rem : root의 font-szie를 따라가. 직관적으로 이해하기가 편햐져!
    - <code>vw/vh</code> : 뷰포트란? 사이트에서 볼 수 있는 웹사이트의 화면비율. 100vw는 100% 뷰 너비, 100vh는 100% 뷰 높이 👉 디바이스의 크기에 따라 <code>반응형으로</code>웹사이트를 만들려 할 때 유용해!
    - <code>vmin/vmax</code> : vw,vh중에 작은애가 vmin, 큰애가 vmax로 지정 돼. <code>어디서 사용?</code>
    - <code>퍼센트(%)</code> : 부모 값의 상대적으로 계산이 되게 되어이썽. 

3. 함수표기법
    - <code>calc()</code> : calc(100% - 50px)로 하면 100%에서 50px만큼을 빼주면서 반응형으로 만들 수 있어 // 연산자 좌우에는 공백이 필요해
    - <code>min()/max()</code> : min(100%, 200px)로 하면 2개 값중 <code>더 작은값을</code> 브라우저가 자동으로 선택해줄수 잇어. 따라서 뷰포트vw, vh에따라 반응형으로 디자인이 가능하지!

# 박스 모델

1. 태그 자체 속성이 <code>inline</code>인 친구들은 width를 아무리 줘도 더이상 넓어지거나 좁아지지 않아(변경X!) inline 은 css 속성을 변경할 수 없어
2. 짜부가 되지 않도록 하는 속성 <code>min-width, max-width</code>를 하면 더이상 짜부가 되지 않아ㅋㅋ
3. <code>margin</code>는 box양파껍데기의 가장 밖쪽 요소. 상하좌우 순으로 입력을 받고, 2개만 입력받으면 y축,x축 요소 영향, 3개받으면 위, (좌,우), 아래, <code>%(퍼센트)</code>값은 무조건 부모의 <code>width값</code>의 %로 계산 돼 // 이는 padding도 동일해!
4. <code>마진상쇄</code>:block요소, 위/아래 margin에만 일어나는 현상으로, 둘 중 큰 크기를 가진 margin으로 합쳐져
    - 부모요소와 자식요소 : margin top이 상쇄돼 <code>해결법</code> : 두가지 사이를 끊어줄 수 있는 요소 : boredr/padding요소를 추가해주면 해결!
    - 혹여나 margin을 줫는데 동작을 안하면 이걸 떠올려!
5. <code>border</code> : 기본값은 none, 키워드로 스타일을 정할 수 있어/short hand(단축속성)도 있어. <code>스타일, 두꼐, 색상</code>
6. <code>outline</code> : border랑은 다르게 tab이나 마우스로 클릭했을 때 focus되는 속성이 outline이야!
7. <code>box-sizing</code> : <code>총 너비, 높이</code>길이를 설정한 width, height로 반응형으로 움직여. padding혹은 border의 크기만큼 커지거나 작아져!. 값은 <code>border-box</code>는 border사이즈를 합친 사이즈가 총 사이즈가 되는거야, default는 content-box : 설정❌ 기본 사이즈를 갖고 있고, border의 크기가 더해져!

# 레이아웃

1. <code>display</code> : block인지, inline인지, inline-block인지! 
    - inline요소는 top/bottom의 margin,padding을 추가하지 못해. 대신 여러 요소가 가로 배치가 가능 해
    - block요소는 여러 요소가 세로 배치가 돼. 
    - inline-block요소의 대표적인 예는 input. block요소처럼 width, height를 지정할 수 있는데 가로 배치가 돼!
    - none : 눈에서 보이지 않게 할 수 있는데 hidden이랑 비슷해. <code>차이점은?</code>none은 렌더링시 아예 그리질 않아. but hidden은 자리는 차지하지만 눈에만 보이지 않아! 레이아웃에서 베재하는지, 안하는지!
2. <code>float</code> : 영단어 뜻대로 붕붕 띄울 수 있어. left나 right요소를 줄 수 있어. 현대에는 <code>flex박스</code>가 등장해서 많이 사용되지 않아. 갈 수 있는 최대한의 left,right로 이동해
3. <code>position</code> : 계산 법칙만 이해하면 어렵지 않게 이해할 수 있어-<code>Normal Flow</code>
    - static : 기본값! top,bottom,right,left를 쓸 수 없어!!❌❌
    - relative : 자기 자신을 기준으로! t,b,r,l를 줄 수 있어(마치 margin을 준것처럼) 하지만 margin이랑 다르게 아래애는 그대로 있어서 그 애를 덮을 수 도 있어. 반대값을 쓰면 top과 left가 우선시 돼
    - absolute : 그 자리에서 붕 뜬것처럼 보여. float 자기자리처럼 보여! t,b,r,l을 하면 자기 조상중에 <code>position이 static이 아닌❌❌</code> 조상을 기준으로 이동을 해
    - fixed : 뷰포트를 기준으로 삼는다! 그래서 스크롤을 한다 하더라도 그 위치에 존재해
    - sticky : Normal-Flow대로 진행하다가, 어느 시점에 도달하면 스티커처럼 fixed로 고정 돼. <code>스크롤이 지나갔을 때</code> fixed처럼 동작시키게 하고싶을때 사용 돼. <code>스크롤 되는 조상-body의 직계 자손에 요소를 추가해야 동작이 돼</code>
4. <code>overflow</code> : 내부 컨텐츠가 넘쳐흐를때 -> 스크롤이 생기는거를 없애거나 넘친 텍스트를 없애거나! scroll을 생기게 하던가! auto하던가!
5. <code>z-index</code> : z축에 순서를 지정한다! 값이 높을수록 우선순위가 높아! 높을수록 눈앞에 가까워지는거지! 혹은 position값을 지정해서 더 위에 뜨게 할 수 있어!

# 색상

1. <code>rgba, opacity</code> rgba는 배경요소에만 영향을 주고, opacity는 안의 children요소를 포함한 내부 전체의 투명도를 조정해
2. <code>background-image</code> : background-color보다 위서 생성 돼. 이미지를 넣으려면 url이라는 함수 표기법을 사용해 ex) url("../..") 사이즈가 다르면 기본적으로 바둑판 형식으로 여러 이미지로 크기를 채워!
3. <code>background-repeat</code> : 바둑판식으로 넘처흐르는 사진들을 제어해! 기본값은 바둑판이니까 repeat이고, x에 하거 싶으면 repeat-x, 반복 안하고싶으면 no-repeat인데 크기는 차지하고, 이미지는 자기 크기만큼만 갖어
4. <code>background-position</code> : no-repeat일때 이미지를 관리하는 방법. 
    - x축값, y축값을 입력받아서 좌슥 상단 꼭지점에서 위치를 지정해. 
    - 키워드로 top, right, bottom, left, center를 쓸 수 있어
5. <code>background-origin</code> : border/padding/content-box로 지정할 수 있어. 각 지정 값을 기준으로 상대적으로 배치할 수 있어.  <code>원점을 어떻게 할지</code>결정해줄수 있는 요소!
    - content-box : 선언한 크기의 좌측 상단이 background의 시작점이 돼
    - padding-box : 패딩의 좌측 상단부분이 background의 시작점이 돼 (default값임)
    - border-box : 보더 박스의 좌측 상단부분이 // (같은 말)
6. <code>background-size</code> 처음 2개는 이미지의 비율을 지켜
    - cover : 이미지가 찌그러지지 않는 한도내에서 가장 크게 꽉 차게 맞춤
    - contain : 이미지가 전부 나올 수 있도록 만들어줘. 빈공간이 생김 
    - length값,px값 : 크기가 고정이 돼. 가령 100px * 100px의 이미지가 나타남(비율 지키지 않음), 대신 값을 하나만 입력하면 width값에 맞춰서 비율이 늘어난다. 가로비율만 맟줘
7. <code>short hand!</code> : background단축속성으로 한번에 선언할 수 있어
    - background : red url('../../..') no-repeat

# transform

크게만들거나, 작게만들고, 돌리거나 이동시킬 수 있어
1. <code>scale</code> : 2D만을 위한 함수. sale(0.5)라고 해도 원래 공간은 갖는데 그 안에서 사이즈가 절반으로 줄여서 width를 반으로 줄이는거랑은 다른거다.
2. <code>rotate</code> : 단위로 deg, rad, turn을 사용할 수 있어
3. <code>translate</code> : x축, y축으로의 이동 , 50%는 가로,세로의 비율을 따라간다
4. <code>skew</code> : 기울이다! x각도, y각도로 기울인것. 90도로 기울이면 사랴져
5. <code>transform-origin</code> : 기준점이나, 원점을 옮긴다. top left로 설정할수도 있고, px로 정할수도 있어!

# transition 

버튼을 올리면 시간차를 둬서 촤라락 변하도록 만들 수 있어! 그래서 시간과ㅏ 관련된 개념이 들어가! transform과 함께쓰면 엄청난 효과가❗❗ transition 관련 이벤트는 hover나 click같은 이벤트들이 있는데 해당 이벤트 안에 transition요소들을 넣게 되면 그 때만 효과가 넣어지고 <code>원래 요소안에</code> 넣게 되면 이벤트 발생, 해제시에도 같이 효과를 줄 수 있어!
1. <code>transition-delay</code> : 지연시키기? 시간 관련된 개념이 들어가! 아하! <code>이벤트가 발생된 후에</code> 이벤트가 진행되도록. 도미노같은 효과를 줄 수 있어. 요소들이 여러개 있을 때 파도치듯이 움직이게 할 수 있지!
2. <code>transition-duration</code> : 시간과 관련된 개념! s나 ms를 사용해!!<code>1s = 1000ms</code>
3. <code>transition-property</code> : 요소가 갖고있는 특정 property를 바꿔! margin이나 padding같은?! <code>none, all, margin ...</code>
4. <code>transition-timing-function</code> : 색이 바뀔때 색이 섞이게 되어있어! 그럴때 진행속도를 어떻게 하는가 <code>ease, linear, ease-out, ease-in..</code>어려워!
5. <code>transition(short hand!)</code> 순서가 중요해! 처음엔 변경할 요소-두번째부턴 시간 관련 요소. 시간은 2가지 있어서 하나라면 duration, 2개라면 앞이 duration-뒤가 delay! 

# animation

트렌지션과 같이 시간 개념이 들어가고 css가 변경 돼. 하지만 트렌지션은 유저의 이벤트가 발생해야지 같이 일어나는데 애니메이션은 자동으로 혼자 실행 가능햐!
1. <code>@keyframes</code> : @(at)이랑 같이 써서 시작해야햐. 작성법은 @keyframse 애니메이션이름작성 { ... }
 - <code>2개가 있을경우</code> from{} to{}를 사용해서 어떻게 변경할건지 작성해
 - <code>3개 이상이 있을 경우</code> %로 시간을 나눠서 0% ~ 100% 까지 작성해!
2. animation의 <code>short cut</code> : animation : 애니메이션이름-시간-infinite-alternate 등의 요소를 쓸 쑤 있어
    - ```animation-iteration-count``` : 1,2,3번으로 수를 지정할 수 있고, <code>infinite</code>를 주면 무한번 반복시킬 수 있어
    - ```animation-direction``` : normal, reverse, <code>alternate</code>:정방향으로갔다가 다시 돌아오는 애니메이션!, alternate-reverse:역방향으로 시작해서 다시 돌아오기!
    - ```animation-play-state``` : 애니메이션의 상태를 지정할 수 있어. paused, running으로 변경 가능해!

# Flexbox

레이아웃을 구성할 수 있게 해줘. felxible layout! 정렬하고 싶은 부모요소에 마법을 부린다.<br/>
용어 : flex container, flex item, main axis:메인축(가로), cross axis:교차축(세로)
- <code>컨테이너</code>에 사용하는것들 
    1. ```flex-direction``` : 컨테이너 내의 아이템들을 배치할 방향과 주축을 결정 : row, column
    2. ```flex-wrap``` : 무언가를 포장하는 느낌. 강제로 한줄로 배치되게 할것인지, 여러줄을 허용할것인지 정하는것 👉 어떻게? 자신의 크기를 보장해주는 wrap을 사용해서. wrap은 틀이야! 틀을 빵틀은 못줄여!
    3. <code>direction + wrap</code> : 오른쪽 밑에 위치시킬 수 있어. reverse속성 써서
    4. ```justify-content``` : 주축을 기준으로 아이템을 어떻게 배열할건지! 
    start, center, end, space-between/around,  flex-start(주축이 시작하는 위치에서부터 정렬) 때문에 ```flex-direction```을 알아야해!
    5. ```align-items``` : 교차축을 기준으로 아이템을 정렬해! flex-start, flex-end, center, stretch(기본값인데 시작에서 끝까지 연결돼 : ```교차축만큼```)
    또 얘는 아이템 ```한줄```의 속성을 주는거니까 space-between같은건 사용 못해!
    6. 한줄일때는 align-items, 여러줄일때는 ```align-content```를 써!
    flex-start면 교차축의 시작에 붙고, end면 끝에 붙고, center면 가운데에 붙어. 얘는 여러줄이니까 space-between 쓸 수 있음


- <code>아이템</code>에 사용하는 것들
    1. ``````order`````` : flex나 grid에서 순서를 지정할 수 있어(코드의 순서대로 말고) 음수값도 쓸 수 있어. 작을수록 왼쪽에(start)에 위치해. nth-child(3)를 써서 3번쨰 자식을 바꿔
    2. ``````flex-grow`````` : 배치를 한 다음에도 공간이 남을때 grow값을 1 주면 나머지 공간을 자기네들끼리 나눠갖음. grow의 값대로 각자 비율대로 갖게 돼. 늘리게 되기 전의 사이즈에 남은 사이즈를 1/n해서 가져가서 처음 ```크기가 다르면``` 후의 크기도 달라
    3. ``````flex-shrink`````` : grow는 늘어나지만 얘는 줄어들어. 1 값이 default
    4. ``````flex-basis`````` : 늘어나고 줄어드는 값을 조절할 수 있음. flex-grow의 처음 크기가 달랐던 문제를 해결. ```basis : 초기값``` 을 설정해서 모두 다 같은 사이즈로 설정할 수 있어. ```basis:0```으로 하면 크기가 변하기 전에 0의 사이즈를 줘서 변경크기는 동일한걸로 만들 수 있어
    5. ```short hand``` 👉 flex : grow, shrink, basis순서로 사용해!!
    하나 또는 2개의 값을 사용하면 basis는 default로 0값을 돼. px을 쓸 수 있어
    6. ``````align-self`````` : 얘는 ```각자의``` 위치를 정하는애. align-items는 각 줄의 위치를 어디다둘지 하는것. 그래서 nth-child(4) 같이 사용해서 그 애의 위치를 지정할 수 있어

# Grid

flex레이아웃이랑 비슷한 개념. flex는 주축에만 여러개의 아이템이 있을 수 있어. 교차축에 여러개의 아이템을 갖고싶으면 ```flex-wrap```의 속성을 변경해서 가로줄이 넘쳐났을 떄 다음줄에 넣어줄 수 있어. ```flex의 컨셉은 가로로의 배열을 위함```

grid는 flex랑 다르게 주축 뿐만아니라 교차축에 다 넣을 수 있어. flex는 1차원이라면, grid는 ```2차원```이다! 미리 테이블(컨테이너)을/를 만들어서 각 아이템을 순서대로 넣은거다! 따라서 행,열값이 존재 햐!

행과 열 사이의 공백은 ```gutters```라고 부른댜.
- ```grid``` : shorthand 👉 명시적인 요소(grid-template-rows/columns/areas), 암시적인 요소(grid-auto-rows/colums/flow) 값들을 한번에 사용할 수 있어. ```/```를 기준으로 앞은 row(행), 뒤쪽은 colums(열)에 관련된 요소를 설정하는거야. 

암시적인 요소는 요소의 이름을 사용해. auto-flow, dense 등등..

- 컨테이너 속성(부모)
    - ```display``` : grid / inline-grid도 가능햐
    - ```grid-template-columns``` : 1fr 1fr 1fr 👉 하나의 행을 1frame씩 3개로 나눠버린다.
    - ```grid-template-rows``` : 사용법이 위와 동일해.  👉여러개를 작성하고 싶으면 ```repeat이라는``` 함수 표기법을 작성 해. ```repeat(4,80px)``` : 80px를 4번 작성해라라는 뜻이야!
    - ```grid-template-areas``` : 땅따먹기하는것마냥 ```어디부터 어디까지 누구의 공간``` 을 선언할 수 있어. 
    ```
    "a a a"
    "b c c"
    "b c c"
    ```
    👉 1행 a 3개, 2행 b 1개, c 2개, 3행 b 1개, c 2개 를 갖는다. '.'을 사용하면 영역을 띄워줄 수 있어.
    - ```row-gap/column-gap``` : 행/열들간의 간격을 지정해. gutter값을 지정하는거겟지?
    - ```grid-auto-rows/columns``` : 정해진 템플릿의 개수보다 ```아이템이 많아질 경우``` 사이즈를 조절할 수 있는 기능. 100px라고 두면 명시적인 애들보다 넘친 애들은 100px의 사이즈를 갖도록 설정할 수 있어
    - ```grid-auto-flow``` : 아이템의 자리잡는 흐름. 주축으로 갈것인지, 교차축 방향으로 갈것인지. row, column으로 하고, ```dense로``` 설정할수도 있지. dense는 빈 영역을 다음애들로 채워줄 수 있어. 땡겨오는거야.
    - ```justify-content``` : flex에서는 주축을 기준으로 어디서 시작할건지에 관련한 배치 요소였어. Grid에서도 마찬가지야! start/end/center/space-around/between
    - ```align-content``` : 교차축을 기준으로 정렬하는 애야! 얘는 align-item은 없나봐!
    - ```justify-items``` : justify는 주축, align은 교차축이야! 뒤에 붙은 items랑 content의 차이는? content는 내부의 아이템을 여러개의 기준으로 정렬시키는거야. items는 하나의 아이템에 대한 속성을 정하는거지. ```justify-items```의 기본값은 stretch(갖을 수 있는 최대 너비, 높이를 갖는 거야). start나 end로 설정하게 되면 자기가 갖는 content의 길이만큼 너비를 갖고 높이는 stretch. 각각 아이템의 주축의 특성을 주고 싶으면 ```justify-self```키를 사용해서 값을 주면 돼
    - ```align-items``` : 교차축을 기준으로 item들의 위치를 정하는거지. 얘도 기본값은 stretch.

- 아이템 속성(자식)

    - ```grid-row``` : 단축속성이다! grid-row-start/end속성부터 이해해야햐!
    - ```grid-start``` : grid-row-start, grid-row-end : 만들어진 grid의 선에서 몇번째부타 시작해서 몇번째까지 차지할것인지 해 줘. start와 end를 슬레시(/)로 한번에 쓰는게 grid-row야! 어디서 시작하든지 시작하는곳에서부터 2칸만 차지하고 싶어 👉 grid-row : 2 / ```span 2``` : 2번째부터 시작해서 2칸을 차지하게 해
    - ```grid-area``` : 컨테이너에 쓰는 grid-template-areas로 각각의 영역을 이름으로 지정을 해줬었는데, 그 이름을 지정하는 키가 얘야. 또! grid-row, grid-column의 단축속성으로도 사용 가능해!
    - ```order``` : 순서 지정일까!? 그러하다!

- Grid의 단위
    - fr : fraction 👉 남은길이의 비율을 나눈거래. 절대길이와 같이 사용할 수 있어.
    - min/max-content : 내부에 있는 길이라는걸 알겠어. 내부에 있는 단어의 기준으로 가장 긴 애가 min. 최대한 줄일 수 있을떄까지 줄여. max는 늘릴 수 있을떄까지 계속 늘려! 
    - auto-fill, auto-fit : 반응형으로 grid를 사용할 때 사용된데. 길이를 절대길이로 설정한 후 화면을 늘리면 옆에 공백이 생기게 되는데 이때 사용되는게 auto-fill, auto-fit이래! ```repeat(auto-fill, 100px)``` 이면 컬럼의 길이가 남으면 알아서 들어가! 또 ```minmax(__,__)``` 함수를 통해서 최소값, 최대값을 지정할 수 있는데 이를 통해 repeat(auto-fill, minmax(100px,1fr)) 👉 최소는 100px, 최대는 1fr
    - auto-fit 은 남는공간을 꽉 채워줘. 남는공간이 생기면 유용해!