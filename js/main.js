const day = 3
let weekend = ''

switch(day){
    case 1:
        weekend = 'mon'
        break
    case 2:
        weekend = 'tue'
        break
    case 3:
        weekend = 'wed'
        break
    case 4:
        weekend = 'thu'
        break
    case 5:
        weekend = 'fri'
        break
    case 6:
        weekend = 'sat'
        break
    case 7:
        weekend = 'sun'
        break
    default:
        weekend = 'end'
}

console.log(weekend);

const UNTIL_NUM = 10
let sum = 0
for(let i=0; i<=UNTIL_NUM; i++){
    if(i%2 === 0){
        sum += i
    }
}
console.log(sum);

for(let i=2; i<=9; i++){
    for(let j=1; j<=9; j++){
        console.log(`${i} x ${j} = ${i*j}`);
    }
}