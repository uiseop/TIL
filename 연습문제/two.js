solution1 = (num) => {
    return !!(num % 4);
};

// 2번
function solve(pattern, str) {
    const words = str.split(" ");
    const newMap = new Map();
    // 패턴길이랑 입력 단어의 길이랑 다르면 false
    if (words.length !== pattern.length) return false;
    if (new Set(words).size !== new Set(pattern).size) return;
    false;
    for (let i = 0; i < pattern.length; i++) {
        if (newMap.has(pattern[i]) && newMap.get(pattern[i]) !== words[i])
            return false;
        newMap.set(pattern[i], words[i]);
    }
    return true;
}

// 3번
// 문자열을 split('')으로 해서 Array형식으로 만든 뒤, reverse().join('')
// 하면 더 짧게 풀이가 가능
const soulution3 = (num) => {
    if (Math.abs(num) > 100000) {
        return 0;
    }
    let str_num = num.toString();
    const reverse = (n) => {
        let result = "";
        for (let i = n.length - 1; i >= 0; i--) {
            result += n[i];
        }
        return result;
    };
    if (str_num[0] === "-") {
        str_num = str_num.slice(1);
        let result = "-" + reverse(str_num);
        console.log(result);
        return result;
    } else {
        let result = reverse(str_num);
        console.log(result);
        return result;
    }
};

// 4번 .....snowball.....
function solution4(n, s, t) {
    // 반복 주기
    var repeatDuration = n + s.length;
    // 반복되는 주기를 제외하고 남은 시간 계산
    var optimizeTime = t % repeatDuration;
    // 남은 시간이 흐른 후의 전광판 출력
    var text = ".".repeat(n) + s + ".".repeat(n - 1);
    // substr 대신 substring 사용하는것을 권장함 (문자열에선)
    return text.substr(optimizeTime, n);
}

// 5번

const sol5 = (s) => {
    let arr = s.split(/[\.\,\!\?\s]/);
    const reverse = (arr) => {
        let nArray = [];
        for (let aid in arr) {
            let result = "";
            for (let i = arr[aid].length - 1; i >= 0; i--) {
                result += arr[aid][i];
            }
            if (result !== "") {
                nArray.push(result);
            }
        }
        return nArray;
    };

    arr = reverse(arr);
    console.log(arr);
    return arr;
};

sol5("Hello, World!?");


function solution6(city) {
    return calcDistance(city);
}
function calcDistance(city) {
    var aptLocations = [];
    var busLocations = [];
    getLocations(city, aptLocations, busLocations);
    var ret = createBaseResult(city);
    for (var aptIndex = 0; aptIndex < aptLocations.length;aptIndex++) {
        var aptY = aptLocations[aptIndex][0];
        var aptX = aptLocations[aptIndex][1];
        for (var busIndex = 0; busIndex < busLocations.length;
        busIndex++) {
            var distance = getDistance(aptLocations[aptIndex],
            busLocations[busIndex]);
            ret[aptY][aptX] = (ret[aptY][aptX] === 0) ? distance :
            Math.min(ret[aptY][aptX], distance);
        }
    }
    return ret;
}
function getLocations(city, aptLocations, busLocations) {
    var ySize = city.length;
    var xSize = city[0].length;
    for (var y = 0; y < ySize; y++) {
        for (var x = 0; x < xSize; x++) {
            if (city[y][x] === 1) {
            aptLocations.push([y, x]);
            } 
            else {
            busLocations.push([y, x]);
            }
        }
    }
}
function createBaseResult(city) {
    var ySize = city.length;
    var xSize = city[0].length;

    return Array.from(Array(ySize), () => new
    Array(xSize).fill(0));
}
    
function getDistance(aptLocation, busLocation) {
    return Math.abs(aptLocation[0] - busLocation[0]) +
    Math.abs(aptLocation[1] - busLocation[1]);
}