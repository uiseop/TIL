const input = [
    "(a+b)",
    "(a*(b+c)+d)",
    "(a*b(b+c)+d+(e)",
    "(a*(b+c)+d)+e)",
    "(a*(b+c)+d)+(e*(f+g))"
]

function answer(str) {
    const result = [];

    const strToArray = str.split("")
    const left = []
    for(let i=0; i<strToArray.length; i++) {
        if (strToArray[i] === "(") {
            left.push(i)
        } else if (strToArray[i] === ")") {
            if (left.length === 0) {
                return []
            }
            result.push([left.pop(), i])
        }
    }

    if (left.length > 0) {
        return []
    }

    return result;
}

for(let i=0; i<input.length; i++) {
    console.log(answer(input[i]))
}