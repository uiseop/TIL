const express = require("express");
const dotenv = require("dotenv");
const mongoose = require("mongoose");
const path = require("path");
const postsRouter = require("./routes/posts");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8000;
// 요청으로 들어온 데이터를 해석할 수 있도록
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
// 정적 파일들 (css, images 등등)
app.use(express.static(path.join(__dirname, "public")));
// views라는 디렉터리에서 views 파일들을 관리하겠다, 엔진으로는 ejs를 쓰겠다.
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

mongoose.connect(process.env.MONGODB_URL);
mongoose.connection.on("connected", () => {
    console.log(`몽고DB 연결 완료`);
});

app.get("/", (req, res) => {
    res.redirect("/posts");
});

app.use("/posts", postsRouter);

app.listen(PORT, () => {
    console.log("server is on " + PORT);
});
