import os 
import json


file_path = "tasks.json" #default file path 

# def get_prev(filepath = file_path):
  
        

def get_id(filepath=file_path):
    with open(filepath,'r') as file:
        data = json.load(file)
    if data:
        ids = [task['id'] for task in data]
        return max(ids)
    else:
        return 0
    
    
    
def add_task(task_json, filepath=file_path): 
      if os.path.exists(file_path):
          
        with open(filepath, 'r') as file:
            db = json.load(file)
            if db:
                db.append(task_json)
            else:
                db = []
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
    