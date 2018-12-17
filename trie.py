class Trie_node:
    def __init__(self):
        self.children = [None]*26
        self.end = False


class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, key):
        seek = self.root
        for ch in key:
            index = ord(ch)-ord('a')
            if not seek.children[index]:
                seek.children[index] = Trie_node()
            seek = seek.children[index]
        seek.end = True

    def search(self, key):
        seek = self.root
        for ch in key:
            index = ord(ch)-ord('a')
            if not seek.children[index]:
                return False
            seek = seek.children[index]
        return seek is not None and seek.end

if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]
    t = Trie()
    for key in keys:
        t.insert(key)

    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))

