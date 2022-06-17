import { createStore } from "redux";

const get = (target) => document.querySelector(target);
const add = get(".Add");
const minus = get(".Minus");
const number = get(".number");

const ADD = "ADD"
const MINUS = "MINUS"

const countModifier = (count = 0, action) => {
    switch (action.type) {
        case ADD:
            return count + 1;
        case MINUS:
            return count - 1;
        default:
            return count;
    }
};

const countStore = createStore(countModifier);

number.innerText = countStore.getState();

const onChage = () => {
    number.innerText = countStore.getState();
};

countStore.subscribe(onChage);

add.addEventListener("click", () => countStore.dispatch({ type: ADD }));
minus.addEventListener("click", () => countStore.dispatch({ type: MINUS }));
