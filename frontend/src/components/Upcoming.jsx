import React, {useState, useEffect} from "react";
import "../styles/Home.css"
import "../styles/Task.css"
import "../styles/Form.css"
import api from "../api";
function Upcoming({timestamp}) {
    const [Tasks, setTasks] = useState([])
    const [tasksDone, setTasksDone] = useState(false)

    const getTasks = async () => {
        const resp = await api.get(`api/tasks/nextmonth/?timestamp=${timestamp}`)
        let tasks = resp.data
        tasks.sort((a, b) => {
            if (a.task_date < b.task_date) return -1
            if (a.task_date > b.task_date) return 1
            return 0;
        })

        const updatedTasks = tasks.map((task) => {
            const newDate = new Date(task.task_date).toISOString().split("T")[0];
            return { ...task, task_date: newDate }; // Update the date field while preserving the rest
        });
        setTasks(updatedTasks)
        console.log("future tasks: " + resp.data.length)
    }

    useEffect(() => {
        getTasks()
    }, [])

    return (

        <div>
            <h2>Upcoming Tasks</h2>
            {Tasks.map((task) => (
                <h1>{task.title} - {task.task_date}</h1>
                ))}
        </div>
    )
}

export default Upcoming