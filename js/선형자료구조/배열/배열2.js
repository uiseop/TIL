const input = [
    [0,1,2,2,2,7],
    [2,1,2,1,2,1],
    [0,1,1,5,3,6],
]

const req = [1,1,1,2,2,8];

function answer(nums) {
    const ans = [];
    for(let i=0; i<req.length; i++) {
        if(nums[i] < req[i]){
            ans.push(req[i] - nums[i])
        } else {
            ans.push(0)
        }
    }
    return ans
}

for(let arr of input){
    console.log(answer(arr));
}