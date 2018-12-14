ToDo Requirements:

Note: Problems for Windows Users
Change path in Todo.py file Line 4 as according to your path.

List of Libraries Imported:   
1).Argparse statement: import argparse  
2).Pandas statement: import pandas as pd  
3).CSV statement: import csv  
4).Re(Regular Expression) statement: import re  
5).Datetime statement: import datetime

--> Recommended to use Python 3.6 -->
Features

Add Todo  
List Todo (by Date, by Context, by Project, by Completed Status)  
Delete Todo  
Extend Todo  
Overdue  
Marking a Uncompleted Todo to Completed  


# How to run:
1). Move to the directory which contains "ToDo.py" module.(Todo/Todos/CLI/ToDo.py)  
2). Open console/command prompt from that path  
3). Write command as follows:  
  Example:  
  python3.6 Todo.py todo -add "+python today @Tutorial download from github"  
  python3.6 Todo.py todo -add "+android tomorrow @Andy send apk"  
  python3.6 Todo.py todo -delete 21  
  python3.6 Todo.py todo -delete 201  
  python3.6 Todo.py todo -extend 9779 today  
  python3.6 Todo.py todo -extend 9779 12-08-2019  
  python3.6 Todo.py todo -complete 9779  
  python3.6 Todo.py todo -complete 9778  
  python3.6 Todo.py todo -overdue  
  python3.6 Todo.py todo -list "date"  
  python3.6 Todo.py todo -list "project"  
  python3.6 Todo.py todo -list "context"  
  python3.6 Todo.py todo -list "completed"  
