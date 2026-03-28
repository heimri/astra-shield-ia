from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory data store
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build an API", "done": False},
]


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled"),
        "done": False,
    }
    tasks.append(task)
    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    task["done"] = data.get("done", task["done"])
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
