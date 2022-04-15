const input = [
    [1,0,1,1,1,0,1,1,0,0],
    [1,1,0,1,1,0,1,1,1,1],
    [1,1,1,1,1,0,0,1,1,0],
]

function answer(nums) {
    let points = 0;
    let score = 0;
    for (let i=0; i<nums.length; i++) {
        if(nums[i]) {
            points += ++score;
        } else {
            score = 0
        }
    }
    return points
}

for(let arr of input) {
    console.log(answer(arr));
}