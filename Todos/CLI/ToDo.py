#! /usr/bin/env python
import argparse
import sys
sys.path.append("/home/subham/PycharmProjects/ToDo-App/")
from Todos.Scripts.Script import add_todo, delete_task, mark_complete, show_todo_values, extend_task, overdue_todo
task_index = 0
date_index = 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="ToDo")
    parser.add_argument("todo", nargs=1, help="todo options[-add|-delete|-extend|-complete|list]")
    parser.add_argument("-add", help="todo -add <+project_name due date | today | tomorrow message>", type=str)
    parser.add_argument("-delete",  help="todo -delete task-number", type=int)
    parser.add_argument("-extend", nargs=2, help="todo -extend task-number due-date")
    parser.add_argument("-complete", help="todo -complete task-number", type=int)
    parser.add_argument("-overdue", help="todo -overdue task-number", action="store_true")
    parser.add_argument("-list",
                        help="list options[project_name | completed | date | context]",
                        type=str)
    args = parser.parse_args()
    if args.add:
        add_to_todo = args.add
        # print(b)
        add_todo(add_to_todo)
    elif args.delete:
        delete_todo = args.delete
        # print(delete_todo)
        delete_task(delete_todo)
    elif args.extend:
        extend_todo = args.extend
        task_number = int(extend_todo[task_index])
        extend_to_date = extend_todo[date_index]
        # print(task_number, extend_to_date, type(extend_to_date))
        extend_task(task_number, extend_to_date)
    elif args.list:
        category = args.list
        # print(category)
        show_todo_values(category)
    elif args.overdue:
        over = args.overdue
        # print(over)
        overdue_todo()
    elif args.complete:
        mark_completed = args.complete
        # print(over)
        mark_complete(mark_complete)





