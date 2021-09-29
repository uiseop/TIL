// 재귀로 등차수열 만들기

const recursion = (num,step,idx) => {
    if(idx === 1){
        return num
    }
    else{
        // console.log(num)
        // return recursion(num+step,step,idx-1)
        return recursion(num,step,idx-1) + step // 강의에서 진행된 방법. num을 보존한 상태에서 step을 계속 더해가는 방식
    }
}

// let result = recursion(3,2,5)
// console.log(result);

const fibonaci = (number) => {
    if(number === 1 || number === 0) return number
    // 피보나치는 f(n) = f(n-1) + f(n-2) 의 점화식을 갖으니까 return값을 그대로 사용해!
    return fibonaci(number-1) + fibonaci(number-2)
}

let result = fibonaci(10)
console.log(result);