class TrieNode: #一个node节点，每个节点有两个属性，一个children字典，一个end标志
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode() #相当于一个head节点
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() #c属于children的key；每个key-value对应的value是TrieNode      
            cur = cur.children[c]

        cur.end = True
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            if c in cur.children:
                cur = cur.children[c]
            
        return cur.end
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]

        return True
        
        