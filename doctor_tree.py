class DoctorNode:
    def __init__(self, name):
        self.name=name
        self.left=None
        self.right=None
class DoctorTree:
    def __init__(self):
        self.root=None
    def insert(self, parent_name, employee_name, side):
        if self.root is None:
            print("Error: No root set yet.")
            return
        parent=self._find(self.root, parent_name)
        if parent is None:
            print(f"Error: Parent '{parent_name}' not found.")
            return
        if side=="left":
            if parent.left is None:
                parent.left=DoctorNode(employee_name)
            else:
                print(f"Error: Left side of {parent_name} is already occupied.")
        elif side=="right":
            if parent.right is None:
                parent.right=DoctorNode(employee_name)
            else:
                print(f"Error: Right side of {parent_name} is already occupied.")
        else:
                print(f"Error: Side must be 'left' or right'.")
    def _find(self, node, target):
        if node is None:
            return None
        if node.name==target:
            return node
        left_result=self._find(node.left, target)
        if left_result:
            return left_result
        return self._find(node.right, target)
    def preorder(self, node):
        if node is None:
            return []
        result=[node.name]
        result+=self.preorder(node.left)
        result+=self.preorder(node.right)
        return result
    def inorder(self, node):
        if node is None:
            return []
        result=[]
        result+=self.inorder(node.left)
        result.append(node.name)
        result+=self.inorder(node.right)
        return result
    def postorder(self, node):
        if node is None:
            return []
        result=[]
        result=self.postorder(node.left)
        result+=self.postorder(node.right)
        result.append(node.name)
        return result
if __name__=="__main__":
    tree=DoctorTree()
    tree.root=DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
