/*
임의의 두 수의 최대 공약수를 구한다.
평범한 풀이 -> 2부터 해당 수까지 for문을 돌리고 while을 써서 나머지가 0이면 나눔 => 그렇게 해서 모인 소인수들을 비교해서 개수를 셈

유클리드 호제법

- 임의의 두 자연수 a, b가 주어졌을때. 둘중 큰 값이 a라고 가정해보겠습니다.
- a를 b로 나눈 나머지를 n 이라고 하면 (a%b = n)
- n이 0일때, b가 최대 공약수(GCD)입니다.
- 만약 n이 0이 아니라면, a에 b값을 다시 넣고 n를 b에 대입 한 후 다시 위에 step2부터 반복하면 됩니다.

*/

const solution = (nums) => {
    let [num1, num2] = nums;
    let n = num1 % num2;
    while (n !== 0) {
        num1 = num2;
        num2 = n;
        n = num1 % num2;
    }
    console.log(num2)
    return num2;
}

solution([888, 220])