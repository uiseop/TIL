function Stack(array = []){
    this.array = array
}

// getBuffer() : 객체 내 데이터 셋 반환
Stack.prototype.getBuffer = function(){
    return [...this.array]
}
// isEmpty() : 객체 내 데이터가 있는지 없는지
Stack.prototype.isEmpty = function(){
    return this.array.length === 0
}

// push() : 데이터 추가
Stack.prototype.push = function(item){
    this.array.push(item)
    return
}
// pop() : 데이터 삭제 - 출력
Stack.prototype.pop = function(){
    return this.array.pop()
}
// size() : array의 사이즈
Stack.prototype.size = function(){
    return this.array.length
}
// peek() : array의 끝 데이터 반환
Stack.prototype.peek = function(){
    return this.array[this.array.length-1]
}
// indexOf() : item의 인덱스를 반환
Stack.prototype.indexOf = function(item){
    for(let i in this.array){
        if(this.array[i] === item) return i
    }
    return -1
}
// includes() : item을 포함하고 있는지
// Stack.prototype.includes = function(item){

// }


let stack = new Stack()
stack.push(123)
stack.push(123)
stack.push(123)
console.log(stack.isEmpty());
console.log(stack.getBuffer())
console.log(stack.size());
