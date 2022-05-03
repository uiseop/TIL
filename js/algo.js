

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function Queue(array) {
    this.array = array ? array : [];
    this.tail = 0;
    this.head = 0;
    this.length = 0;
}

Queue.prototype.enqueue = function (element) {
    this.length += 1
    return (this.array[this.tail++] = element)
}

Queue.prototype.dequeue = function() {
    if (this.isEmpty()) return undefined;
    const result = this.array[this.head];
    delete this.array[this.head];
    this.head += 1;
    this.length -= 1;

    return result;
}

Queue.prototype.isEmpty = function () {
    return this.head === this.tail;
}

function solution(S) {
    // write your code in JavaScript (Node.js 8.9.4)
    const q = new Queue();
    const result = [];
    for (let s of S) {
        if (q.isEmpty()) {
            q.enqueue(s);
        } else {
            if (q.array[q.tail - 1] === s && q.length < 2) {
                q.enqueue(s)
            } else if (q.array[q.tail - 1] !== s) {
                while(!q.isEmpty()) {
                    result.push(q.dequeue());
                }
                q.enqueue(s)
            }
        }
    }
    console.log(`result: ${result}`)
    console.log(`q: ${q}`)

    while (!q.isEmpty()) {
        result.push(q.dequeue())
    }
    
    return result.join("")
}

console.log(solution("eedaaad")) // 3번 이상 중복되지 않는 문자열 만들기 -> 왜 스택을 안썼는가

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N, K) {
    // write your code in JavaScript (Node.js 8.9.4)
    const nums = String(N).split("").map((num) => Number(num))
    let max_num = 0;
    for (let i=0; i<3; i++) {
        max_num += 9 - nums[i]
    }

    if (max_num <= K) {
        return 999;
    }
    let idx = 0;
    for (let i=0; i < K; i++) {
        // console.log(i, nums, idx)
        if (nums[idx] === 9) {
            idx += 1
            nums[idx] = nums[idx] + 1;
        } else {
            nums[idx] = nums[idx] + 1;
        }
    }
    let result = Number(nums.join(""))
    return result;
}
// k번 더해서 최고의 수 뽑기