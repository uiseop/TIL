function sol1(x,y){
    let result = '';
    result = x>y?'>':x<y?'<':'='
    return result
}

// let input = [
//     [3,5],
//     [7,4],
//     [2,2]
// ]

// for(let [i,j] of input){
//     console.log(`#${i+1} ${sol1(i,j)}`)
// }

function sol2(x){
    let result = '';
    result = '*'.repeat(x)
    return result
}

// let input = [
//     5,7,12
// ]

// for(let i of input){
//     console.log(`#${i}개 ${sol2(i)}`);
// }

function sol3(x,y){
    let result = []
    if(x>y){
        for(let i=y; i<=x; i++){
            result.push(i)
        }
    }
    else if(x<y){
        for(let i=x; i<=y; i++){
            result.push(i)
        }
    }
    else{
        result.push(x)
    }
    return result;
}

// let input = [
//     [3,7],
//     [8,3],
//     [12,10]
// ]

// for(let i in input){
//     console.log(`#${+i+1} ${sol3(input[i][0], input[i][1])}`)
// }

function sol4(scores){
    let tot = 0;
    for(let score of scores){
        tot += score
    }
    return (tot/scores.length).toFixed(2)
}

// let input = [
//     [80,95,65,70,100],
//     [82,77,51,64,73,90,80],
//     [100,71,59,88,72,75,91,93]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol4(input[idx])}`)
// }

function sol5(counts){
    let max = Math.max(...counts)
    return counts.indexOf(max) + 1
}

// let input = [
//     [3,7,9,6,1],
//     [2,7,1,4,3,0,5],
//     [7,5,0,1,2,12,6]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol5(input[idx])}`)
// }

function sol6(array){
    console.log(typeof array)
    console.log(array)
    // let len = array.length
    // let head = array[len-2], tail = array[len-1]
    let [head,tail] = array.slice(-2)
    
    let num = head-tail
    if(num >= 0) return sol6(array.push(num))
    else return array
}

// let input = [
//     [9,3],
//     [6,3],
//     [13,7]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} [${sol6(input[idx])}]`)
// }


function sol7(nums){
    let result = ''
    let [a,b,c,d] = nums
    result = a/b > c/d ? 1 : a/b < c/d ? -1 : 0
    return result
}

// let input = [
//     [14,2,6,6],
//     [6,7,8,9],
//     [18,2,36,4]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol7(input[idx])}`)
// }

function sol8(year){
    if((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0){
        return true
    }
    else return false
}

// let input = [
//     4,100,124,247,400
// ]

// for(let year of input){
//     console.log(`#${input.indexOf(year)} ${sol8(year)}`)
// }

function sol9(arr){
    let [withdraw, tot] = arr
    if(withdraw % 5 !== 0) return tot
    if(withdraw + 0.5 > tot){
        return tot
    }
    else{
        return tot - (withdraw + 0.5)
    }
}

// let input = [
//     [40, 130.00],
//     [33, 130.00],
//     [300, 300.00]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol9(input[idx])}`)
// }

function sol10(arr){
    let [x,y] = arr
    let n_x = x.pop()
    let n_y = y.pop()
    if(x.includes(n_x)){
        for(let target of x){
            if(target !== n_x){
                n_x = target
                break
            }
        }
    }

    if(y.includes(n_y)){
        for(let target of y){
            if(target !== n_y){
                n_y = target
                break
            }
        }
    }

    return [n_x,n_y]
}

// input = [
//     [[5,5,8],[5,8,5]],
//     [[3,1,1],[2,1,2]],
//     [[7,7,3],[4,1,1]]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol10(input[idx])}`)
// }

function sol11(person){
    return person.height >= 150? true:false
}

// let input = [
//     {name:'john',age:27,height:181},
//     {name:'alice',age:12,height:148},
//     {name:'bob',age:14,height:156}
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol11(input[idx])}`)
// }

function sol12(time){
    let date = new Date(time)
    let day = date.getDay()
    switch(day){
        case 0:
            return '일요일'
        case 1:
            return '월요일'
        case 2:
            return '화요일'
        case 3:
            return '수요일'
        case 4:
            return '목요일'
        case 5:
            return '금요일'
        case 6:
            return '토요일'
    }
}

// let input = [
//     "2021-01-27",
//     "2021-02-27",
//     "2021-03-14",
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol12(input[idx])}`)
// }

function sol13(arr){
    let set = new Set(arr)
    return [...set]
}

// let input = [
//     ['john','alice','alice'],
//     ['Hello','hello','HELLO','hello'],
//     ['kiwi','banana','mango','kiwi','banana'],

// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol13(input[idx])}`)
// }

function sol14(arr){
    let result = arr.reduce((max,item) => {
        return max > item ? max : item
    })
    return result
}

// let input = [
//     [1,6,5,2,3],
//     [19,41,23,-4,17],
//     [-64,-27,-41,-33,-59]
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol14(input[idx])}`)
// }

function sol15(str){
    let reg = /^advert/ig
    if(reg.test(str)) return true
    else return false
}

// let input = [
//     'AdVert is good',
//     'RE:Request documnets',
//     '[Advertisement] free mobile!',
//     '50% off this week (advertising)'
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol15(input[idx])}`)
// }

function sol16(arr){
    let result = []
    for(let i = arr.length-1; i>=0; i--){
        result.push(arr[i])
    }
    return result
}
// reverse하는 다른 방법은 반으로 나눠서 양쪽 끝끼리 교체하는 식으로 해서 진행할 수 있어!
// let input = [
//     [1,2,3,4],
//     [-1,6,'hello',-15],
//     ['apple','banana','mango']
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol16(input[idx])}`)
// }

function sol17(str){
    str = str.split(/\s/)
    let result = []
    for(let word of str){
        let toUpper = word[0].toUpperCase() + word.slice(1)
        result.push(toUpper)
    }
    return result.join(' ')
}

// let input = [
//     'Hello, My name is john',
//     'This week is closed due to COVID-19',
//     'fifty percent off this week'
// ]

// for(let idx in input){
//     console.log(`#${+idx+1} ${sol17(input[idx])}`)
// }

function sol18(arr){
    let tot = 1;
    for(let sub_arr of arr){
        for(let num of sub_arr){
            tot *= num
        }
    }
    return tot

}

let input = [
    [[1],[2],[3]],
    [
        [1,2],
        [3,4],
        [5,6,7],
    ],
    [
        [5,1],
        [0.2,4,0.5],
        [3,9],
    ]
]

for(let idx in input){
    console.log(`#${+idx+1} ${sol18(input[idx])}`)
}