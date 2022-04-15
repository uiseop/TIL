const input = [
    [129, 137],
    [1412, 1918],
    [4159, 9182]
]

function answer(frm, to) {
    const nums = [0,0,0,0,0,0,0,0,0,0];
    for(let i=frm; i<=to; i++) {
        const div = i.toString().split('');
        for(let num of div) {
            num = Number(num);
            nums[num] += 1;
        }
    }
    return nums
}

for(let arr of input) {
    console.log(answer(arr[0], arr[1]));
}