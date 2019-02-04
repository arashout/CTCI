class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        n = len(key)

        def _insert(parent, i):
            trie_key = key[i]
            if i == len(key) - 1:
                current = parent.children.get(trie_key[i], TrieNode(0))
                current.value += val
                return current.value
            else:

                if trie_key in node.children:
                    next_node = node.children[trie_key]
                    value = _insert(next_node, i+1)
                    next_node.value = value + (val - value) 
                    return val
                else:
                    new_node = TrieNode(0)
                    node.children[trie_key] = new_node
                    val = _insert(new_node, i+1)
                    new_node.value = val
                    return val
        
        _insert(self.root, 0)
    
    def __str__(self):
        def helper(node):
            if node:
                return str(node)
            else:
                return ''

        return helper(self.root)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        def _sum(node, i=0):
            key = prefix[i]
            if key not in node.children:
                return 0
            elif i < len(prefix):
                return _sum(node.children[key], i+1)
            else:
                return node.value    

        return self.root.value if prefix == '' else _sum(self.root, 0)

class TrieNode:
    def __init__(self, value=0):
        self.children = {}
        self.value = value
    
    def __str__(self):
        def helper(node, i):
            if len(node.children) == 0:
                return ' '*(i*2) + str(node.value) + '\n'
            else:
                return ' '*(i*2) + str(node.value) + ':' + '-'.join(node.children.keys()) + '\n' + ''.join([helper(c, i+1) for c in node.children.values()])

        return helper(self, 0)

commands = ["MapSum", "insert", "sum", "insert", "sum"]
inputs = [[], ["apple",3], ["ap"], ["app",2], ["ap"]]


ms = MapSum()
results = []
for c, args in zip(commands[1:], inputs[1:]):
    if c == 'insert':
        ms.insert(args[0], args[1])
        results.append(None)
    else:
        results.append(ms.sum(args[0]))

print(results)