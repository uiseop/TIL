// 빵틀
function FishBread(flavor, price){
    this.flavor = flavor
    this.price = price
    this.base = 'flour'
}
// `new.target을` 통해 new를 사용했는지 확인할 수 있어
let bread_1 = new FishBread("cream", 1200)
let bread_2 = new FishBread("redbean", 1000)
let bread_3 = new FishBread("milk", 1500)

console.log(bread_1);
console.log(bread_2);
console.log(bread_3);
