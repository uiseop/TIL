solution1 = (num) => {
    if(num < 6){
        if(num < 2) return false
        else return true
    }
    solution1(num%6) 
}

// 2번 pass

// 3번
const soulution3 = (num) => {
    if(Math.abs(num) > 100000){
        return 0
    }
    let str_num = (num).toString()
    const reverse = (n) => {
        let result = ''
        for(let i=n.length-1;i>=0;i--){
            result += n[i]
        }
        return result
    }
    if(str_num[0] === '-'){
        str_num = str_num.slice(1)
        let result = '-' + reverse(str_num)
        console.log(result);
        return result
    }
    else{
        let result = reverse(str_num)
        console.log(result);
        return result
    }

}

// 4번 .....snowball.....
const solution4 = (n,s,t) => {
    let neon = ''
    for(let i=0; i<n; i++){
        neon += '.'
    }
    neon += s
    for(let i=0; i<n; i++){
        neon += '.'
    }

}

// 5번

const sol5 = (s) => {
    let arr = s.split(/[\.\,\!\?\s]/)
    const reverse = (arr) => {
        let nArray = []
        for(let aid in arr){
            let result = ''
            for(let i=arr[aid].length-1; i>=0; i--){
                result += arr[aid][i]
            }
            if(result !== ''){
                nArray.push(result)
            }
        }
        return nArray
    }

    arr = reverse(arr)
    console.log(arr);
    return arr
}

sol5('Hello, World!?')