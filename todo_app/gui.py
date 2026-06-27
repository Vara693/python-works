import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit, QMessageBox
)

FILE_NAME = "tasks.json"
tasks = []
task_id = 1


# ---------------- Core Functions (from console app) ---------------- #
def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def load_tasks():
    global tasks, task_id
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks[:] = json.load(f)
        if tasks:
            task_id = max(task["id"] for task in tasks) + 1


def add_task(title):
    global task_id
    task = {"id": task_id, "title": title, "done": False}
    tasks.append(task)
    task_id += 1
    save_tasks()


def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks()
            return True
    return False


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            return True
    return False


# ---------------- PyQt GUI ---------------- #
class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App (PyQt)")
        self.setGeometry(200, 200, 400, 400)

        self.layout = QVBoxLayout()

        # Task List
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Input Box
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter new task...")
        self.layout.addWidget(self.input_box)

        # Buttons
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Task")
        self.done_btn = QPushButton("Mark as Done")
        self.del_btn = QPushButton("Delete Task")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.done_btn)
        btn_layout.addWidget(self.del_btn)
        self.layout.addLayout(btn_layout)

        self.setLayout(self.layout)

        # Button actions
        self.add_btn.clicked.connect(self.add_task_ui)
        self.done_btn.clicked.connect(self.mark_done_ui)
        self.del_btn.clicked.connect(self.delete_task_ui)

        # Load tasks on startup
        load_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        """Refresh the task list display."""
        self.task_list.clear()
        for task in tasks:
            status = "✔️" if task["done"] else "❌"
            self.task_list.addItem(f"{task['id']}. {task['title']} [{status}]")

    def add_task_ui(self):
        title = self.input_box.text().strip()
        if title:
            add_task(title)
            self.input_box.clear()
            self.refresh_tasks()
        else:
            QMessageBox.warning(self, "Error", "Task cannot be empty!")

    def mark_done_ui(self):
        selected = self.task_list.currentItem()
        if selected:
            tid = int(selected.text().split(".")[0])  # Extract task id
            if mark_done(tid):
                self.refresh_tasks()
        else:
            QMessageBox.warning(self, "Error", "Select a task first!")

    def delete_task_ui(self):
        selected = self.task_list.currentItem()
        if selected:
            tid = int(selected.text().split(".")[0])  # Extract task id
            if delete_task(tid):
                self.refresh_tasks()
        else:
            QMessageBox.warning(self, "Error", "Select a task first!")


# ---------------- Main ---------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
