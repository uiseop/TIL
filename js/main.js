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