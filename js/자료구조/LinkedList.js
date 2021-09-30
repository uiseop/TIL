// Node : 데이터와 포인터를 가지고 있는 객체. 포인터는 초기화! null로
function Node(data){
    this.data = data
    this.next = null
}

function LinkedList(){
    this.head = null
    this.length = 0
}

LinkedList.prototype.size = function (){
    return this.length
}

LinkedList.prototype.isEmpty = function (){
    return this.length === 0
}

LinkedList.prototype.printNode = function (){
    for(let node=this.head; node != null; node = node.next){
        // process.stdout.write는 한줄에 작성하는 권법이네
        // console.log는 자동 줄바꿈이 들어가있는데
        process.stdout.write(`${node.data} -> `)
    }
    console.log('null');
}
// 노드 추가
LinkedList.prototype.append = function (value) {
    let node = new Node(value), current = this.head

    if(this.head === null) this.head = node
    else{
        // 가장 끝으로 이동 👉 O(n)만큼 걸리겠지
        while(current.next != null){
            current = current.next
        }
        current.next = node
    }

    this.length += 1
}
// 원하는 위치에 노드 추가
LinkedList.prototype.insert = function (value,idx=0){
    // 기저조건 : 말도안되는 위치(음수 or 길이보다 큰 수)
    if(idx < 0 || idx > this.length) return false

    let node = new Node(value), current = this.head, index = 0, prev

    if(idx == 0){
        // 새로운 노드의 next를 이전의 head로
        node.next = current
        // 이 LinkedList의 head를 새로운 Node로
        this.head = node
    }
    else{
        while(index++ < idx){
            // 현재가 앞의 값
            prev = current
            // 다음이 현재 값
            current = current.next
        }
        prev.next = node
        node.next = current
    }

    this.length += 1

    return true
}

let ll = new LinkedList()

ll.append(1)
ll.append(10)
ll.append(100)

ll.printNode()

ll.insert(2,1)
ll.insert(3,3)

ll.printNode()
console.log(ll.size());