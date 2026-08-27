import { useState } from "react";
import "./App.css";

function App() {
const [task, setTask] = useState("");
const [tasks, setTasks] = useState([]);

const addTask = () => {
if (!task.trim()) return;

setTasks([
  ...tasks,
  {
    id: Date.now(),
    text: task,
    completed: false,
  },
]);

setTask("");

};

const toggleTask = (id) => {
setTasks(
tasks.map((t) =>
t.id === id ? { ...t, completed: !t.completed } : t
)
);
};

const deleteTask = (id) => {
setTasks(tasks.filter((t) => t.id !== id));
};

return ( <div className="container"> <h1>📋 Task Management Dashboard</h1>

  <div className="input-section">
    <input
      type="text"
      placeholder="Enter a task..."
      value={task}
      onChange={(e) => setTask(e.target.value)}
    />
    <button onClick={addTask}>Add task</button>
  </div>

  <div className="stats">
    <p>Total: {tasks.length}</p>
    <p>Completed: {tasks.filter(t => t.completed).length}</p>
    <p>Pending: {tasks.filter(t => !t.completed).length}</p>
  </div>

  {tasks.map((task) => (
    <div className="task-card" key={task.id}>
      <div>
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => toggleTask(task.id)}
        />

        <span
          className={task.completed ? "completed" : ""}
        >
          {task.text}
        </span>
      </div>

      <button
        className="delete-btn"
        onClick={() => deleteTask(task.id)}
      >
        Delete
      </button>
    </div>
  ))}
</div>

);
}

export default App;
