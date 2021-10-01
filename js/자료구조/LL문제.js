// let input = [
//     [4,7,1,10,6],
//     [3,10,6,8,11,3,4],
//     [6,7,8,3,2,1,21,6]
// ]

const sol1 = arr => {
    let result = arr.map(num => `${num} -> `).join('') + 'null'
    return result
}

function Node(data){
    this.data = data
    this.next = null
}

function LL(){
    this.head = null
}

// for(let arr of input){
//     console.log(`${sol1(arr)}`);
// }

const sol2 = str => {
    str = str.split(/\s->\s/).filter(w => !isNaN(w))
    console.log(str);
    
}

// let input = [
//     '1 -> 3 -> 7 -> null',
//     '3 -> 1 -> 9 -> 6 -> 4 -> null',
//     '6 -> 9 -> 7 -> 2 -> 1 -> 4 -> 3 -> null'
// ]

// for(let str of input){
//     console.log(`${sol2(str)}`);
// }

let input = [
    [8,2,3],
    [10,2,3],
    [20,5,7],
]

function Node(data){
    this.data = data
    this.next = null
}

function LL(){
    this.head = null
    this.length = 0
}

CLL.prototype.append = function(data){
    let node = new Node(data)
    if(this.head === null){
        this.head = node
        this.next = node
    }
    else{
        let current = this.head
        while(current.next !== this.head){
            current = current.next
        }
        current.next = node
        node.next = this.head
    }
    this.length += 1
}

CLL.prototype.delete = function(data){
    let current = this.head, prev
    while(current.data !== data){
        prev = current
        current = current.next
    }
    prev.next = current.next
    this.length -= 1
}

CLL.prototype.printNode = function(){
    let current = this.head
    while(current.next != this.head){
        process.stdout.write(`${current.data} -> `)
    }
    console.log(`${current.data}`);
}

const sol3 = (num,start,step) => {
    let cll = new CLL()
    for(let i=1; i<=num; i++){
        cll.append(i)
    }

    cll.printNode()
}

for(let arr of input){
    console.log(`${sol3(arr[0], arr[1], arr[2])}`);
}