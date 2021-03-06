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

const sol2 = input => {
    let result = []
    input.map(command => {
        command = command.split(' ')
        if(command.length == 2){
            result.push(command[1])
        }
        else{
            switch(command){
                case "dequeue":
                    if(result.length) return result.shift()
                    else return -1
                case "front":
                    if(result.length) return result[0]
                    else return -1
                case 'back':
                    if(result.length) return result[result.length-1]
                    else return -1
            }
        }
    })

    return result
}

// let input = [
//     ["enqueue 1", 'enqueue 2', 'dequeue', 'dequeue', 'dequeue'],
//     ['enqueue 3', 'enqueue 4', 'enqueue 5', 'enqueue 6', 'front', 'back', 'dequeue']
// ]

// for(let arr of input){
//     console.log(`${sol2(arr)} gogo`);
// }
