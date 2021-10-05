function Queue(q = []){
    this.queue = q
}

// getBuffer() : 큐 내에 데이터 셋 반환
Queue.prototype.getBuffer = function(){
    return [...this.queue]
    // return this.queue.slice()
}

// isEmpty() : 큐 내에 데이터 존재 여부 파악
Queue.prototype.isEmpty = function(){
    return this.queue.length === 0 ? true : false
}

// front() : 좌측 값
Queue.prototype.front = function(){
    return this.queue.length === 0 ? undefined : this.queue[0]
}

// size() : 데이터 개수
Queue.prototype.size = function(){
    return this.queue.length
}

// enqueue() : 데이터 추가 > 우측에다가
Queue.prototype.enqueue = function(value){
    return this.queue.push(value)
}

// dequeue() : 데이터 삭제 > 처음 값
Queue.prototype.dequeue = function(){
    return this.queue.shift()
}

// clear() : 큐 초기화
Queue.prototype.clear = function(){
    this.queue = [] // 재 할당을 통해 초기화
}