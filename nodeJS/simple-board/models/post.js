const mongoose = require("mongoose");
const { Schema } = mongoose
const shortId = require("./types/short-id");

const postSchema = new Schema(
    {
        shortId,
        title: {
            type: String,
            required: true,
        },
        content: {
            type: String,
            required: true,
        },
        author: {
            type: String,
            required: true,
            default: "작성자",
        },
    },
    {
        timestamps: true,
    }
);

// 모델을 만드는것이고, 모델명은 대소문자를 구분하지 않으며 무조건 복수형이 된다
exports.Post = mongoose.model('sosts', postSchema);
