function Deque(array = []) {
    this.array = array;
}

Deque.prototype.getBuffer = function() {
    return this.array.slice();
}

Deque.prototype.isEmpty = function() {
    return this.array.length === 0;
}

Deque.prototype.pushFront = function(value) {
    this.array.unshift(value);
    return
}

Deque.prototype.pushBack = function(value) {
    this.array.push(value)
}

Deque.prototype.popFront = function() {
    return this.array.shift();
}

Deque.prototype.popBack = function() {
    return this.array.pop();
}