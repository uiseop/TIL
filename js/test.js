function makeUser() {
    return {
        name: "Uiseop",
        ref() {
            return this;
        },
    };
}

let user = makeUser();
console.log(user.ref().name);