// Node라고 보자. data와 priority를 갖고 있지. priority를 기준으로 정렬을 하면 돼
function Element(data, priority){
    this.data = data
    this.priority = priority
}

function PriorityQueue(){
    this.array = []
}

// getBuffer : 데이터셋 반환
PriorityQueue.prototype.getBuffer = function(){
    return this.array.map((elem) => elem.data)
}

// isEmpty : 비어있는지
PriorityQueue.prototype.isEmpty = function(){
    return this.array.length === 0
}

// enqueue() : 데이터를 추가해
PriorityQueue.prototype.enqueue = function(data,priority){
    let elem = new Element(data,priority)
    let added = false
    // 같은 우선순위중 가장 마지막에 추가하는거네
    for(let idx in this.array){
        if(this.array[i].priority > elem.priority){
            this.array = this.array.splice(i,0,elem)
            added = true
            break
        }
    }
    if(!added) this.array.push(elem)

    return this.array.length
}


// dequeue() : 데이터를 삭제 해
PriorityQueue.prototype.dequeue = function(){
    return this.array.shift()
}

// front() : 가장 첫 데이터를 반환

PriorityQueue.prototype.front = function(){
    return this.array.length === 0 ? undefined : this.array[0].data // 0번째 인덱스의 data를 출력
}

PriorityQueue.prototype.clear = function(){
    this.array = []
}