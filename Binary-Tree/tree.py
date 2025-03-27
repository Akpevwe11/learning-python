class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        if self.data > target:
            if self.left:
                return self.left.search(target)
        else:
            if self.right:
                return self.right.search(target)
        return None

    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)

    def height(self, h=0):
        left_height = self.left.height(h + 1) if self.left else h
        right_height = self.right.height(h + 1) if self.right else h
        return max(left_height, right_height)

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.getNodesAtDepth(depth - 1, nodes)
        if self.right:
            self.right.getNodesAtDepth(depth - 1, nodes)
        return nodes


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def traversePreorder(self):
        return self.root.traversePreorder()

    def traverseInorder(self):
        return self.root.traverseInorder()

    def traversePostorder(self):
        return self.root.traversePostorder()

    def height(self, h=0):
        return self.root.height()

    def __repr__(self):
        return self.name


## Testing the tree

tree = Tree(Node(50), 'Tree Traversals')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.right.left = Node(30)
tree.root.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)

print("Nodes at depth", tree.getNodesAtDepth(2))

print("Traverse Pre-Order")
tree.traversePreorder()

print("\nTraverse In-Order")
tree.traverseInorder()

print("\nTraverse Post-Order")
tree.traversePostorder()

print("Height of the tree:", tree.height())

shortTree = Tree(Node(50), 'Tree Traversals')
print("Height of the tree:", shortTree.height())

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)  ## smaller than 10 but should be larger than 5

node.right.left = Node(13)  ## smaller than 15 but should be larger than 10
node.right.right = Node(20)  ## larger than 15

## print(node.right.data)
## print(node.right.right.data)

print(node.search(15).data)
print(node.search(20).data)
