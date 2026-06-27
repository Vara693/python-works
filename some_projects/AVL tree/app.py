import tkinter as tk
from tkinter import ttk, messagebox

from avl_tree import AVLTree
from view import TreeView
from controller import Controller


class AVLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AVL Tree Visualizer")
        self.root.geometry("1100x700")

        self.tree = AVLTree()

        self._build_ui()

    # =============================
    # UI construction
    # =============================
    def _build_ui(self):
        # ---------- Top bar ----------
        top = ttk.Frame(self.root, padding=6)
        top.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(top, text="Key:").pack(side=tk.LEFT)
        self.entry = ttk.Entry(top, width=10)
        self.entry.pack(side=tk.LEFT, padx=4)

        ttk.Button(top, text="Insert", command=self.insert).pack(side=tk.LEFT)
        ttk.Button(top, text="Delete", command=self.delete).pack(side=tk.LEFT)
        ttk.Button(top, text="Search", command=self.search).pack(side=tk.LEFT)
        ttk.Button(top, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=10)

        # ---------- Main content ----------
        main = ttk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)

        # Left panel
        left = ttk.Frame(main, width=250, padding=6)
        left.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(left, text="Operation Log").pack(anchor="w")
        self.log = tk.Text(left, height=15, state=tk.DISABLED)
        self.log.pack(fill=tk.BOTH, expand=True)

        # Canvas
        self.canvas = tk.Canvas(main, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ---------- Bottom bar ----------
        bottom = ttk.Frame(self.root, padding=6)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        ttk.Button(bottom, text="◀ Step", command=self.prev_step).pack(side=tk.LEFT)
        ttk.Button(bottom, text="▶ Play", command=self.play).pack(side=tk.LEFT)
        ttk.Button(bottom, text="❚❚ Pause", command=self.pause).pack(side=tk.LEFT)
        ttk.Button(bottom, text="Step ▶", command=self.next_step).pack(side=tk.LEFT)

        ttk.Label(bottom, text="Speed").pack(side=tk.LEFT, padx=10)
        self.speed = ttk.Scale(
            bottom, from_=1000, to=100, value=500,
            command=self.set_speed
        )
        self.speed.pack(side=tk.LEFT)

        ttk.Button(bottom, text="Toggle h/BF", command=self.toggle_labels).pack(
            side=tk.RIGHT
        )

        # ---------- MVC wiring ----------
        self.view = TreeView(self.canvas)
        self.controller = Controller(self.tree, self.view, self.canvas)

        self.canvas.bind("<Configure>", self._on_resize)

    # =============================
    # Controller wrappers
    # =============================
    def insert(self):
        key = self._get_key()
        if key is not None:
            self.controller.insert(key)
            self._log(f"Insert {key}")

    def delete(self):
        key = self._get_key()
        if key is not None:
            self.controller.delete(key)
            self._log(f"Delete {key}")

    def search(self):
        key = self._get_key()
        if key is not None:
            self.controller.search(key)
            self._log(f"Search {key}")

    def clear(self):
        self.controller.clear()
        self._log("Tree cleared")

    def play(self):
        self.controller.play()

    def pause(self):
        self.controller.pause()

    def next_step(self):
        self.controller.next_step()

    def prev_step(self):
        self.controller.prev_step()

    def set_speed(self, value):
        self.controller.set_speed(value)

    def toggle_labels(self):
        self.view.toggle_labels()
        self.controller._render_current()

    # =============================
    # Helpers
    # =============================
    def _get_key(self):
        try:
            return int(self.entry.get())
        except ValueError:
            messagebox.show_error("Invalid input", "Please enter an integer key.")
            return None

    def _log(self, msg):
        self.log.config(state=tk.NORMAL)
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)
        self.log.config(state=tk.DISABLED)

    def _on_resize(self, event):
        self.controller._render_current()


# =============================
# Entrypoint
# =============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AVLApp(root)
    root.mainloop()

