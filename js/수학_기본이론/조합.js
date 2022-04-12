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


combination(input, output, 0, 0, 2)
console.log(count);

/* output
1 2
1 3
1 4
2 3
2 4
3 4
6
*/