class BinaryNode:
    data = 0
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    
class BinaryOrderedTree:
    def __init__(self):
        self.root = None
        
    def addNode(self, data):
        return BinaryNode(data)
    
    def insert(self, root, data):
        if root and data != root.data:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root
        else:
            return self.addNode(data)
            
    def lookup(self, root, target):
        if root:
            if target == root.data:
                return True
            elif target < root.data:
                return self.lookup(root.left, target)
            else:
                return self.lookup(root.right, target)
        else:
            return False
        
    def minValue(self, root):
        if root:
            while(root.left):
                root = root.left
            return root.data
        else:
            return 0
    
    def maxDepth(self, root):
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1
        else:
            return 0
        
    def size(self, root):
        if root:
            return self.size(root.left) + 1 + self.size(root.right)
        else:
            return 0

    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.data)
            self.printTree(root.right)
            
    def printRevTree(self, root):
        if root:
            self.printTree(root.right)
            print(root.data)
            self.printTree(root.left)
           
    