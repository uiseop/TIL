const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");

dotenv.config();

const url = `mongodb+srv://${process.env.MONGODB_CLIENT_NAME}:${process.env.MONGODB_CLIENT_PASSWORD}@simple-board-cluster.0n9yh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;

// Promise로 해결
mongoose.connect(url)
        .then(() => console.log('몽고DB가 연결되었습니다!!'))
        .catch((err) => console.log(err))


// 한줄 한줄 입력하는 방법
// const db = mongoose.connection;

// db.on("error", () => {
//     console.log("Connection Failed");
// });

// db.once("open", () => {
//     console.log("Connected!!");
// });
