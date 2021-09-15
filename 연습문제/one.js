// 1번
// 출석번호는 1씩 차이나는 오름차순으로 하고자기때문에 nums의 길이만큼 0으로 채워진 cnt를 선언
// cnt배열의 nums 요소들의 값을 1로 업데이트 -> 자바스크립트의 배열은 동적으로 할당 가능. 그 사이의 값은 undefined로 채워짐
// nums의 길이만큼 cnt를 확인하는데 1로 업데이트 되지 않은 부분(0의 값을 갖는)을 ans배열에 넣어주어서 해결
const nums = [1,2,3,5,8,10,12,15,18,20];
const cnt = Array(nums.length+1).fill(0)

for(let i of nums){
    cnt[i] = 1
}
ans = []
for(let i=1; i<nums.length+1; i++){
    if(cnt[i] === 0){
        ans.push(i)
    }
}

console.log(ans)

// 2번

// dfs함수를 화살표 함수로 선언
// findIndex함수를 사용해서 d배열(상하좌우) 이내에 다음문자와 일치하는 배열을 찾고 만약 있다면(return 값이 -1이 아니면) 재귀적으로 dfs를 호출
// dfs의 공통변수로 let ans를 선언 및 할당을 하고, 해당 스코프 안에서 ans값을 독립적으로 갖도록 한 후에
// 최종적으로 끝의 문자를 일치하는걸 찾으면 return true를 통해 puzzle안에 찾고자하는 word가 있음을 알림
// dfs를 호출한 전역부분에선 dfs가 true를 반환하면 flag값에 1을 넣어줌으로써 반복문을 탈출(back tracking)
const dfs = (r,c,w) => {
    let ans = false;
    let idx = d.findIndex((d)=>{
        let nr = r + d[0]
        let nc = c + d[1]
        if(0<=nr && nr<4 && 0<=nc && nc<4 && puzzle[nr][nc] === word[w]) return true
        else return false
    })
    if(idx !== -1){
        const nr = r + d[idx][0]
        const nc = c + d[idx][1]
        if(puzzle[nr][nc] === word[word.length-1]){
            return true
        }
        else{
            ans = dfs(nr,nc,w+1)
        }
    }
    return ans
}

puzzle = [['게', '양', '콘', '사'],['보', '린', '스', '세'],['루',
'을', '먹', '어'],['마', '블', '틴', '요']];
word = '게보린을먹어요'
const d = [[1,0],[-1,0],[0,1],[0,-1]]

let flag = 0;
for(let i=0; i<4; i++){
    for(let j=0; j<4; j++){
        // 만약 같은글자가 반복되면 실패하게 돼 따라서 현재 방문 글자를 지워주고, 다시 돌려주는
        // 코드가 필요하다.
        if(puzzle[i][j] === word[0]){
            if(dfs(i,j,1) === true){
                flag = 1;
                break
            }
            else{
                continue
            }
        }
    }
    if(flag) break
}
if(flag === 1){
    console.log('true')
}
else{
    console.log('false')
}


// 3번 
// 자바스크립트에서는 heap과 관련한 라이브러리를 제공하지 않음.
// 정렬되지 않은 배열에서 최소값을 찾기 => O(n)
// 배열을 정렬하기 => O(nlogn)

// 최소값 혹은 최대값을 찾는 가장 좋은 방법은 힙을 이용한 우선 순위 큐를 활용해야함

function heappush(heap,elem){ // 새 요소를 push하게 되면 최하위 레벨의 가장 오른쪽에 노드가 추가 돼. 그런 후 조건을 만족할때까지 자신의 위치를 찾아가
    heap.push(elem)

    let idx = heap.length - 1  // 마지막 인덱스의 위치 -> i = (n-1)//2 기 때문에 아래 과정 진행
    // parseInt vs Math.trunc :   parseInt는 toString을 통해 string으로 변환하는 과정에서 오류가 발생할 수 있어. 때문에 string arg에서만 주로 사용하고
    // numbers를 다룰 땐 Math.trunc를 사용하자
    while(idx > 0){ // 자신의 위치를 찾을때까지 계속 진행
        const parent = Math.trunc((idx-1)/2)
        if(heap[idx] < heap[parent]){
            [heap[idx],heap[parent]] = [heap[parent],heap[idx]] // 구조분해할당으로 parent와 idx를 swap!
            idx = parent
        }else{
            break
        }
    }
}

function heappop(heap){
    const res = heap.shift() // popleft
    if(heap.length === 0){
        return res // 길이가 0이면 끝 -> 기저조건 // 최솟값 pop
    }
    heap.unshift(heap.pop()) // 가장 마지막 레벨, 가장 오른쪽 노드를 pushleft

    let idx = 0;

    while(2*idx + 1 < heap.length){
        const left = 2*idx + 1
        const right = 2*idx + 2

        let next = idx;
        if(heap[left] < heap[next]){
            next = left
        }

        if(heap[right] < heap[next]){
            next = right
        }
        if(idx === next){
            break
        }

        if(idx !== next){
            [heap[idx],heap[next]] = [heap[next],heap[idx]]
            idx = next
        }
    }

    return res

}

const arr = [[4,5,6,7,8],[11,12,13,14,15],[15,16,19,33,35],[6,8,20,22,88],[8,55,66,77,100]];
const num = 11

const heap = []
arr.forEach(sub => {
    sub.forEach(idx => heappush(heap,idx))
})

let a = 0
for(let i=0;i<num;i++){
    a = heappop(heap)
}

console.log(a);

// 4번
// Array.includes()함수를 사용하여 배열안에 값이 포함되어 있는지 확인하였음
// find함수를 통해 true, false 출력 가능
// findIndex를 통해 찾은 요소의 index를 출력할 수 있음
// filter함수는 만족하는 요소를 모두 포함하는 배열을 출력함
const str = "yeongmin";
let count = 0;
let isMax = 0;
let stack = []
for(let i of str){
    if(stack.includes(i)){
        stack = [];
        isMax = isMax>count?isMax:count;
        count = 0;
    }
    else{
        stack.push(i)
        count += 1
    }
}
isMax = isMax>count?isMax:count;
console.log(isMax);


// 5번

const n_arr = [[1,1],[2,2],[2,4],[3,4]];
const obj = {}
let tot = 0
n_arr.forEach(t => {
    if(t[0] === t[1] && !obj[t[0]]){

        obj[t[0]] = 1
        tot += 1
    }
    else{
        for(let i=t[0]; i<t[1]+1; i++){
            if(!obj[i]){
                obj[i] = 1
                tot += 1
                break
            }
        }
    }
})
console.log(tot);

// 6번
// 문제 이해가 가질 않습니다. 

let arr123 = Array.from({length:10}, (_,i) => i)
console.log(arr123);