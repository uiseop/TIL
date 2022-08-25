function Heap() {
    this.items = [];
}

Heap.prototype.swap = function (idx1, idx2) {
    const temp = this.items[idx1];
    this.items[idx1] = this.items[idx2];
    this.items[idx2] = temp;
};

Heap.prototype.getParentIndex = function (idx) {
    return Math.floor((idx - 1) / 2);
};

Heap.prototype.getParent = function (idx) {
    return this.items[this.getParentIndex(idx)];
};

Heap.prototype.heappush = function (val) {
    let idx = this.items.length;
    this.items.push(val);
    while (this.getParent(idx) && this.getParent(idx) > val) {
        this.swap(this.getParentIndex(idx), idx);
        idx = this.getParentIndex(idx);
    }
};

Heap.prototype.leftChild = function (idx) {
    return this.items[this.leftChildIndex(idx)];
};

Heap.prototype.rightChild = function (idx) {
    return this.items[this.rightChildIndx(idx)];
};

Heap.prototype.leftChildIndex = function (idx) {
    return idx * 2 + 1;
};

Heap.prototype.rightChildIndx = function (idx) {
    return idx * 2 + 2;
};

Heap.prototype.heappop = function () {
    if (!this.items.length) return 'The heap is empty'
    this.swap(0, this.items.length - 1);
    const result = this.items.pop()
    let idx = 0;
    while (
        (this.leftChild(idx) && this.leftChild(idx) < this.items[idx]) ||
        this.rightChild(idx) < this.items[idx]
    ) {
        let childIndex = this.leftChildIndex(idx);
        if (this.rightChild(idx) < this.items[childIndex]) {
            childIndex = this.rightChildIndx(idx);
        }
        this.swap(idx, childIndex);
        idx = childIndex;
    }
    return result
};

const heap = new Heap();
heap.heappush(5);
heap.heappush(4);
heap.heappush(3);
heap.heappush(2);
heap.heappush(1);
heap.heappush(1);
heap.heappush(1);
heap.heappush(1);

console.log(heap.items);

console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())
console.log(heap.heappop())