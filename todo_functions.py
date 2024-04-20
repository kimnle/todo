import csv

def add_todo(file_name):
    todo_name = input("Enter a to do item: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    todo_name = input("Enter the to do name that you want to delete: ")
    # Create new python list
    todo_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader: # [do grocery,False]
            if todo_name != row[0]: # do laundry != do grocery -> True 
                todo_lists.append(row) # [ [title,completed], [do grocery,False], [complete assignment,False] ]
            else:
                is_exist = True
        if not is_exist:
            print("No ite with that name exists.")
    # Write the enter list.csv with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo():
    print("Mark to do")

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                if row[1] == "True":
                    print(f"{row[0]} is completed.")
                else:
                    print(f"{row[0]} is not complete.")
    except FileNotFoundError:
        print("The to do file doesn't exist.")