function Trie() {
    this.root = new TrieNode();
}

function TrieNode() {
    this.children = {};
    this.endOfWord = false;
}

Trie.prototype.insert = function (word) {
    let current = this.root;

    for (let i = 0; i < word.length; i++) {
        let ch = word[i];
        let node = current.children[ch];

        if (node === undefined) {
            node = new TrieNode();
            current.children[ch] = node;
        }

        current = node;
    }

    current.endOfWord = true;
};

Trie.prototype.search = function (word) {
    let current = this.root

    for (let i=0; i<word.length; i++) {
        let ch = word[i];
        let node = current.children[ch];

        if (node === undefined) {
            return false
        }
        current = node;
    }

    return current.endOfWord
}

Trie.prototype.delete = function (word, current=this.root, index=0) {
    if (index === word.length) {
        if(!current.endOfWord) return false;
        current.endOfWord = false;

        return Object.keys(current.children).length === 0;
    }
    let ch = word[index];
    let node = current.children[ch];

    if (node === undefined) return false; // match되는 단어 없음.

    let isDeleteNode = this.delete(word, node, index + 1) && !node.endOfWord; // 삭제되려면 앞에서 끝 flag가 없어야 하고, 재귀적으로 delete했을 때 true가 나와야 해
    if (isDeleteNode) {
        delete current.children[ch];
        return Object.keys(current.children).length === 0;
    }

    return false

}

let trie = new Trie();
trie.insert("be");
trie.insert("bee");
trie.insert("can");
trie.insert("cat");
trie.insert("cd");

console.log(trie);
