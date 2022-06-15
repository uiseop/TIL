interface Counter {
    (start: number): string;
    interval: number;
    reset(): void;
}

function getCounter(): Counter {
    let c = (function (start: number) {}) as Counter;
    c.interval = 123;
    c.reset = function () {}
    return c
}

let c = getCounter();
c(10);
c.reset()
c.interval = 5.0;