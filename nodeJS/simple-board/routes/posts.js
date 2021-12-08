const { Router } = require("express");
const { Post } = require("../models/post");

const router = Router();

router.get("/", async (req, res) => {
    const posts = await Post.find({});
    res.render("post/index", { posts });
});

router.get("/new", (req, res) => {
    res.render("post/new");
});

router.post("/", async (req, res, next) => {
    const { title, content } = req.body;
    try {
        if (!title || !content) {
            throw new Error("제목과 내용을 입력 해 주세요");
        }
        const post = await Post.create({
            title,
            content,
        });
        res.redirect(`/posts/${post.shortId}`);
    } catch (err) {
        next(err);
    }
});

router.get("/:shortId", async (req, res, next) => {
    const { shortId } = req.params;
    const post = await Post.findOne({ shortId })
    console.log(post)
    res.render('post/detail', { post })
});

module.exports = router;
