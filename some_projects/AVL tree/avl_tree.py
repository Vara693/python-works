from avl_node import AVLNode
import copy


class AVLTree:
    def __init__(self):
        self.root = None
        self.steps = []

    # -----------------------------
    # Public API
    # -----------------------------
    def insert(self, key):
        self.steps.clear()
        self.root = self._insert(self.root, key)
        self._emit("done", message=f"Insert {key} complete")
        return list(self.steps)

    def delete(self, key):
        self.steps.clear()
        self.root = self._delete(self.root, key)
        self._emit("done", message=f"Delete {key} complete")
        return list(self.steps)

    def search(self, key):
        self.steps.clear()
        node = self.root
        while node:
            self._emit("compare", focus=[node.key])
            if key == node.key:
                self._emit("found", focus=[node.key])
                return True
            node = node.left if key < node.key else node.right
        self._emit("not_found")
        return False

    # -----------------------------
    # Core AVL logic
    # -----------------------------
    def _insert(self, node, key):
        if not node:
            new = AVLNode(key)
            self._emit("insert_leaf", focus=[key])
            return new

        self._emit("compare", focus=[node.key])

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            self._emit("duplicate", focus=[node.key])
            return node

        node.update_height()
        self._emit("update_height", focus=[node.key])

        return self._rebalance(node)

    def _delete(self, node, key):
        if not node:
            return None

        self._emit("compare", focus=[node.key])

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            self._emit("delete_node", focus=[node.key])

            if not node.left:
                return node.right
            if not node.right:
                return node.left

            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        node.update_height()
        self._emit("update_height", focus=[node.key])

        return self._rebalance(node)

    # -----------------------------
    # Rotations & rebalance
    # -----------------------------
    def _rebalance(self, node):
        bf = node.balance_factor()
        self._emit("rebalance_check", focus=[node.key])

        # LL
        if bf > 1 and node.left.balance_factor() >= 0:
            return self._rotate_right(node)

        # LR
        if bf > 1 and node.left.balance_factor() < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RR
        if bf < -1 and node.right.balance_factor() <= 0:
            return self._rotate_left(node)

        # RL
        if bf < -1 and node.right.balance_factor() > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        self._emit(
            "rotate_left",
            focus=[x.key, y.key],
            message=f"Rotate left at {x.key}"
        )

        y.left = x
        x.right = T2

        x.update_height()
        y.update_height()

        self._emit("update_height", focus=[x.key, y.key])
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        self._emit(
            "rotate_right",
            focus=[y.key, x.key],
            message=f"Rotate right at {y.key}"
        )

        x.right = y
        y.left = T2

        y.update_height()
        x.update_height()

        self._emit("update_height", focus=[y.key, x.key])
        return x

    # -----------------------------
    # Helpers
    # -----------------------------
    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # -----------------------------
    # Instrumentation
    # -----------------------------
    def _emit(self, step_type, focus=None, message=""):
        self.steps.append({
            "type": step_type,
            "focus": focus or [],
            "message": message,
            "tree": self._serialize(self.root)
        })

    def _serialize(self, node):
        if not node:
            return None
        return {
            "key": node.key,
            "height": node.height,
            "bf": node.balance_factor(),
            "left": self._serialize(node.left),
            "right": self._serialize(node.right)
        }
