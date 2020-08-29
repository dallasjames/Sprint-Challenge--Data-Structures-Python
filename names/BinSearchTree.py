class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right == target:
                return True
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left == target:
                return True
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            return True
