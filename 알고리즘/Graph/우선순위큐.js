function PrioQ() {
    this.items = [];
}

PrioQ.prototype.parentIndex = function(idx) {
    return Math.floor((idx-1)/2)
}

PrioQ.prototype.parent = function(idx) {
    return this.items[this.parentIndex(idx)]
}

PrioQ.prototype.swap = function (idx, pid) {
    const temp = this.items[pid];
    this.items[pid] = this.items[idx]
    this.items[idx] = temp;
}

PrioQ.prototype.heappush = function (v,w) {
    this.items.push([v,w]);
    let idx = this.items.length - 1;
    while (this.parent(idx) && this.parent(idx)[1] > w) {
        let pid = this.parentIndex(idx);
        this.swap(idx, pid);
        idx = pid;
    }
}

PrioQ.prototype.leftChild = function (idx) {
    return this.items[this.leftChildIndex(idx)]
}

PrioQ.prototype.leftChildIndex = function (idx) {
    return 2*idx+1;
}
PrioQ.prototype.rightChild = function (idx) {
    return this.items[this.rightChildIndex(idx)]
}

PrioQ.prototype.rightChildIndex = function (idx) {
    return 2*idx+2;
}

PrioQ.prototype.heappop = function () {
    if (this.items.length === 1) {
        return this.items.pop();
    }
    let idx = 0;
    this.swap(idx, this.items.length - 1);
    const result = this.items.pop();
    const w = this.items[0][1]
    while ((this.leftChild(idx) && this.leftChild(idx)[1] < w) || (this.rightChild(idx) && this.rightChild(idx)[1] < w)) {
        let cid = this.leftChildIndex(idx);
        if (this.rightChild(idx) && this.rightChild(idx)[1] < this.leftChild(idx)[1]) {
            cid = this.rightChildIndex(idx);
        }
        this.swap(idx, cid);
        idx = cid;
    }
    return result;
}