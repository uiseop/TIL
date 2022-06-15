function getCounter() {
    var c = (function (start) { });
    c.interval = 123;
    c.reset = function () { };
    return c;
}
var c = getCounter();
c(10);
c.reset();
c.interval = 5.0;
