const sol = str => {
    str = str.split('')
    let stack = []
    let result = []
    for(let i in str){
        if(str[i] === '(') {
            stack.push(i)
        }
        else if(str[i] === ')'){
            if(stack.length === 0) return [] // 추가조건
            result.push([stack.pop(), i])
        }
    }

    return result
}

console.log(sol('(a*(b+c)+d)'));