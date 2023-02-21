const input = [1,2,3,4];
const output = [];
let count = 0;

const combination = (arr, data, idx, n_cnt, cnt) => {
    if (n_cnt === cnt) {
        count += 1;
        console.log(data.join(" "));
        return
    }
    for (let i=idx; i < arr.length; i++) {
        data[n_cnt] = arr[i];
        combination(arr, data, i + 1, n_cnt + 1, cnt);
    }
}

const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1); 
      // 해당하는 fixed를 제외한 나머지 뒤
      const combinations = getCombinations(rest, selectNumber - 1); 
      // 나머지에 대해서 조합을 구한다.
      combinations.map((combi) => results.push([fixed, ...combi]))
    //   const attached = combinations.map((el) => [fixed, ...el]); 
    //   //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    //   results.push(...attached); 
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}

console.log(getCombinations(input, 2))


// combination(input, output, 0, 0, 2)
// console.log(count);

/* output
1 2
1 3
1 4
2 3
2 4
3 4
6
*/