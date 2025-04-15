let todos = [
    { name: "Task 1", completed: false },
    { name: "Task 2", completed: true },
    { name: "Task 3", completed: false },];
  
const form = document.getElementById("add-todo-form");
const input = form.querySelector("input[name='todo-name']");
const clearAll = document.getElementById("todos-clear");
const todoList = document.getElementById("todo-list");
const counter = document.getElementById("count");

//------------------------------------------------

function render() {
    todoList.innerHTML = "";

    todos.forEach((todo, index) => {
        const li = createTodoElement(todo, index);
        todoList.appendChild(li);
    });

    const counterRemaining = todos.filter(todo => !todo.completed).length;
    counter.textContent = counterRemaining;
}

//------------------------------------------------

//creating one task
function createTodoElement(todo, index) {
    const li = document.createElement("li");
    li.className = "todo__container";
    if (todo.completed) {
        li.classList.add("todo__container--completed");
    }

    const nameDiv = document.createElement("div");
    nameDiv.className = "todo-element todo-name";
    nameDiv.textContent = todo.name;
    li.appendChild(nameDiv);

    //up button
    const upButton = createMoveButton("↑", () => moveUp(index), "move-up");
    li.appendChild(upButton);

    //down button
    const downButton = createMoveButton("↓", () => moveDown(index), "move-down");
    li.appendChild(downButton);

    //done / revert button
    const toggleButton = createToggleButton(todo, index);
    li.appendChild(toggleButton);

    //delete button
    const removeButton = createRemoveButton(index);
    li.appendChild(removeButton);

    return li;
}

//------------------------------------------------

function createMoveButton(text, fun, class_option) {
    const button = document.createElement("button");
    button.className = "todo-element todo-button " + class_option;
    button.textContent = text;
    button.onclick = fun;
    return button;
}

function moveUp(index) {

    if (index > 0) {
        [todos[index - 1], todos[index]] = [todos[index], todos[index - 1]];
        render();
    }
}

function moveDown(index) {

    if (index < todos.length - 1) {
        [todos[index + 1], todos[index]] = [todos[index], todos[index + 1]];
        render();
    }
}

// done / revert button
function createToggleButton(todo, index) {
    const button = document.createElement("button");
    button.className = "todo-element todo-button";
    button.textContent = todo.completed ? "Revert" : "Done";

    button.onclick = () => {
        todos[index].completed = !todos[index].completed;
        render();
    };
    return button;
}

function createRemoveButton(index) {
    const button = document.createElement("button");
    button.className = "todo-element todo-button";
    button.textContent = "Remove";

    button.onclick = () => {
        todos.splice(index, 1);
        render();
    };
    return button;
}

//------------------------------------------------

//adding a new task
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const newTodoName = input.value;

    if (newTodoName) {
        todos.push({ name: newTodoName, completed: false });
        input.value = "";
        render();
    }
});

//clearing all
clearAll.addEventListener("click", () => {
    todos = [];
    render();
});

//------------------------------------------------
render();
