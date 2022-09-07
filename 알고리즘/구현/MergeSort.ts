const input = [
    1, 65, 3, 2, 16, 3, 32, 45, 3, 26, 435, 2, 23, 45, 6476, 3, 453, 765, 424,
    243, 3124, 6, 476, 4576, 543, 763455, 354,
];

// Array.prototype.slice 는 새로운 배열을 만들면서 start?: number, end?: number 이지만 하나만 넣으면 start이기 때문에 start 이후 모두 slice함
// mergeSort는 최악이든 최선이든 상관 없이 모두 분할/정복으로 문제를 해결하기 때문에 완전한 O(nlogn)의 시간 복잡도를 갖는 정렬 알고리즘이다.
// 대부분의 경우 퀵정렬 보다는 느리지만, 어떤 경우에서도 O(nlogn)이 보장되면서, stable 정렬 알고리즘이기때문에 많이 사용된다고 한다.
// 왜 Stable일까? 분할 되는 과정에서 한 아이템 기준 왼쪽에 있던 아이템은 병합할 때 왼쪽 먼저 확인하기 때문에 순서가 보장되는 것 인가?

const merge = (left: number[], right: number[]): number[] => {
    const result: number[] = []
    let leftId = 0
    let rightId = 0
    while (leftId < left.length && rightId < right.length) {
        if (left[leftId] < right[rightId]) {
            result.push(left[leftId])
            leftId += 1
        } else {
            result.push(right[rightId])
            rightId += 1
        }
    }
    return result.concat(left.slice(leftId), right.slice(rightId))
};

const mergeSort = (arr: number[]): number[] => {
    if (arr.length === 1) return arr;
    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    return merge(mergeSort(left), mergeSort(right))
};

const sortedArr = mergeSort(input);
console.log(sortedArr)
