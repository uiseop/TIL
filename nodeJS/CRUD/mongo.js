const express = require("express");
const { MongoClient } = require("mongodb");
const dotenv = require("dotenv");

dotenv.config();

const url = `mongodb+srv://${process.env.MONGODB_CLIENT_NAME}:${process.env.MONGODB_CLIENT_PASSWORD}@simple-board-cluster.0n9yh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;

const client = new MongoClient(url);

async function main() {
    const c = await client.connect();
    // console.log(c)
    console.log("몽고디비에 연결되었습니다!!");
    // users는 연결된 몽고DB에 fc21데이터베이스를 만들고 users라는 collection을 가리킨다 / 없으면 만들고 있으면 선택
    const users = client.db("fc21").collection("users");
    // user Collection을 모두 지워버린다.
    await users.deleteMany({});

    await users.insertMany([
        {
            name: "Foo",
            birthYear: 2000,
        },
        {
            name: "Bar",
            birthYear: 1995,
        },
        {
            name: "Baz",
            birthYear: 2000,
        },
    ]);

    const cursor = users.find({});
    await cursor.forEach(console.log);

    await users.updateOne(
        {
            name: "Baz",
        },
        {
            $set: {
                name: "Boo",
            },
        }
    );

    const cursor2 = users.find({});
    await cursor2.forEach(console.log);

    const cursor3 = users.find({
        birthYear: 2000,
    });

    await cursor3.forEach(console.log);

    const cursor4 = users.find({
        birthYear: {
            $gte: 200,
        },
    });

    await cursor4.forEach(console.log);

    const cursor5 = users.find({
        birthYear: {
            $gte: 200,
        }
    }, {
        sort: {
            // -1 내림차순, 1 오름차순
            birthYear: -1
        }
    })

    await cursor5.forEach(console.log);

    await users.deleteOne({
        name: 'Baz'
    })

    // 열어줬으면 다시 닫아준다
    await client.close();
}

main();
