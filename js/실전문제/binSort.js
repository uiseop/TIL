/* 
배열 A에는 0 ~ 1000사이의 숫자가 랜덤하게 들어있습니다.
이 숫자들이 2진수로 변환되었을 때 가지고 있는 1의 개수에 따라 오름차순 정렬하는 함수를 작성하세요.
단, 1의 개수가 같은 경우 숫자의 크기에 따라 오름차순 정렬을 합니다.
*/

const solution = (arr) => {
    const binArr = arr.map((num) => {
        return num.toString(2);
    });
    binArr.sort((a, b) => {
        const count_a = a.split("").filter((num) => num === "1").length;
        const count_b = b.split("").filter((num) => num === "1").length;
        if (count_a > count_b) return 1;
        else if(count_a < count_b) return -1;
        const int_a = parseInt(a, 2);
        const int_b = parseInt(b, 2);
        if (int_a > int_b) return 1;
        else if (int_a < int_b) return -1;
        else return 0;
    });

    const intArr = binArr.map((num) => parseInt(num,2))

    console.log(intArr)
    return;
};

// 자바스크립트의 sort 메서드에는 compareFunction이라는 함수가 있는데 이게 생략되면 문자열로 취급되어 유니코드 값 순서대로 정렬
// a,b 두개의 파라미터를 입력받고 함수의 결과가 0보다 작으면 a가 먼저, 0보다 크면 b가 먼저
// 결과가 0이면 순서를 바꾸지 아니한다.
// 결과적으로 원본 객체를 변화시킨다.

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
solution(arr);
