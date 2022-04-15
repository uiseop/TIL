const input = [
    [-11, 5, 18, -2, -3, 6, 4, 17, 10, 9],
    [3, 7, -14, 2, -6, 13, -20, -2, -7, 6, -17, -5, 14, -9, 19],
    [-15, -4, -8, 12, 12, -8, -8, 9, 10, 15, -2, 10, -14, 2, 13, 19, -9, 3, -18, 14]
]

function answer(nums) {
    nums.sort((x,y) => y-x);
    return [nums[0], nums[1]]
}

for (let arr of input) {
    console.log(answer(arr));
}