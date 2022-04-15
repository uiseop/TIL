const input = [
    [5,2,10,2],
    [4,5,7,4,8],
    [12,11,11,16,11,12]
]

function answer(nums) {
    const min = Math.min(...nums);
    const ans = [];
    for(let i=0; i<nums.length; i++) {
        if (nums[i] === min) {
            ans.push(i);
        }
    }
    return ans;
}

for(let arr of input) {
    console.log(answer(arr))
}