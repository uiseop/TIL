const express = require("express");
const path = require("path");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const userRouter = require("./routes/user");
const cookieParser = require("cookie-parser");
const session = require("express-session");

const app = express();
const PORT = 5000;

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));
app.use(cookieParser());
app.use(session({
    key: "sessionID",
    secret: "my_secret",
    resave: false,
    saveUninitialized: true,
    cookie: {
        maxAge: 24000*60*60
    }
}))
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

dotenv.config();

mongoose.connect(process.env.MONGODB_URL);
mongoose.connection.on("connected", () => {
    console.log("몽고디비가 연결 디비 됐습니다.");
});

app.get("/", (req, res) => {
    res.render("users/login");
});

app.get("/signup", (req, res) => {
    res.render("users/signup");
});

app.use("/user", userRouter);

app.listen(PORT, () => {
    console.log(`The server is opened ${PORT}`);
});
