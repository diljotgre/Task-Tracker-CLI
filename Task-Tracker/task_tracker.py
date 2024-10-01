import argparse
from crud import add_task,clear_file
import os
from model import Task, Test
import json
from datetime import datetime



def main():
    parser = argparse.ArgumentParser(description="Task Tracker")
    
    parser.add_argument('--add', type=str, help='Add task')
    parser.add_argument('--update', type=str, help='Update Task')
    parser.add_argument('--delete', type=str, help = "Delete Task")


    args = parser.parse_args()

    # clear_file()
    if args.add:        
        add_task(Task(id=1, description= args.add, createdAt= datetime.now(), updatedAt= datetime.now() ).model_dump_json(indent=4))

    

if __name__=='__main__':
    main()



