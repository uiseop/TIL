# 태그 학습 노트 

1. h태그는 6개까지 있데 h1~h6
2. 인용태그, blockquote vs q :: 인라인 블록 : 인라인 인용문 공통점 : cite속성을 사용하여 url(출처)를 가져올수 있다.
blockquote는 들여쓰기로 작성되어있어 <p>태그 안에서 작성하면 안된데. blockquote가 시작되면 자동으로 <p>가 닫힌데
(default)q는 자동으로 쌍따옴표가 들어가 있지 
3. pre태그 : 미리 서식을 지정한 텍스트를 나타내줌. spacing을 적용한만큼 다 적용 도ㅐ. 생긴 그대로가 완성본. 추가 <br>요소 필요하지 않아. 이모지 가죠올때 좋아 👇 figure로 blockquote랑 q태그를 한번에 설정해줄 수 있어 -> 문단의 설명
4. figure 태그 : 독립적인 콘텐츠를 표현한데 : 보통 위나 아래의 설명, 콘텐츠의 하나의 단위로 참조된데 (아예 사용하지않아도 뭐 상관 없음 - div대체)
5. abbr 태그 : 문자의 약어를 표현 : 속성으로 title을 써서 원래 뜻을 알려주면 좋데
6. 주소나 웹메일 주소 등 address 태그를 사용한데. 이텔릭체로 디폴트로 적용되서 랜더링해주는듯
7. bdo 태그 : 택스트를 아랍어 형식으로 작성할 때 사용 (별로..)
8. <b>b 태그</b> : 택스트를 굵게 해주는 태그 : font-weight 주는것이지!
9. <mark>mark 태그</mark> : 하이라이터가 생기네. 형광펜 밑줄 쫙
10. <small>small 태그</small> : 작은글씨로 써져 쿠쿸
11. <sup>위로</sup><sub>아래로</sub> : sup,sub태그 지수 로그 표기할 때 쓰면 좋겠네 ex) log<sub>2</sub>2<sup>2</sup> = 2
12. del 태그, ins 태그 : <del>삭제될</del> 애들, <ins>추가될</ins> 애들 // 사용 할 수 있는 속성으론 cite:변경점 암시, datetime:변경 발생 일시
13. code 태그 : 짧으 코드 조각을 나타내는 스타일을 사용. p태그는 block요소인데 code태그는 inline요소래.span 이랑 비슷한데 코드를 나타낼때 사용
14. ⌨<kbd>키보드 태그</kbd> kbd태그⌨ : 키보드에 있는 Ctrl, Shift, R등등 그런애들을 inline요소에 적용함 // 사용량 많지 않아
15. a태그 : 앵커Anchor : 닻의 줄인말이래 mailto속성 -> href="mailto:이메일주소", tel속성 -> href="tel:전화번호"
target속성 -> 링크한 URL을 표시할 위치. 가능한 값은 브라우징 맥락으로, 즉 탭, 창, iframe의 이름이나 특정 키워드입니다. blank속성을 많이 쓴다는데 default로 새탭에서 열린데 ==> <code><a href="www.naver.com" target="_blank">네이버</a></code>