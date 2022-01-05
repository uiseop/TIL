const express = require("express");
const path = require("path");
const env = require("dotenv");
const mongoose = require("mongoose");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");

env.config();

const app = express();
mongoose.connect(process.env.MONGODB_URL);
mongoose.connection.on("connected", () => {
    console.log("hello mongoDB");
});

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));
app.use(cors());

const postSchcema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    desc: {
        type: String,
        required: true,
    },
    author: {
        type: String,
        required: true,
        default: "철수",
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

const Post = mongoose.model("post", postSchcema);

app.post("/api", async (req, res) => {
    const { title, desc } = req.body;
    const post = await Post.create({ title, desc });
    res.json(post);
});

app.get("/api/lists", async (req, res) => {
    const posts = await Post.find({});
    res.json(posts);
});

const users = [];
const jwtSecret = "JsonWebTokenSecret";

app.post("/join", (req, res) => {
    const { email, password } = req.body;
    const user = users.find((u) => u.email === email);
    if (!user) {
        const salt = String(Math.round(new Date().valueOf() * Math.random()));
        const hashedPassword = crypto
            .createHash("sha512")
            .update(password + salt)
            .digest("hex");

        const newUser = { email, password: hashedPassword };
        users.push(newUser);
        // const newUserToken = jwt.sign({email}, jwtSecret, { expiresIn: 60*60})

        return res.status(200).json({
            msg: "회원가입 성공!!",
        });
    } else {
        return res.status(400).json({
            msg: "이미 가입된 이메일입니다.",
        });
    }
});

app.post("/login", (req, res) => {
    const { authorization } = req.headers;
    console.log(authorization);
    const userToken = authorization.split(" ")[1];

    jwt.verify(userToken, jwtSecret, (err, encode) => {
        if (err) console.error(err);
        else {
            cosole.log(encode);
        }
    });
});

app.listen(3000, () => {
    console.log("hello PORT 3000");
});
