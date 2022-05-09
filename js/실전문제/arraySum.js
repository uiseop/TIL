/*
정수가 들어있는 배열 A가 주어질 때  연속 합이 가장 큰 수열의 합을 반환하는 함수를 작성하세요.
만약 가장큰 합이 음수인 경우에는 0으로 반환하세요.

예를들어 배열 A에 [2, -8, 3, -2, 4, -10] 이 들어있는 경우 3 -2 4 를 선택했을 때 값이 5로 가장 큰 값이 나온다.
*/

const solution = (arr) => {
    const dp = [];
    arr.forEach((num, idx) => {
        if (idx === 0) {
            dp.push(num)
            return
        }
        num >= dp[idx-1] + num ? dp.push(num) : dp.push(dp[idx-1] + num)
        return
    })
    console.log(Math.max(...dp))
    return
}
solution([30, -10, 20, -50])