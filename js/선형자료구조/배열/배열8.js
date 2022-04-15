const input = [
    [5, 2, 4, 1, 7, 5],
    [12, 8, 10, 11, 9, 5, 8],
    [27, 14, 19, 11, 26, 25, 23, 15],
];

function answer(blocks) {
    const avg = blocks.reduce((sum, n) => sum + n, 0) / blocks.length;
    let move = blocks.reduce((tot, n) => {
        if (n > avg) {
            return tot + (n - avg);
        }
        return tot;
    }, 0);

    return move;
}

for (let arr of input) {
    console.log(answer(arr));
}
