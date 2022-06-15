(function () {
    interface SquareConfig {
        color?: string;
        width?: number;
    }

    function createSquare(config: SquareConfig): {
        color: string;
        area: number;
    } {
        let newSquare = { color: "white", area: 100 };
        if (config.color) {
            newSquare.color = config.color;
        }

        if (config.width) {
            newSquare.area = config.width * config.width;
        }
        return newSquare;
    }
    // '{ colour: string; width: number; }' 형식의 인수는 'SquareConfig' 형식의 매개 변수에 할당될 수 없습니다.
    // 개체 리터럴은 알려진 속성만 지정할 수 있지만 'SquareConfig' 형식에 'colour'이(가) 없습니다. 'color'을(를) 쓰려고 했습니까?ts(2345)
    // let mySquare = createSquare({ colour: "red", width: 100})
    // Optional 프로퍼티와 초과 프로퍼티를 결합하면 위와 같은 오류를 확인할 수 있다

    const mySquare = createSquare({width: 100, height: 300, color: "black"})

    console.log(mySquare);
})();
