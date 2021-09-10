const solve1 = (nums) => {
    const length = nums.length
    let student = [...Array(length+1).keys()].slice(1)
    for(let i of nums){
        student[i-1] = -1
    }
    // console.log(student);
}

solve1([1,3,4,8])

const solve2 = (puzzle, word) => {
    if(!puzzle || puzzle.length <= 0 ) return false

    const SIZE = 4
    const D = [[1,0],[-1,0],[0,1],[0,-1]]

    const dfs = (r,c,w) => {
        // 해당자리 문자가 word의 문자랑 다르면 break하도록
        if(puzzle[r][c] !== word[w]) return false
        // 마지막 문자에 도달한거면 true
        if(w === word.length - 1) return true
        // --------- 기저조건 끝 ------------
        // 해당 자리의 문자는 방문을 했다는 표시인듯. 또또또또또 이런 문자면 다시 검색할 수 있으니
        puzzle[r][c] = 'x'

        for(const [dr,dc] of D){
            const nr = r + dr
            const nc = c + dc
            // true로 반환될경우 계속 진행해서 결국 true를 반환해서 true를 반환
            if(0<=nr && nr<SIZE && 0<=nc && nc<SIZE){
                if(dfs(nr,nc,w+1)) return true
            }
        }

        // 아닐경우에는 x로 만든 글자를 다시 방문하지 않은걸로 돌려야해
        puzzle[r][c] = word[w]
        return false
    }
}

const solve3 = (arr,num) => {
    // arr의 마지막 인덱스의 배열을 가져와? 왜 why?? 마지막 배열이 최대배열임 : 오름차순 정렬
    const maxArray = arr[arr.length-1]
    // arr의 첫번째 인덱스의 길이 -1 ?? 왜 why?? =>  첫번째 인덱스의 마지막번째를 기준으로 정렬한건가봄
    const minNum = arr[0].length-1
    // 오름차순으로 정렬되서 최소는 0,0
    let min = arr[0][0]
    let max = maxArray[minNum] + 1
    // 이분탐색을 해서 mid값을 기준으로 cnt 개수를 num과 일치하는지 확인!!
    // 이분탐색이니까 min과 max값은 left와 right. right가 더 작아지거나 같을때까지 진행
    // 만약 입력 n이 엄청나게 클 때 사용하면 좋음
    // 혹은 해당 index를 찾을 때, searching할때는 이분탐색을 생각해서 쓰면 좋다!
    while(min<max){
        let mid = min + Math.floor((max-min)/2)
        let cnt = 0
        for(let i =0; i< arr.length; i++){
            // 참가 국가 수 === 각 국가의 참여 선수들의 수
            for(let j=0; j<arr.length; j++){
                if(arr[i][j] <= mid){
                    cnt += 1
                }else{
                    break
                }
            }
        }
        if (cnt < num){
            min = mid + 1
        }
        else{
            max = mid
        }
    }
}

const solve4 = (str) => {
    const alpha = []
    let temp = 0
    // str.split('') 은 붙어있는 string타입을 Array로 변환해서 한글자씩 위치하게
    // reduce는 1.누산기, 2.현재값, 초기값
    
    
    // 공통점 : bruteforce방식으로 진행한것.
    // 차이점 : 자바스크립트 내장함수를 사용함으로써 더 깔끔한 코딩이 가능
    // 배열의 dictionary처럼 사용의 가능함을 알게 됨

    // reduce((callback함수) , 초기값) callback의 계산값으로 하나의 결과값을 반환함 reduce!
    // reduce((콜백의 반환값, 현재값, 현재값의 인덱스, 호출한 배열), 초기값)
    // 초기값을 선언하지않으면 첫번쨰값이 콜백의 반환값으로 드루가
    
    
    return str.split('').reduce((longest,current,currentIndex) => {
        // temp는 시작하는 인덱스. (중복이 없는!)
        // 그래서 temp값과 alpha[현재]값과 비교를 해서 현재 값이 시작하는 인덱스 뒤에 있으면
        // 중복이 되니까 시작하는걸 현재인덱스의 다음번째(다른 단어)로 바꿔줌
        // 중복된게 없으면 그냥 pass! temp값 유지!
        temp = temp <= alpha[current]? alpha[current] + 1: temp
        // alpha의 알파벳은 인덱스를 저장한다
        // 현재 단어 최신위치를 업데이트
        alpha[current] = currentIndex
        // longest Number형 공간에 더 큰 값을 넣어줘
        // 시작 위치(temp) ~ 현재 위치 current + 1을 하면 길이가 나와
        return Math.max(longest, currentIndex - temp + 1)
    },0)
}

solve4('nooeolomx')

const solve5 = (arr) => {
    let temp = new Set()
    // 끝나는 시간을 기준으로 오름차순 정렬
    // 끝나는시간이 같으면 시작하는시간 기준 오름차순
    arr.sort((a,b) => a[1] === b[1]? a[0]-b[0] : a[1]-b[1])
    for(let [stt,end] of arr){
        // Set.prototype.has : Set객체에서 주어진 요소가 존재하는지 여부를 판별해줘
        // Set.has(검색할 요소). Set객체는 중복을 하용하지않지

        // add. delete, has, 
        while(stt <= end && temp.has(stt)) ++stt
        if(stt <= end) temp.add(stt)
    }
    return temp.size
}

solve6 = (time,distance) => {
    const dist = distance.length
    let enemy = []
    let result = 0

    for(let i in dist){
        enemy.push(distance[i] / time[i])
    }
    // x,y를 비교해서 오름차순으로
    // -1,0 그대로 1 change
    enemy.sort((x,y) => x-y)

    for(const person of enemy){
        if(person - result <= 0){
            break
        }
        result += 1
    }
    return result
}