from fastapi  import FastAPI

app = FastAPI()

tasks =["learn fastAPI" , "Set up linux"]
# first 1 -> get  ( read function )

@app.get("/tasks")
def  get_task():
   return  {"all tasks" : tasks}
# second one -> post ( create function )

@app.post("/tasks")
def add_task(new_task:str):
   tasks.append(new_task)
   return  {"message" : "task added" , "current list" : tasks}

# third one -> put ( update function)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_name:str):
    tasks[task_id] = updated_name
    return {"message" : "task list updated", "updated list" : tasks}

# fourth one -> delete ( delete function)

@app.delete("/tasks/{task_id}")
def delete_tasks(task_id:int):
    deleted_item = tasks.pop(task_id)
    return {"message" : "updated list after deleting" , "updated list" : tasks}

