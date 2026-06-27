class Controller:
    def __init__(self, tree, view, canvas):
        self.tree = tree
        self.view = view
        self.canvas = canvas

        self.steps = []
        self.index = 0

        self.playing = False
        self.speed_ms = 500
        self._after_id = None

    # =============================
    # Tree operations
    # =============================
    def insert(self, key):
        self._stop()
        self.steps = self.tree.insert(key)
        self.index = 0
        self._render_current()

    def delete(self, key):
        self._stop()
        self.steps = self.tree.delete(key)
        self.index = 0
        self._render_current()

    def search(self, key):
        self._stop()
        self.tree.search(key)
        self.steps = self.tree.steps
        self.index = 0
        self._render_current()

    def clear(self):
        self._stop()
        self.tree.root = None
        self.steps = []
        self.index = 0
        self.canvas.delete("all")

    # =============================
    # Playback controls
    # =============================
    def play(self):
        if not self.playing and self.steps:
            self.playing = True
            self._schedule_next()

    def pause(self):
        self._stop()

    def next_step(self):
        self._stop()
        if self.index < len(self.steps) - 1:
            self.index += 1
            self._render_current()

    def prev_step(self):
        self._stop()
        if self.index > 0:
            self.index -= 1
            self._render_current()

    def set_speed(self, ms):
        self.speed_ms = int(ms)

    # =============================
    # Internal helpers
    # =============================
    def _schedule_next(self):
        if not self.playing:
            return

        self._render_current()

        if self.index < len(self.steps) - 1:
            self.index += 1
            self._after_id = self.canvas.after(
                self.speed_ms, self._schedule_next
            )
        else:
            self._stop()

    def _render_current(self):
        if not self.steps:
            return

        step = self.steps[self.index]
        from layout import compute_layout

        layout = compute_layout(
            step["tree"],
            self.canvas.winfo_width()
        )

        self.view.render(step, layout)

    def _stop(self):
        self.playing = False
        if self._after_id:
            self.canvas.after_cancel(self._after_id)
            self._after_id = None
