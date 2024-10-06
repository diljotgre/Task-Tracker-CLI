import argparse
from modules.crud import add_task,clear_file,get_id, update_task, delete_task, list_tasks, list_type, mark
import os
from modules.model import Task, Test
import json
from datetime import datetime



def main():
    parser = argparse.ArgumentParser(description="Task Tracker")
    subparser = parser.add_subparsers(title = "Commands", dest = "command")
    
    add = subparser.add_parser('add', help="Add task")
    add.add_argument('add', type=str)
    update = subparser.add_parser('update', help= "Update Task")
    update.add_argument('update', nargs=2)
    delete = subparser.add_parser('delete', help = "Delete Task")
    delete.add_argument('delete', type=int, help = "Delete Task")
    mark_inprog = subparser.add_parser('mark-in-progress', help="Mark tasks in-progress" )
    mark_inprog.add_argument("inprogress", type = int)
    mark_todo = subparser.add_parser('mark-todo', help="Mark tasks todo" )
    mark_todo.add_argument("todo", type = int)
    mark_done = subparser.add_parser('mark-done', help="Mark tasks done" )
    mark_done.add_argument("done", type = int)
    
    

    list_parser = subparser.add_parser("list", help = "List all the tasks")
    
    
    
    list_subparsers = list_parser.add_subparsers(dest="type", help="Commands for list")
    
    todo = list_subparsers.add_parser("todo", help="List all the todo tasks")
    inprog = list_subparsers.add_parser("in-progress", help="List all the in-progress tasks")
    done = list_subparsers.add_parser("done", help="List all the done tasks")
    
    
    
    


    args = parser.parse_args()
    id_counter  =get_id()
    # clear_file()
    if args.command == 'add':        
        add_task(Task(id= id_counter+1, description= args.add, createdAt= datetime.now().isoformat(), updatedAt= datetime.now().isoformat()).json_custom())

    if args.command == 'update':
        update_task(id=int(args.update[0]), new_description=args.update[1], update= datetime.now().isoformat())
        
    
    if args.command == 'delete':
        delete_task(id=args.delete)
    
    if args.command == 'list':
        if args.type == 'todo':
            list_type(type = 'todo')
        elif args.type == 'done':
            list_type(type = 'done')
        elif args.type == 'in-progress':
            list_type(type = "in-progress")
        else:
            list_tasks()
    
    if args.command == 'mark-in-progress':
        mark(status = 'in-progress', id=args.inprogress)
    if args.command == 'mark-todo':
        mark(status = 'todo', id=args.todo)
    if args.command == 'mark-done':
        mark(status = 'done', id=args.done)

if __name__=='__main__':
    main()



