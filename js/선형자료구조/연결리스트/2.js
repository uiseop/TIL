function File(number) {
    this.number = number;
    this.next = null;
}

function LinkedList() {
    this.head = null;
}

function answer(ll) {


    return ll;
}

const input = [
    [7,3,1],
    [4,6,9,1,3],
    [3,4,1,2,7,9,6]
]

LinkedList.prototype.printNode = function() {
    for (let node=this.head; node !== null; node = node.next) {
        process.stdout.write(`${node.number} -> `)
    }
    console.log("null")
}

LinkedList.prototype.makeFiles = function (files) {
    let current = this.head;
    let node;

    for(let i=0; i<files.length; i++) {
        node = new File(files[i]);
        node.next = current; // null을 head로 받아. 역순이니까
        this.head = node; // 역순이니까 head를 변경

        current = node; // current는 이제 현재 head. prev를 지정
    }
}