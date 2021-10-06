const HASH_SIZE = 37;

function Element(key,value){
    this.key = key;
    this.value = value
}

function HashTable(){
    this.table = new Array(HASH_SIZE);
    this.length = 0;
}

HashTable.prototype.hashFunc = function(key){
    let hash = 0
    for(let i=0; i<key.length; i++){
        // 문자열.charCodeAt(문자열의 위치) : 아스키코드로 반환
        // 문자열의 모든 문자의 아스키코드 합으로 해시처리
        hash += key.charCodeAt(i)
    }
    return hash % HASH_SIZE;
}

// put() : 데이터 추가
HashTable.prototype.put = function(key,value){
    let hash = this.hashFunc(key)
    
    if(this.table[hash] !== undefined) return false

    this.table[hash] = new Element(key,value)
    this.length += 1
    return true
}


// get() : 데이터 조회(key값을 통해서)
HashTable.prototype.get = function(key){
    let hash = this.hashFunc(key)
    return this.table[hash]
}


// remove() : 데이터 삭제(key값을 통해서)
HashTable.prototype.remove = function(key){
    let hash = this.hashFunc(key)
    if(this.table[hash] !== undefined){
        delete this.table[hash]
        this.length -= 1
        return hash
    }
    return undefined
}

// clear() : 초기화
HashTable.prototype.clear = function(){
    this.table = new Array(HASH_SIZE)
    this.length = 0
}

// size() : 크기 반환 length
HashTable.prototype.size = function(){
    return this.length
}

// getBuffer() : 데이터셋 반환
HashTable.prototype.getBuffer = function(){
    let arr = []
    for(let elem of this.table){
        if(elem){
            arr.push(elem)
        }
    }
    return arr
}

// print() : 데이터 셋 출력 인덱스 -> 키 -> 값
HashTable.prototype.print = function(){
    for(let elem in this.table){
        if(this.table[elem]){
            console.log(`${elem} -> ${this.table[elem].key} -> ${this.table[elem].value}`)
        }
    }
}


let ht = new HashTable();

ht.put('Ana', 172)
ht.put('SueA', 163)
ht.put('Paul', 190)

// console.log(ht.getBuffer());

// console.log(ht.table);
console.log(ht.print());

console.log(ht.remove('Paul'));
console.log(ht.remove('Paul'));