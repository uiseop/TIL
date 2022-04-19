function Dict(items = {}) {
    this.items = items;
}

Dict.prototype.getBuffer = function () {
    return { ...this.items };
};

Dict.prototype.clear = function () {
    this.items = {};
};

Dict.prototype.size = function () {
    return Object.keys(this.items).length;
};

Dict.prototype.set = function (key, value) {
    this.items[key] = value;
};

Dict.prototype.has = function (key) {
    return this.items.hasOwnProperty(key);
};

Dict.prototype.get = function (key) {
    return this.has(key) ? this.items[key] : undefined;
};

Dic.prototype.remove = function (key) {
    if (this.has(key)) {
        delete this.items[key];
        return true;
    }
    return false;
};

Dict.prototype.keys = function () {
    return Object.keys(this.items);
};

Dict.prototype.values = function () {
    return Object.values(this.items);
};

Dict.prototype.each = function() {
    return Object.entries(this.items)
}