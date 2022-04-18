const input = [
    [10, 3, 7, 4, 12, 2],
    [7, 4, 12, 1, 13, 11, 12, 6],
    [20, 1, 19, 18, 15, 4, 6, 8, 3, 3],
];

function answer(arr) {
    let count = 0;
    arr.push(Number.MAX_SAFE_INTEGER);

    const stack = [];
    for (let i = 0; i < arr.length; i++) {
        if (stack.length === 0) {
            stack.push({ idx: i, h: arr[i] });
        } else {
            while (stack.length && stack[stack.length - 1]["h"] < arr[i]) {
                let { idx } = stack.pop();
                count += i - idx - 1;
            }
            stack.push({ idx: i, h: arr[i] });
        }
    }
    return count;
}

for (let arr of input) {
    console.log(answer(arr));
}

/* output
5
6
30

풀이 : 
스택을 사용하여 현재 인덱스, 높이를 저장하고 다음 기린의 높이가 더 크면 pop하는 형식.
더 크게 되면 더이상 볼 수 없기때문에 그 때까지 본 기린의 수를 확인해줘.
while문을 사용해서 모든 기린이 적용될 수 있도록 해준다.
*/