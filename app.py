from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Add Task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.json.get("task")
    if task:
        tasks.append(task)
    return jsonify({"tasks": tasks})

# Edit Task
@app.route("/edit/<int:index>", methods=["PUT"])
def edit_task(index):
    new_task = request.json.get("task")
    if 0 <= index < len(tasks) and new_task:
        tasks[index] = new_task
    return jsonify({"tasks": tasks})

# Delete Task
@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(debug=True)
