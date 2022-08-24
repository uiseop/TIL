function Heap() {
    this.items = [];
}

Heap.prototype.swap = function (index1, index2) {
    const temp = this.items[index1];
    this.items[index1] = this.items[index2];
    this.items[index2] = temp;
};

// 0 - 1,2 - 3,4/5,6 - ... 3,4의 parent는 1, 5,6의 parent는 2 => (idx - 1) // 2

Heap.prototype.parentIndex = function (index) {
    return Math.floor((index - 1) / 2);
};

// 1의 leftChild는 3, 2의 leftChild는 5 => (idx*2) + 1

Heap.prototype.leftChildIndex = function (index) {
    return index * 2 + 1;
};

Heap.prototype.rightChildIndex = function (index) {
    return index * 2 + 2;
};

Heap.prototype.parent = function (index) {
    return this.items[this.parentIndex(index)];
};

Heap.prototype.leftChild = function (index) {
    return this.items[this.leftChildIndex(index)];
};

Heap.prototype.rightChild = function (index) {
    return this.items[this.rightChildIndex(index)];
};

Heap.prototype.peek = function () {
    return this.items[0];
};

Heap.prototype.size = function () {
    return this.items.length;
};

// 추가 -> 마지막 Level의 왼쪽부터 추가하게 되는데 동시에 parent와 비교하면서 swap을 수행.

Heap.prototype.heappush = function (value) {
    let idx = this.size();
    this.items.push(value);
    while (this.parent(idx) && value < this.parent(idx)) {
        this.swap(idx, this.parentIndex(idx));
        idx = this.parentIndex(idx);
    }
}

Heap.prototype.heappop = function() {
    const value = this.items[this.size() - 1];
    this.swap(this.size() - 1, 0);
    this.items.pop();
    let idx = 0;
    while (this.leftChild(idx) && (this.leftChild(idx) < value) || (this.rightChild(idx) < value)) {
        let childIndex = this.leftChildIndex(idx);
        if (this.rightChild(idx) && this.rightChild(idx) < this.items[childIndex]) {
            childIndex = this.rightChildIndex(idx);
        }
        this.swap(idx, childIndex);
        idx = childIndex;
    }
}

const minHeap = new Heap();
minHeap.heappush(90)
minHeap.heappush(15)
minHeap.heappush(10)
minHeap.heappush(7)
minHeap.heappush(12)
minHeap.heappush(2)
minHeap.heappush(8)
minHeap.heappush(3)

console.log(minHeap)