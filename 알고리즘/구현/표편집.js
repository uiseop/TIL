
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
function solution(n, k, cmd) {
    let answer = '';
    // linkedList 구현, length Property, values는 없기때문에 index로 값을 생성
    let list = Array.from({length: n}, (value,index) => [index-1, index+1]);
    let temp = []
    list[n-1][1] = -1
    answer = Array(n).fill(true);
    for(let c of cmd){
        let command = c.split(' ')
        if(command[0] === 'U'){
            for(let i=0 ; i<Number(command[1]); i++){
                k = list[k][0]
            }

        }
        else if(command[0] === 'D'){
            for(let i=0; i<Number(command[1]); i++){
                k = list[k][1]
            }
        }
        else if(command[0] === 'C'){
            answer[k] = false
            temp.push([k,list[k][0],list[k][1]])

            let pre = list[k][0]
            let next = list[k][1]

            if(next === -1){
                if(pre !== -1){
                    list[pre][1] = next
                }
                k = pre
            }else{
                if(next !== -1){
                    list[next][0] = pre

                }
                if(pre !== -1){

                    list[pre][1] = next

                }

                k = next
            }

        }
        else{
            const t = temp.pop()
            let K = t[0]
            let pre = t[1]
            let next = t[2]

            if(pre !== -1) list[pre][1] = K
            if(next !== -1) list[next][0] = K
            answer[K] = true
        }
    }

    answer = answer.reduce((acc,cur) => {
        cur = cur===true?'O':'X'
        return acc+cur
    },'')

    return answer;
}
