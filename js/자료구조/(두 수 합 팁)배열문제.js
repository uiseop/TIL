let input

// 배열안에 최소값의 위치를 모두 출력해라
const sol1 = (arr) => {
    let min = Math.min(...arr)
    let answer = []
    arr.map((num,index) => {
        if(num === min){
            answer.push(index)
        }
    })

    return answer
}

// input = [
//     [5,2,10,2],
//     [4,5,7,4,8],
//     [12,11,11,16,11,12]
// ]

const sol2 = (arr) => {
    let def = [1,1,2,2,2,8]
    return arr.map((num,index) => def[index] - num)
}

// input = [
//     [0,1,2,2,2,7],
//     [2,1,2,1,2,1],
//     [0,1,1,5,3,6]
// ]

const sol3 = (arr) => {
    arr.sort((x,y) => y-x)
    return [arr[0], arr[1]]
}

// input = [
//     [-11,5,18,-2,-3,6,4,17,10,9],
//     [3,7,-14,2,-6,13,-20,-2,-7,6,-17,-5,14,-9,19],
//     [-15,-4,-8,12,12,-8,-8,9,10,15,-2,10,-14,2,13,19,-9,14]
// ]

const sol4 = (arr) => {
    let tot = arr.reduce((acc,num) => acc + num, 0)
    tot -= 100

    let faker = []
    for(let i=0; i<arr.length; i++){
        for(let j=i+1; j<arr.length; j++){
            if(tot === arr[i] + arr[j]){
                faker = [arr[i],arr[j]]
            }
        }
    }

    return arr.filter(num =>
        num !== faker[0] && num !== faker[1]
    )

}

// input = [
//     [1,5,6,7,10,12,19,29,33],
//     [25,23,11,2,18,3,28,6,37],
//     [3,37,5,36,6,22,19,2,28]
// ]

const sol6 = (inp) => {
    let [arr,num] = inp
    // for(let i=0; i<arr.length; i++){
    //     for(let j=i+1; j<arr.length; j++){
    //         if(arr[i] + arr[j] === num){
    //             return [i,j]
    //         }
    //     }
    // }

    // ✅✅ 2중 for문을 사용하지 않고 구하는 방법
    // 👉 target 숫자와 현재 인덱스의 차이를 구해. key-value값의 Object 자료형에 모두 저장을 하고, 출력을 한다. 
    let map = {}
    for(let i = 0; i < arr.length; i++){
        if(map[num - arr[i]] !== undefined) return [map[num - arr[i]], i]
        else{
            map[arr[i]] = i
        }
    }
}

// input = [
//     [[2,7,11,15],9],
//     [[3,2,4],6],
//     [[3,3],6]
// ]

const sol7 = arr => {
    let res = 0
    let score = 0

    for(let i = 0; i<arr.length; i++){
        if(arr[i]){
            res += ++score
        }
        else score = 0
    }
    return res
    
}

// input = [
//     [1,0,1,1,1,0,1,1,0,0],
//     [1,1,0,1,1,0,1,1,1,1],
//     [1,1,1,1,1,0,0,1,1,0]
// ]

const sol8 = (nums) => {
    let map = new Map()
    let [frm, to] = nums
    for(let i=frm; i<=to; i++){
        let numbers = String(i).split('')
        numbers.forEach(n => {
            if(map.has(n))  map.set(n,map.get(n) + 1)
            else map.set(n,1)
        })
    }
    return [...new Map([...map.entries()].sort()).values()]
}

// input = [
//     [129, 137],
//     [1412,1918],
//     [4159,9182]
// ]

for(let idx in input){
    console.log(`${+idx+1} [${sol9(input[idx])}]`)
}