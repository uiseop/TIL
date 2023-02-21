// 다차원 배열의 초기화 

// 3차원을 만들어 보자

const arr = new Array(3).fill(null).map((v) => new Array(3).fill(null).map((v) => new Array(3).fill(null)))

let idx = 0

for (let i=0; i<arr.length; i++) {
    for (let j=0; j<arr.length; j++) {
        for (let k=0; k<arr.length; k++) {
            arr[i][j][k] = idx
            idx += 1
        }
    }
}

// 무조건 map을 통해 각기 새로운 Array 객체를 참조할 수 있도록 하여서 다차원 배열을 생성
// 내가 아는 방식, 2차에서 사용하던 방식이 옳다!

// queue 만들기

// stack 버전

function Queue() {
    this.stack1 = new Array()
    this.stack2 = new Array()
}

Queue.prototype.isEmpty = function () {
    if (this.stack1.length === 0 && this.stack2.length === 0) return true
    return false
}

Queue.prototype.append = function (val) {
    this.stack1.push(val)
}

Queue.prototype.pop = function () {
    if (this.stack2.length) {
        // return console.log(this.stack2.pop())
        return this.stack2.pop()
    }
    while (this.stack1.length) {
        const val = this.stack1.pop()
        this.stack2.push(val)
    }
    return this.pop()
}

const q = new Queue()

const t_cur = new Date()

for (let i=0; i<10; i++) {
    q.append(i)
}

const a_end = new Date()

while (!q.isEmpty) {
    q.pop()
}

const t_end = new Date()

console.log(`Double Stack Queue 걸린 시간 ${a_end- t_cur} ${t_end - t_cur}`)

function Queue2 () {
    this.q = new Array()
    this.left = 0
    this.right = 0
}

Queue2.prototype.append = function (val) {
    this.q.push(val)
    this.right += 1
}

Queue2.prototype.pop = function () {
    const ret = this.q[this.left]
    this.left += 1
    return ret
}

Queue2.prototype.isEmpty = function () {
    if (this.left === this.right) return true
    return false
}

const q2 = new Queue2()

const t_cur2 = new Date()

for (let i=0; i<10; i++) {
    q2.append(i)
}

const a_end2 = new Date()

while (!q2.isEmpty()) {
    q2.pop()
}

const t_end2 = new Date()

console.log(`Array Queue 시간: ${t_cur2 - a_end2}, ${t_cur2 - t_end2}`)

const map = new Map()
map.set(0, 0)
map.set(1, 40)
map.set(2, 30)
map.set(3, 20)

const mapIterator = map.values()
// console.log(mapIterator.next())
// console.log(mapIterator.next())
// console.log(mapIterator.next())
// console.log(mapIterator.next())
// console.log(mapIterator.next())
// console.log(mapIterator.next())

for (let val of map.entries()) {
    console.log(val)
}

// 어차피 공간을 많이 쓰는것은 메한가지 인 것 같으니까 속도가 좀 더 빠른 Double Stack을 큐로 사용하자.
// Stack 공간을 하나 더 사용하기 때문에 공간 복잡도 측면에서 더 손해가 있긴 하겠지만,
// 알고리즘 문제 푸는 상황에서는 괜찮아보인다.

// 조합 순열 만들기
// 조합 : n개 중에서 k개를 선택, 중복이 없어야 함
// 순열 : n개 중에서 k개를 선택, 중복을 부분 허용, 순서를 확인

const input = [1,2,3,4,5,6,7,8,9]

const getCombination = (arr, len) => {
  const result = []
  if (len === 1) return arr.map((el) => [el])

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index+1)
    const combis = getCombination(rest, len-1)
    combis.forEach((combi) => result.push([fixed, ...combi]))
  })
  return result
}

// console.log(getCombination(input, 3), 'haha')

const getPermutation = (arr, len) => {
  const results = []
  if (len === 1) return arr.map((el) => [el])
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(0, index).concat(origin.slice(index+1))
    const permutes = getPermutation(rest, len-1)
    permutes.forEach((permute) => results.push([fixed, ...permute]))
  })
  return results
}

console.log(getPermutation(input,2), 'hahah')



// 힙 구현하기

function Heap() {
    this.arr = []
}

Heap.prototype.swap = function (pid, idx) {
    const temp = this.arr[pid]
    this.arr[pid] = this.arr[idx]
    this.arr[idx] = temp
}

Heap.prototype.heappush = function (val) {
    let idx = this.arr.length
    this.arr.push(val)
    if (idx === 0) return
    while (idx) {
        const pid = Math.floor((idx-1) / 2)
        if (this.arr[pid] > this.arr[idx]) {
            this.swap(pid, idx)
            idx = pid
        } else return
    }
}

Heap.prototype.heappop = function () {
    let idx = this.arr.length - 1
    this.swap(0, idx)
    idx = 0
    const ret = this.arr.pop()
    if (this.arr.length > 1) {
        while (true) {
            const left = 2*idx + 1
            const right = 2*idx + 2
            if (this.arr[left] && this.arr[right]) {
                if (this.arr[left] <= this.arr[right] && this.arr[left] < this.arr[idx]) {
                    this.swap(idx, left)
                    idx = left
                } else if (this.arr[left] > this.arr[right] && this.arr[right] < this.arr[idx]) {
                    this.swap(idx, right)
                    idx = right
                } else break
            } else if (this.arr[left] && this.arr[left] < this.arr[idx]) {
                this.swap(idx, left)
                idx = left
            } else break
        }
    }
    return ret
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

while (minHeap.arr.length > 0) {
    console.log(minHeap.heappop())
}

const MyReact = (function() {
    let _val // 모듈 스코프 안에 state를 잡아놓습니다.
    return {
      render(Component) {
        const Comp = Component()
        Comp.render()
        return Comp
      },
      useState(initialValue) {
        _val = _val || initialValue // 매 실행마다 새로 할당됩니다.
        function setState(newVal) {
          _val = newVal
        }
        return [_val, setState]
      },
    }
  })()

function Counter() {
    const [count, setCount] = MyReact.useState(0)
    hello()
}

function hello() {
  console.log('asdhello')
  console.log(count);
}

Counter()