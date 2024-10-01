import os 
import json


file_path = "tasks.json" #default file path 

# def get_prev(filepath = file_path):
  
        

# def get_id(filepath=file_path):
#     with open(filepath,'r') as file:
#         data = json.load(file)
#     ids = [task.get('id') for task in data]
#     print(ids) 
    
    
    
def add_task(task_json, filepath=file_path): 
      if os.path.exists(file_path):
        with open(filepath, 'r') as file:
            db = json.load(file)
            db.append(task_json)
            with open(filepath, 'w') as file:
                json.dump(db,file,indent=2)
        
        
      else:
        db = []
        db.append(task_json)   
        with open(filepath, 'w') as file:
            json.dump(db,file,indent=2)

        
def clear_file(filepath = file_path):
    with open(filepath, 'w') as file:
        file.write('')
    