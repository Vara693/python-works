def compute_layout(tree, canvas_width, level_gap=80, node_gap=40):
    """
    Computes x,y positions for each node using subtree widths.
    """

    positions = {}
    widths = {}

    # -----------------------------
    # First pass: compute subtree widths
    # -----------------------------
    def compute_width(node):
        if not node:
            return 0

        lw = compute_width(node["left"])
        rw = compute_width(node["right"])

        if lw == 0 and rw == 0:
            w = node_gap
        else:
            w = lw + node_gap + rw

        widths[node["key"]] = w
        return w

    total_width = compute_width(tree)

    # -----------------------------
    # Second pass: assign positions
    # -----------------------------
    def assign(node, x_center, level):
        if not node:
            return

        key = node["key"]
        x = x_center
        y = level * level_gap
        positions[key] = (x, y)

        lw = widths.get(node["left"]["key"], 0) if node["left"] else 0
        rw = widths.get(node["right"]["key"], 0) if node["right"] else 0

        if node["left"]:
            left_x = x_center - (rw + node_gap) / 2
            assign(node["left"], left_x, level + 1)

        if node["right"]:
            right_x = x_center + (lw + node_gap) / 2
            assign(node["right"], right_x, level + 1)

    # Initial center
    assign(tree, total_width / 2, 1)

    # -----------------------------
    # Normalize to canvas width
    # -----------------------------
    xs = [x for x, _ in positions.values()]
    if xs:
        min_x, max_x = min(xs), max(xs)
        span = max_x - min_x if max_x != min_x else 1

        scale = min(1.0, canvas_width / (span + node_gap))
        offset = (canvas_width - span * scale) / 2

        for k, (x, y) in positions.items():
            nx = (x - min_x) * scale + offset
            positions[k] = (nx, y)

    return positions
