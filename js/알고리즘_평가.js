function dateSub(old_date, new_date){
    return new_date-old_date
}

function getTimeSub(old_date, new_date){
    return new_date.getTime() - old_date.getTime()
}

function benchMark(callback_func){
    let date_1 = new Date("2020-01-01")
    let date_2 = new Date()

    let start = Date.now();
    for(let i=0; i<100000; i++){
        callback_func(date_1,date_2)
    }
    return Date.now() - start
}

console.log("dateSub : " + benchMark(dateSub) + "ms");
console.log("getTimeSub : " + benchMark(getTimeSub) + "ms")