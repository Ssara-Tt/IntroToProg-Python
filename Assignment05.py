# --------------------------------------------------------- #
# Title: To Do List
# Description: Working with Dictionaries and Files
# #            When the program starts, load each "row" of data
# #            in "ToDoList.txt" into a python Dictionary.
# #            Add the each dictionary "row" to a python list "table"
# Name: Sara Tupponce
# Date: 05/08/2021
# Change Log:
#     STupponce - 05/08/2021 - imported starter script
#     STupponce - 05/08/2021 - added code for step 1-4
#     STupponce - 05/08/2021 - tested script
# --------------------------------------------------------- #


# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

dataFile = open(objFile, 'r')
for row in dataFile:
    strData = row.split(',')  # split() returns a list object
    dicRow = {'task': strData[0], 'priority': strData[1].strip()}
    lstTable.append(dicRow)
dataFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(row['task'] + ',' + row['priority'].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        newTask = str(input('Enter a new task: '))
        newPri = str(input('Enter a priority: '))
        dicRow = {'task': newTask, 'priority': newPri}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        deleteTask = str(input('Enter task that you would like to delete: '))
        for row in lstTable:
            if row['task'].lower() == deleteTask.lower():
                lstTable.remove(row)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        dataFile = open(objFile, 'w')
        for row in lstTable:
            dataFile.write(row['task'] + ',' + row['priority'] + '\n')
        dataFile.close()
        print('Task saved to ToDoList.txt file...')
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print('Exiting Program...')
        break  # and Exit the program
