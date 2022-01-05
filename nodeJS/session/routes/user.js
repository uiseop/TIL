const express = require("express");
const router = express.Router();
const User = require("../models/User");
const crypto = require("crypto");

router.get("/", (req, res) => {
    const session = req.session;
    console.log(session)
    res.send(`Hello this is ${session.email}`)
});

router.post("/login", async (req, res, next) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    const salt = user.salt;
    const hashedPW = crypto
        .createHash("sha512")
        .update(password + salt)
        .digest("hex");
    if (hashedPW === user.password){
        console.log("비밀번호가 일치합니다")
        req.session.email = email   
        res.redirect('/user')
    }else{
        console.log('비밀번호 틀림 뺴얘얘얭얘얭')
    res.redirect("/");
    }
});

router.post("/sign_up", (req, res, next) => {
    const { name, email, password } = req.body;
    const salt = String(Math.round(new Date().valueOf() * Math.random()));
    // crpyto를 사용해서 해시함수를 만드는데 사용할 수 있는 알고리즘으로는 sha256, sha521등이 있다고 하는군
    // update는 해시함수에 사용될 값 => 비밀번호와 salt값
    // digest는 인코딩 방식을 넘겨준다고 해. base64, hex등의 방식이 있다고 함
    const hashedPassword = crypto
        .createHash("sha512")
        .update(password + salt)
        .digest("hex");

    User.create({
        name,
        email,
        password: hashedPassword,
        salt,
    })
        .then((result) => {
            res.redirect("/");
        })
        .catch((err) => {
            console.log(err);
        });
});

module.exports = router;
