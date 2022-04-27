//  -- Not In Place한 방법: 훨씬 직관적이며 구현이 쉽지만 메모리 공간의 낭비가 심하다는 문제가 있음

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

// -- In Place한 방법: 추가적인 공간을 필요로 하지 않기 떄문에 메모리 공간이 절약되지만,
//  왼쪽/오른쪽 교환하는 과정에서 중복값의 위치가 변경될 수 있기때문에 unStable한 정렬 방법이다.

function inQuickSort(arr, left=0, right=arr.length - 1) {
    if (left >= right) {
        return;
    }
    const mid = Math.floor((left + right) / 2);
    const pivot = arr[mid];
    const partition = divide(arr, left, right, pivot)

    inQuickSort(arr, left, partition - 1);
    inQuickSort(arr, partition, right);
    return arr;
}

function divide(arr, left, right, pivot) {
    while (left < right) {
        while (arr[left] < pivot) {
            left++;
        }
        while (arr[right] > pivot) {
            right--;
        }
        if (left <= right) { // 탈출조건, left === right일 경우에도 ++, -- 연산을 해줌으로 while문을 탈출할 수 있음
            let swap = arr[left];
            arr[left] = arr[right]
            arr[right] = swap;
            left++;
            right--;
        }
    }
    return left;
}

console.log(inQuickSort([5, 3, 7, 1, 9]));