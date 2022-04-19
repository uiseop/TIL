const input = [
    [[3], 0],
    [[3,4,5,6], 2],
    [[1,1,5,1,1,1], 0]
]

function answer(arr) {
    let [prio, n] = arr;
    // 높은 숫자가 우선순위 최상
    // 항상 Max값을 알아야한다. 
    let cnt = 1;
    while (prio.length !== 0) {
        let max = Math.max(...prio);
        if (max === prio[0]) {
            if (n === 0) {
                return cnt;
            }
            cnt += 1
            prio.shift();
            n > 0 ? n -= 1 : n = prio.length - 1;
        } else {
            prio.push(prio.shift());
            n > 0 ? n -= 1 : n = prio.length - 1;
        }
    }
}

for (let arr of input) {
    console.log(answer(arr));
}