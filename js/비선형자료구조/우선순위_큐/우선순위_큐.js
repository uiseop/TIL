function Element(data, priortiy) {
    this.data = data;
    this.priortiy = priortiy;
}

function PriorityQueue() {
    this.array = [];
}

PriorityQueue.prototype.getBuffer = function () {
    return this.array.map((element) => element.data);
};

PriorityQueue.prototype.isEmpty = function () {
    return this.array.length === 0;
};

PriorityQueue.prototype.enqueue = function (data, priortiy) {
    let element = new Element(data, priortiy);
    let added = false;

    for (let i = 0; i < this.array.length; i++) {
        if (element.priortiy < this.array[i].priortiy) {
            this.array.splice(i, 0, element);
            added = true;
            break;
        }
    }

    if (!added) {
        this.array.push(element);
    }

    return this.array.length;
};

PriorityQueue.prototype.dequeue = function () {
    return this.array.shift(); // shift는 성능이 좋지 못하다.
};

PriorityQueue.prototype.front = function() {
    return this.array[0];
}

PriorityQueue.prototype.size = function() {
    return this.array.length;
}