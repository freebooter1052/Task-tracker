import sys
import os
import json
from datetime import datetime


FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# command =sys.argv[1]

def generate_id(tasks):
    if not tasks:
        return 1
    return tasks[-1]["id"] +1

def add_tasks(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)

    task ={
        "id": task_id,
        "description":description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task_id})")

def update_tasks(task_id,new_description):
    tasks =load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id :
            task["description"] =new_description
            task["updatedAt"] =datetime.now().isoformat()
            save_tasks(tasks)
            print("updated task succesfully")
            return
        print("task not found")

def delete_tasks(task_id):
    tasks = load_tasks()

    tasks =[task for task in tasks if task["id"] !=task_id]
    save_tasks(tasks)

def markstatus(task_id,status):
    tasks =load_tasks()
    task_id=int(task_id)
    for task in tasks:
        if task["id"] == task_id :
            task["status"] = status
            task["updatedAt"] =datetime.now().isoformat()
            save_tasks(tasks)

            return

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f'{task["id"]} | {task["status"]} | {task["description"]}')

def main():
    if len(sys.argv) <2:
        print("Usage: python task_cli.py <command> [arguments]")
        return
    
    command =sys.argv[1]

    if command == "add" :
        add_tasks(sys.argv[2])
    if command == "update" :
        update_tasks(sys.argv[2],sys.argv[3])
    if command == "delete":
        delete_tasks(int(sys.argv[2]))
    if command == "mark-in-progress":
        markstatus(sys.argv[2],"in-progress")
    if command == "mark-done":
        markstatus(sys.argv[2],"done")
    if command =="list":
        list_tasks()
    
    

if __name__ == "__main__":
    main()