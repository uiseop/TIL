function CircularQueue(array = [], size = 5){
    this.array = array
    this.size = array.length > size ? array.length : size
    // 길이
    this.length = array.length
    this.head = 0
    // 꼬리는 길이에 위치
    this.tail = array.length
}

CircularQueue.prototype.getBuffer = function(){
    return this.array.slice()
}

CircularQueue.prototype.isEmpty = function(){
    return this.length === 0
}

CircularQueue.prototype.isFull = function(){
    // size는 총 용량, length는 현지
    return this.length === this.size
}

CircularQueue.prototype.enqueue = function(value){
    if(this.isFull) return false

    this.array[this.tail % this.size]
    this.tail += 1
    this.length += 1

    return true
}

CircularQueue.prototype.dequeue = function(){
    if(this.isEmpty) return undefined
    // 계속 돌게되면서 head가 size보다 커질 수 있는것을 방지
    let pop = this.array[this.head % this.size]
    this.head += 1
    this.length -= 1

    return pop
}