from flask import Flask, jsonify, request
import main_demo as core

app = Flask(__name__)
core.load_tasks()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(core.list_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Task title required"}), 400
    task = core.add_task(data["title"])
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def mark_task_done(task_id):
    task = core.mark_done(task_id)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if core.delete_task(task_id):
        return jsonify({"success": True})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
