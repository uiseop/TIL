# 메타데이터

<code>metadata</code>는 코드를 설명하기위한 데이터. 즉, html을 설명하는 데이터다.😱 <code>meta</code>태그 안에 문서의 설명을 넣어줘라. <code>name</code>과 <code>content</code> 쌍으로 작성하면 좋다야~SEO(검색엔진)의 추천을 잘 받을 수 있도록 꼼꼼하게 작성하는게 좋아<br>
<code>charset</code>속성👉인코딩하는 방식을 정해줘. <code>link</code>태그 : 현재 문서와 외부 리소스의 관계를 명시해. 보통 css나 js파일 연결하거나, 사이트의 파비콘 연결 등에 사용해 <code>rel</code>속성은 stylesheet를 가장 많이 사용해.(파비콘은 icon) <br>
<code>MIME</code>타입 : link한 파일의 확장자를 정의해주는것. 대분류/소분류 ```ex)text/html, image/gif, application/xml 등``` 찾아서 사용해!<br>
<code>data</code>속성 : data속성은 Javascript에서 사용할 정보들을 담는 공간인가봐🤔

# 텍스트 요소

1. <code>h</code>태그는 6개까지 있데 h1~h6
2. 인용태그, **blockquote** vs **q** :: 인라인 블록 : 인라인 인용문 공통점 : cite속성을 사용하여 url(출처)를 가져올수 있다.
blockquote는 들여쓰기로 작성되어있어 <code>p</code>태그 안에서 작성하면 안된다는군. blockquote가 시작되면 자동으로 <code>p</code>가 닫힌대.
(default)q는 자동으로 쌍따옴표가 들어가 있지 
3. <code>pre</code>태그 : 미리 서식을 지정한 텍스트를 나타내줌. spacing을 적용한만큼 다 적용 도ㅐ. 생긴 그대로가 완성본. 추가 <br>요소 필요하지 않아. 이모지 가죠올때 좋아 👇 figure로 blockquote랑 q태그를 한번에 설정해줄 수 있어 -> 문단의 설명
4. <code>figure</code> 태그 : 독립적인 콘텐츠를 표현한데 : 보통 위나 아래의 설명, 콘텐츠의 하나의 단위로 참조된데 (아예 사용하지않아도 뭐 상관 없음 - div대체) <code>figcaption</code>을 통해 해당 figure을 설명줄 수 있어
5. <code>abbr</code> 태그 : 문자의 약어를 표현 : 속성으로 title을 써서 원래 뜻을 알려주면 좋데
6. 주소나 웹메일 주소 등 <code>address</code> 태그를 사용한데. 이텔릭체로 디폴트로 적용되서 랜더링해주는듯
7. <code>bdo</code> 태그 : 택스트를 아랍어 형식으로 작성할 때 사용 (별로..)
8. <b>b 태그</b> : 택스트를 굵게 해주는 태그 : font-weight 주는것이지!
9. <code>mark 태그</code> : 하이라이터가 생기네. 형광펜 밑줄 쫙
10. <code>small 태그</code> : 작은글씨로 써져 쿠쿸
11. <sup>위로</sup><sub>아래로</sub> : sup,sub태그 지수 로그 표기할 때 쓰면 좋겠네 ex) log<sub>2</sub>2<sup>2</sup> = 2
12. <code>del</code> 태그, ins 태그 : <del>삭제될</del> 애들, <ins>추가될</ins> 애들 // 사용 할 수 있는 속성으론 cite:변경점 암시, datetime:변경 발생 일시
13. <code>code</code> 태그 : 짧으 코드 조각을 나타내는 스타일을 사용. p태그는 block요소인데 code태그는 inline요소래.span 이랑 비슷한데 코드를 나타낼때 사용
14. ⌨<kbd>키보드 태그</kbd> <code>kbd</code>태그⌨ : 키보드에 있는 Ctrl, Shift, R등등 그런애들을 inline요소에 적용함 // 사용량 많지 않아
15. <code>a</code>태그 : 앵커Anchor : 닻의 줄인말이래 mailto속성 -> href="mailto:이메일주소", tel속성 👉 href="tel:전화번호"
<code>target</code>속성 -> 링크한 URL을 표시할 위치. 가능한 값은 브라우징 맥락으로, 즉 탭, 창, iframe의 이름이나 특정 키워드입니다. _blank 값을 많이 쓴다는데 default로 새탭에서 열린데 👉 ```<a href="/www.naver.com" target="_blank">네이버</a>```

16. Entity : html코드안에 특수문자를 사용하고 싶으면 &+lt+;, &+gt+;, 등등 사용하면 돼! ```w3c entity```에서 그때그때 찾아보면서 사용해도 될듯햐!

# 구조 요소

1. 의미가 없는 <code>div</code>태그 : 구획을 나누거나 단순 스타일링의 목적으로 많이 사용하지 class로 구획을 딱딱 나눠. 태그상 의미가 없을떄 얘를 사용하고 의미가 있는 article,nav등엔 적절하지 않다! div vs span : div : block, 길이는 부모의 요소, span : inline 길이는 children의 요소
2. **Semantic Web**(의미의,의미론적인 Web)의 이점 / 의미론적인 마크업 사용의 이점
 - 검색 엔진은 의미론적 마크업을 분석해서 페이지의 검색 랭킹에 영향을 준다고 해! 의미있는것이 많으면 검색엔진에 많이 노출된대!!
 - 의미가 없는 끊임없는 <code>div</code>들을 탐색하는 것보다, 의미있는 코드 블록을 찾는 것이 훨씬 쉬움 👉 한눈에 보기 편하다!
 - 개발자에게 태그 안에 채워질 데이터 유형을 제안 👉 협업시 유용하도록!
 - 의미있는 이름짓기는 적절한 사용자 정의 요소 / 구성 요소의 이름짓기를 반영함
 - 시각 장애가 있는 사용자가 스크린리더로 페이지를 탐색할 때 의미론적 마크업을 푯말로 사용할 수 있음
3. <code>header</code>태그 : 소개 및 탐색에 도움을 주는 콘텐츠를 나타낸대. 제목, 로고, 검색 폼, 작성자 이름 등이 있지. header와 footer는 페이지에 하나만있쥐.
4. <code>nav</code>태그 : 네비게이션 영역, 내가 어디로 가야할지 알려주는 이정표 역할(탐색을 용이하도록해줘). 다른 페이지로의 링크, 현재 페이지의 링크
5. <code>aside</code>태그 : 보통 본문 옆의 사이드바에 들어갈 태그, nav랑 다른 점은 이 페이지 내의 부가적인 정보들을 넣는데 없어도 크게 문제가 되지 않을 정보들을 넣어줘
6. <code>main</code>태그 : 웹페이지 내에 오직 하나만 존재해야하고, 익스플로어에선 지원하지 않는데🤦‍♂️, 주요 콘텐츠의 컨테이너라고 생각!
7. <code>article</code>태그 : main태그 안에서 자주 보였던 애. **article** vs **section** 👉 aricle은 독립적으로 구분해 배포하거나 재사용 할 수 있는 구획(얘 하나만으로도 어떤내용인지 이해가 가능할 때! article!! 독립적으로는 맥락이 이해가 가지 않은 작은 부분, 그러나 문맥적인 의미가 있다면 section태그를 쓴데! ex)목차같은..? div랑 달라!)

# 목록과 표

1. <code>ol/ul</code> : Ordered/Un-Ordered List 정렬 표기법! <code>ol</code>의 속성중 <b>type</b>속성으로 숫자나, 영어, 그리스어로 표현 가능해. 그리고 <b>start</b>속성을 통해 시작하는 문자를 지정할 수 있어. 혹은 <code>li</code> 태그의 value값을 통해 시작 문자를 지정할 수 있어. reversed속성도있지
2. <code>dl</code> : dl태그는 설명 목록을 나타내고 2개의 자식 <code>dt</code>와 <code>dd</code>를 가져. term(용어)의 dt와 description(설명)의 dd.
정의목록을 나타낼때 알려줘. dt와 dd가 key/value처럼 짝으로 구성되어있어 dt를 dd가 설명해주는 구죠.
3. <code>table</code> : 얘전엔 테이블을 사용해서 레이아웃을 잡았던적이 있대. 지금은 flex나 grid를 사용해서 하기 때문에 table을 써서 만드는건 <strong>❌지.양❌</strong> 해야해. <code>th</code> : table head는 해당 열의 대표값으로 <code>scope</code>라는 속성을 갖고있어 행의값인지, 열의값인지 정해(시각적인 요소는 아냐!) 
 - <code>thead</code>, <code>tbody</code>, <code>tfoot</code>으로 마크업하여 항목을 나눌 수 있어(☝위에 말했던것처럼 레이아웃을 잡아)
 - <code>caption</code>태그 : 표를 설명할때 사용해. 표의 제목같은<strong>반드시 표(table) 요소의 첫번째 자식으로 넣어야해.</strong>

 # 임베디드 요소

1. **HTML에서 지원하는 이미지** : <code>JPEG</code>:현재 가장많이 사용되는데 압축이 기가맥힘, <code>PNG</code>:원본 이미지를 지캬줘-선명한 사진, <code>GIF</code>움짤, <code>WEBP</code>:구글이 만든 이미지 포맷인데 아직 호환성이 떨어져, <code>SVG</code>:아이콘에서 많이 봤지-벡터이미지래👉아무리 확대해도 이미지가 깨지지 않음
 - <code>img</code>태그의 srcset속성 : 반응형 이미지-사용자의 화면에 따른 다른 이미지를 보여주도록 서로 다른 이미지 크기를 넣어주는것. ```너비서술자 w 밀도서술자 x``` 가장 큰 사이즈를 받아오면 그 애로 계속 사용한데
 - <code>sizes</code>속성 : (min-width:100px) 100px 👉100px이상 크기의 화면이면 100px크기가 최대인걸로 보여라 라는 뜻으로 <a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element/img#attr-srcset">자세히</a> 에서 확인하자.😓
2. <code><a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video">video<a></code>태그 : (구글 - sample mp4 검색 다운로드) children요소는 <code>img</code>의 alt요소와 같은 기능을 해. 
 - <code>controls</code>속성을 통해 컨트롤러를 키거나 끌 수 있어. 
 - <code>autoplay</code>속성을 넣으면 들어오자마자 자동으로 실행해(단, 사운드가 있으면 실행되지 않으니 <code>mute</code>속성과 더불어서 사용하도록 하자.)
 - <code>poster</code>속성을 사용하면 섬네일로 사용할 이미지를 설정할 수 있어.
3. <code>audio</code>태그 : 대부분 video태그와 동일하게 사용 돼. 
4. <code>canvas</code>태그 : WebGL API랑 사용된데. html에서 마크업을 하고, 그림을 그리려면은 Javascript를 사용해야한대.
5. <code>iframe</code>태그 : inline frame요손데 다른 html페이지를 <code>src</code>태그로 구글맵같은걸로 불러온데(오호😮) <a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element/iframe">자세히</a>

# Form 사용법

<code>form</code>태그 : 자체로는 보여지는게 없고, <code>action</code>, <code>method</code>를 통해 HTTP통신을 하지 body의 내용은 <code>input</code>태그의 value들이 넘어가겠쥐

- <code>GET</code> : action으로 보내는 주소 뒤에 구구절절 query형식으로 어떤 데이터들이 입력됐는지 붙어서 들어가.❗보안에 위험이 있어👉들어나도 괜찮은 검색창에서 사용될 수 있겠지
- <code>POST</code> : 주소창에 내용이 들어나지 않아. 게시물 작성할때도 POST를 쓰지
- <code>input</code> : input태그는 <code>label</code>태그와 보통 세트로 움직여. 해당 input안에 뭘 입력해야할지 알려줘야하니까 이름 스티커를 붙여주는것. 어떤 input인지 구분자로써는 input의 <code>id</code>속성을 label의 <code>for</code>속성 안에 넣으면 돼.(Tip❗❗ label의 자식요소로 input을 넣으면 for, id값을 넣지 않아도 돼)
- <code>feildset</code> : feildset은 동일한 영역의 input들을 모아서 테두리로 감싸는 태그. 첫번째 태그로 <code>legend</code>태그를 사용해소 테이블의 <code>caption</code>태그와 같은 효과를 줄 수 있어. (Tip❗❗ 자손 태그들을 각각 disabled하지 않아도 한번에 disabled해줄 수 이썽!)

# input 사용법

- <code>input</code>태그는 속성이 매우 많아. 그 중 minlength와 maxlength를 통해 입력 개수를 조절할 수 있어 / 값으로 min과 max로 줄 수도 있지 <code>step</code>을 사용해서 증가하는 단위를 지정해줄수도 있다!
- <code>type</code>속성 <code>"number"</code>:숫자만 입력받아. <code>"range"</code>:막대그래프가나와. <code>date/month/time</code>년,월,일을 입력받아
    - <code>"checkbox"</code>이름그대로 체크박스. 체크를하고 submit하면 설정한 <code>name=on</code>으로 넘어가. <code>checked</code>는 default로 체크돼
    - <code>"radio"</code> radio는 <code>name</code>이 다르면 중복선택이 가능하고, 같으면 하나만 선택 가능해. 👉어떻게 확인하게? 각각value값으루. 왜why?넘어가는건 ❗<code>name과 value</code>❗니까
- <code>autocomplete</code> on과 off로 값을 줄 수 있는데 검색창에 검색했던 요소들이 나오는것과 같은 기능을 줄 수 있어
- <code>required</code>는 boolean태그로서 필수 입력값을 설정할 수 있어
- <code>readonly</code>는 boolean태그로서 넣어주면 변경이 불가능해져 default값으로 넣어지겠지?
- <code>list</code>는 select처럼 작동하는 input이야. list값엔 label처럼 <code>datalist</code>의 id값을 넣어주면 datalist안의 요소들이 drop-down 돼!
- <code>datalist</code>는 ☝input list="id"의 id에 연결돼서 보여주는 애들로 <code>select</code>처럼 option들을 넣어줘

<code>button</code>과 <code>input type="button"</code>의 차이점 : input은 value안에 값을 넣어야하기 때문에 문자열값만 사용할 수 있어. 하지만 button의 경우 children요소에 값을 넣기 떄문에 <strong>제출</strong>과 같이 format태그(이미지 등등..스타일 적용하기 수월해)로 꾸밀 수 있어.
<code>select</code> : select태그는 drop down요소인데 자식으로 <code>option</code>태그로 안에 후보군들을 추가해줄 수 있어. 필수값으로 넣으려면 ☝<code>required</code>속성 값을 추가시켜 주는데, default값으로 유효성검사를 하기 위해서는 value=''을 통해 빈값을 넣어 검사를 강제할 수 있어.
또, 기본값으로 설정하고싶으면 checkbox의 checked처럼 select태그는 <code>selected</code>로 쓰면 된대(..?!비슷해!😮)

 - drop down에서 또 한번 분류하고 싶어👉<code>optgroup</code>태그로 감싸서 카테고리별로 분류할 수 있어. 결과는 들여쓰기로 나와! 카테고리 명은 <code>optgroup</code>태그 안에 <code>label</code>속성을 통해 값을 넣어주면 돼!
<code>textarea</code>는 여러줄의 text를 입력을 받을 수 있게 해줘. rows,cols속성을 사용하면 보여주는 행,렬의 개수를 정해줄 수 있어

