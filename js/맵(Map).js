let map = new Map()

map.set('name','의섭')
map.set(123,456)
map.set(true, "bool_type")

console.log(map.has(123));
console.log(map.get(true));

map.clear()
console.log(map);

map.set('name',"의섭").set(123,456).set(true, "bool_type")
console.log(map);

let recipe_juice = new Map([
    // [key,value] 형식으로 한번에 지정이 가능해. 단 Map안엔 iterable형식으로 들어가야하니까 앞에 대괄호를 쳐줘야함
    ['strawberry',50],
    ['banana',100],
    ['ice',150],
    ['watermellon',200],
])


console.log(recipe_juice);
for(let item of recipe_juice.keys()){
    console.log(item);
}