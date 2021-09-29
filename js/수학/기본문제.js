const sol1 = (start,step,num) => {
    // let nums = []
    // let idx = 1;
    // while(start <= num){
    //     if(start === num){
    //         return idx
    //     }
    //     else{
    //         start += step
    //         idx += 1
    //     }
    // }
    // return -1
    // 강의 풀이 : 숫자들의 차이가 step으로 나눠떨어지면 등차수열로 이뤄진것! 👍👍
    if((num-start) % step === 0){
        return 1 + (num-start)/step // O(1) 로 풀 수 있다! 등차수열은 아이템끼리 차이가 등차의 배수로 이뤄져있음!
    }
    else return -1
}

// let input = [
//     [1,2,7],
//     [2,3,10],
//     [3,5,23],
// ]

const sol2 = (a,b,c) => {
    let num = [a,b,c]
    num.sort((x,y) => x-y)
    let step = 0
    for(let i=1; i<num.length; i++){
        step += num[i] - num[i-1]
    }
    step /= 3

    let idx = num[2] - num[1] > num[1] - num[0] ? 2 : 1

    return num[0] + step*idx
}

let input = [
    [1,7,10],
    [3,8,18],
    [11,2,5]
]

for(let idx in input){
    console.log(`#${+idx+1} ${sol2(input[idx][0], input[idx][1], input[idx][2])}`)
}