const input = [
    1, 65, 3, 2, 16, 3, 32, 45, 3, 26, 435, 2, 23, 45, 6476, 3, 453, 765, 424,
    243, 3124, 6, 476, 4576, 543, 763455, 354,
];

const quickSort = (
    arr: number[],
    left: number = 0,
    right: number = arr.length - 1
) => {
    const partition = (low: number, high: number) => {
        const pivot = arr[high];
        let left = low;
        for (let right = low; right <= high; right++) {
            if (arr[right] < pivot) {
                [arr[left], arr[right]] = [arr[right], arr[left]];
                left += 1;
            }
        }
        [arr[left], arr[high]] = [arr[high], arr[left]];
        return left;
    };

    if (left < right) {
        const pivot = partition(left, right);
        quickSort(arr, left, pivot - 1);
        quickSort(arr, pivot + 1, right);
    }
};

quickSort(input);
console.log(input);
