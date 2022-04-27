function mergeSort(arr) {
    if (arr.length === 1) return arr;
    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
    const result = [];
    let leftIdx = 0;
    let rightIdx = 0;

    while (leftIdx < left.length && rightIdx < right.length) {
        if (left[leftIdx] < right[rightIdx]) {
            result.push(left[leftIdx])
            leftIdx += 1;
        } else {
            result.push(right[rightIdx]);
            rightIdx += 1;
        }
    }

    return result.concat(left.slice(leftIdx), right.slice(rightIdx));
}

console.log(mergeSort([5,4,3,2,1]))