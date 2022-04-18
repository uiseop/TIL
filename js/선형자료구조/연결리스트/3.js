// 원형 연결 리스트 문제. 대표자 선출

const input = [
    [8, 2, 3],
    [10, 2, 3],
    [20, 5, 7],
];

function Candidate(num) {
    this.num = num;
    this.next = null;
}

function CircularLinkedList() {
    this.head = null;
}


function answer([n, m, k]) {
    let cll = new CircularLinkedList();
    let current, prev;
    let result = [];

    for (let i = 1; i <= n; i++) {
        current = new Candidate(i);

        if (i == 1) {
            cll.head = current;
        } else {
            prev.next = current;
        }

        prev = current;
    }
    current.next = cll.head; // 원형 연결리스트의 tail의 next는 head

    while (m) {
        console.log(m)
        m -= 1;
        // 원점을 m만큼 이동해서 고정
        prev = current;
        current = current.next;
    }

    while (current !== current.next) {
        result.push(current.num);
        prev.next = current.next;

        count = k;
        while (count--) {
            prev = current;
            current = current.next;
        }
    }

    result.push(current.num);

    return result;
}

for (let arr of input) {
    console.log(answer(arr));
}
