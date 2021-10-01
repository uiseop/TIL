function Node(data){
    this.data = data
    this.prev = null
    this.next = null
}
// ✅✅ 기존 LL는 노드를 추가할 때 끝의 index를 찾기 위해 O(n)이 걸렸는데
// DLL은 tail이라는 포인터가 있어서 O(1)만큼이 빠르다! `LL < DLL 좋다!`
function DLL(){
    this.head = null
    this.tail = null
    this.length = 0
}

// 노드 개수 👉 메서드 명은 size
DLL.prototype.size = function(){
    return this.length
}

DLL.prototype.isEmpty = function(){
    return this.length === 0 // 길이가 0인지 아닌지
}

// DLL 노드 전부 출력
DLL.prototype.printNode = function(){
    if(this.length === 0) return null
    let current = this.head
    process.stdout.write('head -> ')
    while(current !== null){
        process.stdout.write(`${current.data} -> `)
        current = current.next
    }
    console.log('tail // end')
}

// DLL 노드 전부 역출력
DLL.prototype.printReverse = function(){
    // 출력할값이 없음이
    if(this.length === 0) return null
    let current = this.tail
    process.stdout.write('tail -> ')
    while(current !== this.head){
        process.stdout.write(`${current.data} -> `)
        current = current.prev
    }
    console.log(`${current.data} -> head // end`)
}

DLL.prototype.append = function(data){
    let node = new Node(data)
    if(this.length === 0){
        this.head = node
        this.tail = node
        // head이자 tail은 노드
    }
    else{
        let last_node = this.tail
        last_node.next = node
        node.prev = last_node
        this.tail = node
    }
    this.length += 1
}

DLL.prototype.appendAt = function(idx,data){
    // 터무늬없는 위치는 안돼
    if(idx < 0 || idx > this.length) return false
    let current = this.head, index = 0
    let node = new Node(data)
    while(index !== idx){
        index += 1
        current = current.next
    }
    let prev = current.prev
    prev.next = node
    node.prev = prev

    node.next = current
    current.prev = node

}

DLL.prototype.remove = function(data){
    if(this.length === 0) return null
    let current = this.head
    while(current !== null){
        if(current.data === data){
            let next = current.next
            current.prev.next = next
            next.prev = current.prev
            this.length -= 1
            return current
        }
        current = current.next
    }
    return null
}

let dll = new DLL()

dll.append(1)
dll.append(10)
dll.append(100)

dll.printNode()
dll.printReverse()

dll.remove(10)

dll.printNode()
console.log(dll.remove(10))