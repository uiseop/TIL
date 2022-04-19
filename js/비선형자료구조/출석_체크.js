const input = [
    [["kali", 'oliver', 'naomi'],
    ['oliver', 'naomi', 'maya']],
    [["roxy", "olga", "kara", "nana"],
    ["oliver", "roxy", "kara", "nana", 'maya']],
    [["roxy", 'ravi', 'nana', 'rei', 'karis', 'mana', 'naomi'],
    ['olga', 'nana', 'rei', 'oliver', 'kali', 'rei', 'kara']]
]

function answer(arr) {
    const result = []
    const [first, second] = arr;
    const f = {}
    const s = {}

    for (let student of first) {
        f[student] = true;
    }

    for (let student of second) {
        if (f[student] === true) {
            result.push(student)
            delete f[student];
        }
    }

    return result
}

for(let arr of input) {
    console.log(answer(arr));
}