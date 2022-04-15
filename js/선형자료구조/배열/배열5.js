const input = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3,3], 6]
]

// function answer(nums, num) {
//     ans = [];
//     flag = false;
//     for(let i=0; i<nums.length; i++){
//         for(let j=i+1; j<nums.length; j++) {
//             if(num === nums[i] + nums[j]){
//                 ans.push(i);
//                 ans.push(j);
//                 flag = true
//                 break
//             }
//         }
//         if(flag) {
//             break;
//         }
//     }
//     return ans
// }
// flag를 사용한 break를 하지 않고 바로 return을 해도 돼.

function answer(nums, target) {
    const map = {};
    for(let i=0; i<nums.length; i++) {
        if(map[target - nums[i]] !== undefined) {
            return [map[target - nums[i]], i]
        }
        map[nums[i]] = i
    }
}

for(let [arr, num] of input) {
    console.log(answer(arr,num))
}