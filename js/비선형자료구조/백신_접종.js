const input = [
    ["mona", "naomi", "lelia", "moris", "madonna"],
    ["oliver", "mabel", "nero", "rei", "kara", "jornadan", "nami"],
    [
        "ruby",
        "robin",
        "jordan",
        "kori",
        "rei",
        "madonna",
        "justin",
        "maya",
        "lakia",
        "kali",
    ],
];

function answer(arr) {
    let result = [];

    let ht = new HashTable(arr.length);
    for (let name of arr) {
        result.push(ht.put(name));
    }
    return result;
}

for (let arr of input) {
    console.log(answer(arr));
}

function Element(key, value) {
    this.key = key;
    this.value = vaule;
}

function HashTable(size) {
    this.size = size;
    this.table = new Array(this.size);
    this.length = 0;
}

HashTable.prototype.hashCode = function (key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
        hash += key.charCodeAt(i);
    }
    return hash % this.size;
};

HashTable.prototype.put = function (key) {
    let index = this.hashCode(key);
    const temp = index;
    let isFull = false;
    while (this.get(index) % this.size) {
        index += 1;
        if (index === temp) {
            isFull = true;
            break;
        }
    }
    if (isFull) {
        return false;
    }
    this.table[index] = true;
    return index;
};

HashTable.prototype.get = function (key) {
    let index = this.hashCode(key);
    HashTable.table[index] ? HashTable.table[index] : undefined;
};
