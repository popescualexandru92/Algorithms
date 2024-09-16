class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def depth_first_traversal(self):
        print(self.value)
        for child in self.children:
            child.depth_first_traversal()

    def breadth_first_traversal(self):
        queue = [self]
        while queue:
            current = queue.pop(0)
            print(current.value)
            queue.extend(current.children)

    def search(self, value):
        if self.value == value:
            return self
        for child in self.children:
            found = child.search(value)
            if found:
                return found
        return None

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_child(self, child_value, parent_value=None):
        if parent_value == None:
             parent_node = self.root
        else:
            parent_node=self.root.search(parent_value)        
        if parent_node:
            parent_node.add_child(TreeNode(child_value))
        else:
            print(f"Parent {parent_value} not found.")

    def DFT(self):
        print("Depth First Traversal:")
        self.root.depth_first_traversal()

    def BFT(self):
        print("Breadth First Traversal:")
        self.root.breadth_first_traversal()

    def find_max_depth(self):
        def max_depth(node):
            if not node.children:
                return 1
            else:
                return 1+ max(max_depth(child) for child in node.children)
        return max_depth(self.root)

    def minimax(self, node, depth, maximizing_player):
        if not node.children or depth == 0:
            return node.value

        if maximizing_player:
            max_eval = float('-inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    
tree=Tree(0)
tree.add_child(1)
tree.add_child(4)
tree.add_child(7)
tree.add_child(2,1)
tree.add_child(3,1)
tree.add_child(5,4)
tree.add_child(6,4)
tree.add_child(8,7)
tree.add_child(9,7)
tree.add_child(10,2)
tree.add_child(12,2)
tree.add_child(23,8)
tree.add_child(24,8)
tree.add_child(56,24)

# print(tree.find_max_depth())

print(tree.minimax(tree.root,tree.find_max_depth(),False))