import tkinter as tk


class TreeView:
    NODE_RADIUS = 18
    EDGE_COLOR = "#555555"

    COLORS = {
        "normal": "#E0E0E0",
        "highlight": "#FF9800",
        "search": "#2196F3",
        "insert": "#8BC34A",
        "delete": "#F44336",
    }

    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.show_labels = True  # height + BF toggle

    # -----------------------------
    # Main render entry
    # -----------------------------
    def render(self, step, layout):
        self.canvas.delete("all")
        tree = step["tree"]
        focus = set(step.get("focus", []))
        step_type = step.get("type")

        if not tree:
            return

        self._draw_edges(tree, layout)
        self._draw_nodes(tree, layout, focus, step_type)

    # -----------------------------
    # Drawing helpers
    # -----------------------------
    def _draw_edges(self, node, layout):
        if not node:
            return

        x1, y1 = layout[node["key"]]

        for child in ("left", "right"):
            c = node[child]
            if c:
                x2, y2 = layout[c["key"]]
                self.canvas.create_line(
                    x1, y1,
                    x2, y2,
                    fill=self.EDGE_COLOR,
                    width=2
                )
                self._draw_edges(c, layout)

    def _draw_nodes(self, node, layout, focus, step_type):
        if not node:
            return

        key = node["key"]
        x, y = layout[key]

        color = self._node_color(key, focus, step_type)

        # Node circle
        self.canvas.create_oval(
            x - self.NODE_RADIUS,
            y - self.NODE_RADIUS,
            x + self.NODE_RADIUS,
            y + self.NODE_RADIUS,
            fill=color,
            outline="#333333",
            width=2
        )

        # Key label
        self.canvas.create_text(
            x, y,
            text=str(key),
            font=("Arial", 11, "bold")
        )

        # Height + BF labels
        if self.show_labels:
            label = f"h={node['height']}  bf={node['bf']}"
            self.canvas.create_text(
                x, y + self.NODE_RADIUS + 10,
                text=label,
                font=("Arial", 8),
                fill="#333333"
            )

        self._draw_nodes(node["left"], layout, focus, step_type)
        self._draw_nodes(node["right"], layout, focus, step_type)

    # -----------------------------
    # Color logic
    # -----------------------------
    def _node_color(self, key, focus, step_type):
        if key in focus:
            if step_type in ("compare", "search", "found"):
                return self.COLORS["search"]
            if step_type == "insert_leaf":
                return self.COLORS["insert"]
            if step_type == "delete_node":
                return self.COLORS["delete"]
            return self.COLORS["highlight"]
        return self.COLORS["normal"]

    # -----------------------------
    # UI toggles
    # -----------------------------
    def toggle_labels(self):
        self.show_labels = not self.show_labels
