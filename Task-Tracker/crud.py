import os 
import json


file_path = "tasks.json" #default file path 


def get_id(filepath=file_path):
    data = json.load(filepath)
    
def add_task(task_json, filepath=file_path):
    
    with open(filepath, 'a') as file:
        file.write(task_json)
        
def clear_file(filepath = file_path):
    with open(filepath, 'w') as file:
        file.write('')
    