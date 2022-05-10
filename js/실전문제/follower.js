/* 
SNS에서 서로가 팔로우를 했다는 것을 '맞팔'이라고 표현합니다.
다음 팔로우 관계를 나타낸 배열을 통해 서로 맞팔 관계인 쌍의 수를 리턴하는 함수를 작성하세요.

이때 ["철수", "영희"] 라는 정보는 철수가 영희를 팔로우 했음을 나타냅니다.
*/

const solution = (arr) => {
    const map = new Map();
    let count = 0;
    arr.forEach(([follwee, follwer]) => {
        console.log(map.get(follwee), follwee)
        if (map.get(follwee)) {
            map.set(follwee, follwer);
            if (map.get(follwer) && map.get(follwer).indexOf(follwee)) {
                count += 1
            }
        } else {
            map.set(follwee, follwer)
        }
    })
    console.log(count)
    console.log(map)
    return
}

solution([["철수", "영희"], ["영희", "철수"], ["진수", "진호"], ["진호", "진수"]])