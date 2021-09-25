var student = [
    { name : "재석", age : 21},
    { name : "광희", age : 25},
    { name : "형돈", age : 13},
    { name : "명수", age : 44}
]
// 객체를 리스트로 변환하지 않고 한번에 정렬 할 수 있음
// 객체를 이름, 오름차순으로 정렬
student.sort((a,b) => a.name > b.name? 1: a.name < b.name? -1 : 0)

console.log(student);

// 객체를 이름, 내림차순으로 정렬
student.sort((a,b) => a.name > b.name ? -1: a.name < b.name ? 1 : 0)

console.log(student);

// 객체를 나이순으로 정렬
student.sort((a,b) => a.age > b.age? 1: a.age < b.age ? -1 : 0)

console.log(student);