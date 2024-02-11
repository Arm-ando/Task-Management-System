# Importing datetime to be used
import datetime

# Creating 6 Functions overall for later use in the program.

# Function 1: 'reg_user' is called when the user selects 'r' to register a user
def reg_user(menu):

    # if statement for the menu choice
    if menu == 'r':
        new_user = input("Welcome to registering a new user!\nPlease enter a new username: ")

        # checking if the username already exists in the username variable
        # user is prompted to try again if username already exists
        while new_user in username_list:
            print("The username is already listed. Please try another username.")

            new_user = input("\nPlease enter a new username: ")

        # if not in username user in prompted to enter the password twice for confirmation
        if new_user not in username_list:
            new_password = input("\nPlease enter a new password: ")
            pass_confirm = input("\nPlease enter your new password again for confirmation: ")
            if new_password == pass_confirm:
                print("\n\nPassword confirmed!")

                # username and password are written into the 'user.txt' text file
                with open('user.txt', 'a+') as user:
                    user.write(f"\n{new_user}, {new_password}")

            # user prompted to try again if the passwords do not much
            else:
                print("\nPasswords do not match, please try again!")

        # message returned at the end of function
        return "Your new username and password have been successfully added."

# Function 2: add_task is called when user selects 'a' in order to add a new task
def add_task(menu):
    if menu == "a":

        print("\nWelcome to adding a task!")

        # requesting user input and storing in variables
        assigned_user = input("\nHi, please enter the username of whom the task is assigned to: ")
        assigned_task = input("Please enter the title of the task: ")
        assigned_taskdesc = input("Please enter the description of the task: ")
        assigned_duedate = input("Please enter the due date in DD MMM YYYY (e.g. 30 Dec 2022) format: ")
        current_date = input("Please enter the current date in DD MMM YYYY (e.g. 30 Dec 2022) format: ")
        complete = input("Is the task completed?")

        # opening task text file and writing the users input
        with open('tasks.txt', 'a+') as tasks:
            print("\nAdding task to the system...")
            tasks.write(
                f"\n{assigned_user}, {assigned_task}, {assigned_taskdesc}, {assigned_duedate}, {current_date} "
                f"{complete}")

        # return message when function is complete
        return ("\nTask has been added to the system.")

# Function 3: view_all is called when a user selects 'va' in order to view all tasks
def view_all(menu):
    if menu == 'va':
        print("\nWelcome to view all tasks!")

        # opening tasks text file for reading
        with open('tasks.txt', 'r') as view:

            # for loop to iterate through the textfile and split method
            for lines in view:
                view_split = lines.split(", ")

                # printing the username, task.. etc in a user friendly manner
                print(f"""

                Username:           {view_split[0]} 
                Task:               {view_split[1]}
                Description:        {view_split[2]} 
                Due date:           {view_split[3]}
                Current date:       {view_split[4]}
                Completed:          {view_split[5]} 

                """)
    # return message
    return "End of view all tasks!"

# Function 4: view_mytask when user selects 'vm' to view all the tasks assigned to them
def view_mytask(menu):
    if menu == 'vm':
        print("Welcome to view my tasks!")

        # opening task text file for reading with readlines method
        with open('tasks.txt', 'r+') as file:
            contents = file.readlines()

            # for loop to iterate through the task with enumerate function and storing informaation in value and task variable
            for value, task in enumerate(contents):

                # if the entered_login is = the username, then it displays their tasks
                # task number is stored in the 'value' variable
                if entered_login == task.split(", ")[0]:
                    print(f"""                                                                                      

                    Task Number:            {value}                                                                 
                    Assigned to user:       {task.split(", ")[0]}                                                   
                    Date assigned:          {task.split(", ")[3]}                                                   
                    Due date:               {task.split(", ")[4]}                                                   
                    Task Complete?          {task.split(", ")[5]}                                                   
                    Task description:                                                                               
                        {task.split(", ")[2]}                                                                       
                    """)

            # requesting user input whether they want to edit a task or return to the main menu
            # data of task number stored in task_num so it can be used to see what task the user wants to edit
            task_num = int(input("\nPlease select a task by number to edit (e.g. 1, 2, 3) or "
                                 "enter '-1' to return to the main menu."
                                 "\nEnter selection here: "))

            # Assigning task_num as key in content to call out the entire task and store in split_data variable
            split_data = contents[task_num].split(", ")

            # if statement for when user decides to exit
            if task_num == -1:
                print("To menu..")

                return (menu)

            # else statement for when they choose to edit task
            else:

                # requesting user input for whether they want to edit the task as complete or edit the task
                option = int(input("""                                                                              

                Would you like to assign the task as complete or edit the task?                                     

                Please enter an option:                                                                             
                1 - Assign task as complete                                                                         
                2 - Edit task                                                                                       

                Enter selection here (Type '1' or '2'): """))

                # if statement for when user wants to mark task as complete
                if option == 1:
                    split_data[5] = "Yes\n"
                    join_data = ", ".join(split_data)
                    contents[task_num] = join_data

                    # task rewritten into task text file
                    file.write(f"\n{contents[task_num]}")

                    return("Your task has been marked as completed!")

                # elif statement for when user decides to edit task
                elif option == 2:

                    # request user input whether they want to edit the username or due date
                    option_choice = input("""                                                                           
                    Would you like to edit the task username or due date?                                               

                    Edit task username - type 'u'                                                                       
                    Edit due date - type 'd'                                                                            

                    Enter here: """).lower()

                    # if statement for when user decides to edit username
                    if option_choice == 'u':
                        username_edit = input("Please enter a new username for the task: ")
                        split_data[0] = username_edit

                        join_data = ", ".join(split_data)

                        contents[task_num] = join_data

                        # writing the edited username in tasks text file
                        file.write(f"\n{contents[task_num]}")

                        print("The due date has been successfully changed.")

                    # elif statement for when user decides to change due date
                    elif option == 'd':
                        due_date_edit = input("Please enter a new date in DD MMM YYYY format (e.g. 27 DEC 2022: ")
                        split_data[3] = due_date_edit
                        join_data = ", ".join(split_data)

                        contents[task_num] = join_data

                        file.write(f"\n{contents[task_num]}")

                        print("The due date has been successfully changed.")

                # elif option if the tasks that has been marked as complete cannot be edited
                elif option == 2 and contents[task_num][5] == "Yes":
                    return ("Error! You can only edit tasks that are not already complete.")


# Function 5: 'generate' to generate reports
def generate(menu):
    if menu == 'gr':
        print("Welcome to generate reports!")

        file_content = {}

        # opening task text file for reading
        with open('tasks.txt', 'r') as file:
            contents = file.readlines()

        # empty list to append to later
        task_empty = []

        # for loop to iterate through the task text file with enumerate function
        # appending the count to the empty list
        for count, task in enumerate(contents):
            num = count
            task_empty.append(num)

        # acquiring the length of the task list to generate a number
        total_number_tasks = len(task_empty)

        # Setting my 3 control variables at zero
        completed = 0
        incomplete = 0
        overdue = 0

        # for loop to iterate through task text file in contents
        for line in contents:
            split_list = line.split(", ")

            # creating dictionaries and assigning keys 'completed' and 'due date'
            task_details = {'completed': split_list[5]}
            task_date = {'due date': split_list[4]}

            key = task_date['due date']

            # if statement for whether 'Yes' is in completed
            if "Yes" in task_details['completed']:

                # variable increase by one if task is marked as completed
                completed += 1

            # elif statement for whether 'No' is in completed
            elif "No" in task_details['completed']:

                # variable increase by one if task is not completed
                incomplete += 1

            # if statement whereby if the current date is greater than the due date, the 'overdue' variable increases by one
            if datetime.datetime.now() > datetime.datetime.strptime(key, '%d %b %Y'):
                overdue += 1

            # creating percentages of incomplete and overdue tasks are store in variable
            percent_incomplete = incomplete / total_number_tasks * 100
            percent_overdue = (overdue / total_number_tasks) * 100

        # opening 'task_overview' text file for reading and writing
        with open('task_overview.txt', 'w+') as task_overview:

            # writing completed tasks.. etc in a user friendly manner
            task_overview.write(
                f"""Total users:                {total_number_tasks}
    Completed tasks:            {completed}
    Uncompleted tasks:          {incomplete}
    Tasks overdue:              {overdue}
    Tasks incomplete (%):       {percent_incomplete}%
    Tasks overdue (%):          {percent_overdue}%
    """)
        print("Information has been successfully transferred to 'task_overview.txt' text file")

        # opening task overview task file to be read and display its contents in a friendly manner to the user
        with open('task_overview.txt', 'r') as t_overview:
            print("\nReports: ")
            for line in t_overview:
                print(line)

# Function 6: 'Display' for when user chooses to display statistics
def display(menu):
    if menu == 'd':

        # setting my control variables at zero
        task_no = 0
        user_no = 0

        # opening task text file for reading only
        with open('tasks.txt', 'r') as file:

            # for loop to iterate through the file
            # increase control variable by one after each loop
            for line in file:
                task_no += 1

        # opening task text file for reading only
        with open('user.txt', 'r') as users:

            # for loop to iterate through the file
            # increase control variable by one after each loop
            for line in users:
                user_no += 1

        # opening task text file for reading only
        with open('tasks.txt', 'r') as file:
            contents = file.readlines()

        # empty list to append to later
        task_empty = []

        # for loop to iterate through the task text file with enumerate function
        # appending the count to the empty list
        for count, task in enumerate(contents):
            num = count
            task_empty.append(num)

        # acquiring the length of the task list to generate a number
        total_number_tasks = len(task_empty)

        with open('tasks.txt', 'r') as task_file:

            # assigning my counter variables as zero
            no_assigned = 0
            percent_assigned_completed = 0
            percent_assigned_incomplete = 0
            percent_assigned_overdue = 0

            # for loop to gather username, complete and date using slicing methods
            for line in task_file:
                task_split = line.split(", ")

                task_username = task_split[0]
                task_complete = task_split[5]
                task_date = task_split[4]
                task_details = {'completed': task_split[5]}

                # if statement for when the user that is logged in, their select information is displayed and gathered
                if entered_login == task_username:
                    no_assigned += 1

                    if "Yes" in task_complete:
                        percent_assigned_completed += 1

                    elif "No" in task_complete:
                        percent_assigned_incomplete += 1

                    if datetime.datetime.now() > datetime.datetime.strptime(task_date, '%d %b %Y'):
                        percent_assigned_overdue += 1

        # opening user overview text file for reading and writing
        with open('user_overview', 'w+') as user_overview:

            # writing completed tasks.. etc in a user friendly manner
            user_overview.write(
                f"""The total number of tasks is: {task_no}
    The total number of users is: {user_no}

    The total number of tasks assigned to {entered_login}: {no_assigned}
    The percentage of the total number of tasks assigned to {entered_login}: {round((no_assigned / total_number_tasks) * 100, 2)}%
    The percentage of tasks completed assigned to {entered_login} : {round((percent_assigned_completed / no_assigned) * 100, 2)}%
    The percentage of tasks incomplete assigned to {entered_login} : {round((percent_assigned_incomplete / no_assigned) * 100, 2)}%
    The percentage of tasks incomplete and overdue assigned to {entered_login} : {round((percent_assigned_overdue / no_assigned) * 100, 2)}%
    """)
        print("Information has been successfully transferred to 'user_overview.txt' text file")

        # opening user overview task file to be read and display its contents in a friendly manner to the user
        print("\nStatistics: ")
        with open('user_overview', 'r') as u_overview:
            for line in u_overview:
                print(line)


# The actual program
# Welcoming user
print("Hi Welcome! \nTo login, enter your username and password below.")

# input command to request user to enter their login and store in variables
entered_login = input("\nPlease enter your username: ")
entered_password = input("\nPlease enter your password: ")

# opening user text file for reading
with open('user.txt', 'r') as u:
    data = u.readlines()


username_list = []
password_list = []

# for loop to iterate through text file
# string split and slicing methods to obtain username and password
for i in range(len(data)):
    user = data[i].strip("\n").split(", ")
    username_list.append(user[0])
    password_list.append(user[1])


# if statement to verify login
if entered_login in username_list and entered_password == password_list[username_list.index(entered_login)]:
    print("Logging you in...")

    # while loop to ensure that is the user is the admin then a specific menu displays
    while entered_login == "admin":

        menu = input('''\nWelcome to the Menu!                  
                         \nSelect one of the following Option below:          
                         r - Registering a user                     
                         a - Adding a task                          
                         va - View all tasks                        
                         vm - view my task 
                         gr - Generate reports
                         d - display statistics                         
                         e - Exit                                   

                         Enter here: ''').lower()

        # if statement for when user chooses t register new user
        # calling reg_user function
        if menu == 'r':
            reg_user(menu)

        # elif statement for when user chooses to add task
        # calling add_task function
        elif menu == 'a':
            add_task(menu)

        # elif statement for when the user chooses view all tasks
        # calling view_mytask function
        elif menu == 'va':
            view_all(menu)

        # elif statement for when user chooses view my task
        # calling view_all function
        elif menu == 'vm':
            view_mytask(menu)

        # elif statement for when user chooses to generate reports
        # calling generate function
        elif menu == 'gr':
            generate(menu)

        # elif statement for when user chooses to display statistics
        # calling display function
        elif menu == 'd':
            display(menu)

        # elif statement to exit program
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

    # else statement for all other users
    else:
        menu = input('''\nWelcome to the Menu!                              
                                      \nSelect one of the following Option below:                                    
                                      a - Adding a task                                  
                                      va - View all tasks                                
                                      vm - View my task
                                      gr - Generate reports                                                    
                                      e - Exit                                           

                                      Enter here: ''').lower()

        # elif statement for when user chooses to add task
        # calling add_task function
        if menu == 'a':
            add_task(menu)

        # elif statement for when the user chooses view all tasks
        # calling view_mytask function
        elif menu == 'va':
            view_all(menu)

        # elif statement for when user chooses view my task
        # calling view_all function
        elif menu == 'vm':
            view_mytask(menu)

        # elif statement for when user chooses to generate reports
        # calling generate function
        elif menu == 'gr':
            generate(menu)

        # elif statement to exit program
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

# else statement for when username or password is incorrect
else:
    print("Incorrect username or password. Please try again.")
