function possible(stones, k, n) {
    let tmp = stones.slice();
    let leaf = 0;

    for (let i = 0; i<tmp.length; i++) {
        tmp[i] -= n;
    }

    for (let i=0; i<stones.length; i++) {
         if(tmp[i] <= 0) {
             leaf++
         }
         else {
             leaf = 0;
         }
        if(leaf >= k) 
            return false;
    }

    return true;
}
function solution(stones, k) {
    let result = 0;

    let start = 0;
    let end = 200000000;
    //let cnt = 0;
    while (start<=end) {
        //cnt++;
        //if (cnt>100) break;
        let mid = start + Math.floor((end-start)/2)

        //console.log(start,end,mid)

        if(possible(stones,k,mid)) {
            start = mid+1
        }
        else {
            end = mid -1;
        }
    }
    //console.log(end,start);
    return start;
}