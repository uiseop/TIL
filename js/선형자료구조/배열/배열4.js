const input = [
    [1,5,6,7,10,12,19,29,33],
    [25,23,11,2,18,3,28,6,37],
    [3,37,5,36,6,22,19,2,28]
]

function answer(nums) {
    const diff = nums.reduce((t,n) => t+n, 0) - 100;
    for(let i=0; i<nums.length; i++) {
        for(let j=i+1; j<nums.length; j++) {
            if (diff === nums[i] + nums[j]) {
                nums.splice(i,1);
                nums.splice(j-1,1);
                break;
            }
        }
    }
    return nums
}

for(let arr of input){
    console.log(answer(arr));
}