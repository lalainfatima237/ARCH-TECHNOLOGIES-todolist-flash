async function addTask() {
    let input = document.getElementById("taskInput");
    let task = input.value.trim();
    if (!task) return alert("Enter a task");

    await fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({task})
    });
    input.value = "";
    window.location.reload();
}

async function editTask(index, oldTask) {
    let newTask = prompt("Edit task:", oldTask);
    if (!newTask) return;

    await fetch(`/edit/${index}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({task: newTask})
    });
    window.location.reload();
}

async function deleteTask(index) {
    await fetch(`/delete/${index}`, {method: "DELETE"});
    window.location.reload();
}
