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
}

let ll = new LinkedList()

ll.append(1)
ll.append(10)
ll.append(100)

ll.printNode()