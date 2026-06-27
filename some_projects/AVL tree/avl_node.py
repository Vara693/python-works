class AVLNode:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def update_height(self):
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        self.height = 1 + max(lh, rh)

    def balance_factor(self):
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        return lh - rh
