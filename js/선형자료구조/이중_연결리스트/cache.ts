interface INode {
    value: string;
    pre: INode | null;
    next: INode | null;
}

function C_node(value: string) {
    this.value = value;
    this.pre = null;
    this.next = null;
}

function Double_linked_list() {
    this.head = null;
    this.tail = null;
    this.length = 0;
}

Double_linked_list.prototype.remove = function (node: INode) {
    if (this.length === 1) {
        this.head = null;
        this.tail = null;
        this.length = 0;
        return;
    }
    if (this.head === node) {
        this.head = node.next;
        this.length -= 1;
        return;
    }
    if (this.tail === node) {
        this.tail = node.pre;
        this.length -= 1;
        return;
    }
    (node.pre as INode).next = node.next as INode;
    (node.next as INode).pre = node.pre;
    return;
};

Double_linked_list.prototype.add = function (node: INode) {
    if (this.length === 0) {
        this.head = node;
        this.tail = node;
        this.length += 1;
        return;
    }
    this.tail.next = node;
    const pre = this.tail;
    this.tail = node;
    this.tail.pre = pre;
    this.length += 1;
};

function solution(cacheSize: Number, cities: string[]) {
    var answer = 0;
    const llist = new Double_linked_list();
    const node_obj = new Map<string, INode>();

    for (let city of cities) {
        city = city.toLowerCase();
        if (node_obj.has(city)) {
            const node = node_obj.get(city);
            llist.remove(node);
            llist.add(node);
            answer += 1;
            continue;
        }
        if (node_obj.size < cacheSize) {
            const node = new C_node(city);
            node_obj.set(city, node);
            llist.add(node);
            answer += 5;
        } else if (cacheSize && node_obj.size === cacheSize) {
            // cacheSize가 0이 아닐 때
            const head = llist.head;
            llist.remove(head)
            node_obj.delete(head.value);
            const node = new C_node(city);
            node_obj.set(city, node);
            llist.add(node);
            answer += 5;
        } else {
            answer += 5;
        }
    }
    console.log(answer);
    return answer;
}

solution(3, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
    "Jeju",
    "Pangyo",
    "Seoul",
]);
