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
    while (this.parent(idx) && this.parent[1] > w) {
        let pid = this.parentIndex(idx);
        this.swap(idx, pid);
        idx = pid;
    }
}

PrioQ.prototype.heappop = function () {
    let idx = 0;
    this.swap(idx, this.items.length - 1);
    const result = this.items.pop();
    const w = this.items[0][1]
    while ((this.leftChild(idx) && this.leftChild[1] < w) || (this.rightChild(idx) && this.rightChild(idx)[1] < w)) {
        let cid = this.leftChildIndex(idx);
        if (this.rightChild(idx) && this.rightChild(idx)[1] < w) {
            cid = this.rightChildIndex(idx);
        }
        this.swap(idx, cid);
        idx = cid;
    }
    return result;
}