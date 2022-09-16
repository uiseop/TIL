const lzw = (answer, msg, dict, did) => {
    console.log(answer, msg)
    if (!msg) return
    if (msg.length === 1) {
        answer.push(dict.get(msg))
        return
    }
    let mid = 1
    while (dict.has(msg.slice(0,mid)) && mid <= msg.length ) {
        mid += 1
        console.log("hello??")
    }
    dict.set(msg.slice(0, mid), did)
    answer.push(dict.get(msg.slice(0,mid-1)))
    lzw(answer, msg.slice(mid-1), dict, did+1)
    return
}

function solution(msg) {
    var answer = [];
    const alpha = new Array(26).fill().map((_,i) => String.fromCharCode(i+65))
    const dict = new Map()
    alpha.forEach((s,i) => dict.set(s, i+1))
    lzw(answer, msg, dict, 27)
    console.log(answer)
    return answer;
}

solution('TOBEORNOTTOBEORTOBEORNOT')