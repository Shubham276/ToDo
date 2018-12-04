import pandas as pd
import re
import datetime
path = '/home/subham/PycharmProjects/ToDo-App/Todos/Assets/temp.csv'
now = datetime.datetime.now()
today = now.date()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)


def add_todo(input_string):
    status = '[X]'
    try:
        items = re.search(r"((((.*(?P<project>\+\w+).*)?)(?P<date>today|tomorrow|\d+.\d+.\d{2,}).*)?)"
                          r"(?P<message>.*(?P<context>(@\w+)).*)",
                          input_string, re.I)
    except ValueError:
        print("Invalid Ordering of input")

    # testing
    # print(items.group('project'))
    # print(items.group('date'))
    # print(items.group('context'))
    # print(items.group('message'))
    try:
        project = items.group('project')
    except ValueError:
        project = ""

    try:
        date_value = items.group('date')
        if date_value == 'today':
            date_value = str(today)
        elif date_value == 'tomorrow':
            date_value = str(tomorrow)
        else:
            date_value = items.group('date')
    except ValueError:
        date_value = ""

    try:
        context = items.group('context')
    except ValueError:
        context = ""

    try:
        message = items.group('message')
    except ValueError:
        message = ""

    df = pd.read_csv(path)
    count = int(df.list_number.tail(1).item())
    print(count)
    if count > 0:
        data = [(count + 1, status, project, date_value, context, message)]
    else:
        data = [(1, status, project, date_value, context, message)]
    # print(data)
    data_frame = pd.DataFrame(data=data, columns=['list_number', 'status', 'project', 'date', 'context', 'message'])
    try:
        with open(path, 'a') as csv_file:
            data_frame.to_csv(csv_file, header=False, index=False)
        print(data_frame.to_string(index=False))
    except FileNotFoundError as e:
        print(e)


def show_todo_values(filter_string):
    # list by project, date, context, completed
    csv_data = pd.read_csv(path)  # file
    data_frame = pd.DataFrame(data=csv_data)
    if filter_string == 'completed':
        filter_data = "status"
        try:
            list_of_values = data_frame.groupby(filter_data)  # column name
            for name, group in list_of_values:
                if name == '[✓]':
                    print(group.to_string(index=False))
        except KeyError:
            print("Invalid options --> Valid Options are <completed>|<project>|<date>|<context> ")
    else:
        try:
            list_of_values = data_frame.groupby(filter_string)  # column name
            for name, group in list_of_values:
                print(name)
                print(group.to_string(index=False))
        except KeyError:
            print("Invalid options --> Valid Options are <completed>|<project>|<date>|<context> ")


def delete_task(task_number):
    # put inside read_csv if needed
    # na_values = {'Department': ["not available", "n.a"],
    #              'Date': ["not available", "n.a"], 'Context': ["not available", "n.a"],
    #              'Message': ["not available", "n.a"]}
    data = pd.read_csv(path)
    data_frame = pd.DataFrame(data=data)
    index_names = data_frame[(data_frame['list_number'] == task_number)].index
    data_frame.drop(index_names, inplace=True)
    data_frame.to_csv(path, index=False)
    print(data_frame.to_string(index=False))


def mark_complete(task_number):
    data = pd.read_csv(path)
    data.loc[data['list_number'] == task_number, 'status'] = "[✓]"
    data.to_csv(path, index=False)
    print(data.to_string(index=False))


def extend_task(task_number, date):
    data = pd.read_csv(path)
    check = (data['list_number'] == task_number).any()
    if check:
        if date == 'tomorrow':
            data.loc[data['list_number'] == task_number, 'date'] = tomorrow
        elif date == 'today':
            data.loc[data['list_number'] == task_number, 'date'] = today
        else:
            data.loc[data['list_number'] == task_number, 'date'] = date
        data.to_csv(path, index=False)
        val_date = data[data['list_number'] == task_number]
        val_list_number = data[data['list_number'] == task_number]
        print(val_list_number.list_number.to_string(index=False)+" "+val_date.date.to_string(index=False))
        print(data.to_string(index=False))
    else:
        print("Wrong Task Value or Date")


def overdue_todo():
    data = pd.read_csv(path)  # file
    data_frame = pd.DataFrame(data=data)
    not_completed_data = data_frame[data_frame['status'] == "[X]"]
    list_values = not_completed_data.groupby("date")  # column name
    format1 = "%d/%m/%Y"
    format2 = "%Y-%m-%d"
    format3 = "%d-%m-%Y"
    format4 = "%Y/%m/%d"
    for date, group in list_values:
        try:
            date1 = datetime.datetime.strptime(date, format1)
            if date1.date() <= today:
                print(date1.date())
                print(group.to_string(index=False))
        except ValueError:
            pass
        try:
            date2 = datetime.datetime.strptime(date, format2)
            if date2.date() <= today:
                print(date2.date())
                print(group.to_string(index=False))
        except ValueError:
            pass
        try:
            date3 = datetime.datetime.strptime(date, format3)
            if date3.date() <= today:
                print(date3.date())
                print(group.to_string(index=False))
        except ValueError:
            pass
        try:
            date4 = datetime.datetime.strptime(date, format4)
            if date4.date() <= today:
                print(date4.date())
                print(group.to_string(index=False))
        except ValueError:
            pass


# extend_task(58, "tomorrow")
# show_todo_values("projet")
# add_todo("+android today meet @kk for +android")
# delete_task(101)
# overdue_todo()
# mark_complete(9779)

