function quickSort(arr) {
    if (arr.length <= 1) {
         return arr;
    }
    let pivot = [arr[0]];
    const left = [];
    const right = [];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else if (arr[i] > pivot) {
            right.push(arr[i]);
        } else {
            pivot.push(arr[i]);
        }
    }

    return quickSort(left).concat(pivot, quickSort(right));
}

console.log(quickSort([5, 3, 7, 1, 9]));
