#!/usr/bin/python3
masters_credentials = "/home/sept/projects/python/passwordmanager/masters_credentials.txt"
users_credentials = "/home/sept/projects/python/passwordmanager/users_credentials.txt"
commands_information = "/home/sept/projects/python/passwordmanager/commands_information.txt"
def get_existing_masters():
    """
    This command splits the stored masters data into username ansd password.
    """
    with open(masters_credentials, "r") as f:
        next(f)
        for line in f:
            line = line.strip()
            master, password = line.split("|")
            yield master, password
    f.close()

def get_existing_users():
    """
    This command splits the stored users data into username, password and title.
    """
    with open(users_credentials, "r") as f:
        next(f)
        for line in f:
            line = line.strip()
            user, password, title = line.split("|")
            yield user, password, title
    f.close()

def master_pass_exists(password):
    """
    Verify if the entered password is inside the stored master passwords, use (get_existing_masters()) to get the passwords. 
    If it is not found, the script will stop. If it is found the script will continue.

    Input: password (string)
    Output: True||False (boolean)
    """
    return any((masters_pass == password) for _, masters_pass in get_existing_masters())

def user_exists(username):
    """
    Verify if the entered parameter is inside the stored user usename, use (get_existing_users()) to get the usernames. 
    If it is not found, the script will stop. If it is found the script will continue.

    Input: username (string)
    Output: True||False (boolean)
    """
    return any((usr_name == username) for usr_name, _, _ in get_existing_users())

def user_pass_exists(password):
    """
    Verify if the entered parameter is inside the stored user passwords, use (get_existing_users()) to get the passwords.  
    If it is not found, the script will stop. If it is found the script will continue.

    Input: password (string)
    Output: True||False (boolean)
    """
    return any((usr_pass == password) for _, usr_pass, _ in get_existing_users())

def get_user_pass_title(title_input):
    """
    Verifies that the title entered is inside the stored users, if is found, obtains the index to which it belongs, 
    with the index obtains the user and password as a return. 
    """
    if any((titles == title_input) for users, passwords,titles in get_existing_users()):
        with open(users_credentials, "r") as f:
            next(f)
            users = []
            passwords = []
            titles = []
            for line in f:
                line = line.strip()
                user, password, title = line.split("|")
                users.append(user)
                passwords.append(password)
                titles.append(title)
            index = titles.index(title_input)
            user_password = passwords[index]
            user_name = users[index]
        f.close()
    return user_name, user_password

def get_line_number(file, parameter_1, parameter_2):
    """
    Finds the line in the text file where both parameters are found.

    Input:
    file: path file (string)
    parameter1 (string)
    parameter2 (string)

    Output:
    Line number where match both parameters (int)
    """
    with open(file) as f:
        for num, line in enumerate(f, 0):
            if (parameter_1 and parameter_2) in line:
                return num

def get_line_number_user(file, parameter_1, parameter_2, parameter_3):
    """
    Finds the line in the text file where both parameters are found.

    Input:
    file: path file (string)
    parameter1 (string)
    parameter2 (string)

    Output:
    Line number where match both parameters (int)
    """
    with open(file) as f:
        for num, line in enumerate(f, 0):
            if (parameter_1 and parameter_2 and parameter_3) in line:
                return num


def get_line_number_title(file, title):
    """
    Finds the line in the text file where title are found.

    Input:
    file: path file (string)
    title (string)

    Output:
    Line number where match with the title given
    """
    with open(file) as f:
        for num, line in enumerate(f, 0):
            if title in line:
                return num

def del_existing_masters(master_user,password_master):
    """
    Deletes the master that matches the master_user and password_master input.
    
    Input:
    master_user (string)
    password_master (string)

    Output:
    Delete the line with the master_user and password_master given.
    """
    match_line = get_line_number(masters_credentials, master_user, password_master)
    old_file = open(masters_credentials, "r")
    lines = old_file.readlines()
    old_file.close()
    del lines[match_line]
    lines[(len(lines)-1)] = lines[(len(lines)-1)].replace('\n','')

    new_file = open(masters_credentials, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def del_existing_users(title):
    """
    Deletes the user that matches the master_user and password_master input.
    
    Input:
    title (string)

    Output:
    Delete the line with the user_title given.
    """
    match_line = get_line_number_title(users_credentials, title)
    old_file = open(users_credentials, "r")
    lines = old_file.readlines()
    old_file.close()
    del lines[match_line]
    lines[(len(lines)-1)] = lines[(len(lines)-1)].replace('\n','')

    new_file = open(users_credentials, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def get_table_users():
    """
    Reads the values stored in the users_credentials.txt file 
    """
    with open(users_credentials) as f:
        contents = f.read()
        print(contents)
    f.close()

def get_user_repeat_pass():
    """
    With this function the master would check if a password has been used more than once for the same title. 
    All passwords are compared between them. 
    If passwords are the same. The output will be like: 
    Follow titles {title_with_the same_password} have the same password: {password}
    """ 
    with open(users_credentials, "r") as f:
        next(f)
        users = []
        passwords = []
        titles = []
        for line in f:
            line = line.strip()
                
            user, password, title = line.split("|")
            users.append(user)
            passwords.append(password)
            titles.append(title)
    
    f.close()
    list_set = set(passwords)
    unique_pass_list = (list(list_set))
    for password_unique in unique_pass_list:
        index_pos_list = []
        for i in range(len(passwords)):
            if passwords[i] == password_unique:
                title_repeat = titles[i]
                index_pos_list.append(title_repeat)
        if len(index_pos_list) > 1:
            return f"Follow titles {index_pos_list} have the same password: {password_unique}"
        else:
            pass

def change_pass_master(master_user, password_old, password_new):
    """
    Searches for the old password in the masters_credentials file that stores the masters data and replaces it with the new password.
    """
    match_line = get_line_number(masters_credentials, master_user, password_old)
    old_file = open(masters_credentials, "r")
    lines = old_file.readlines()
    old_file.close()
    lines[match_line] = lines[match_line].replace(password_old, password_new)
    new_file = open(masters_credentials, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def change_password_user(username_user, title_user, password_old, password_new):
    """
    Searches for the old password in the users_credentials file that stores the masters data and replaces it with the new password.
    """

    match_line = get_line_number_user(users_credentials, username_user, password_old, title_user)
    old_file = open(users_credentials, "r")
    lines = old_file.readlines()
    old_file.close()
    lines[match_line] = lines[match_line].replace(password_old, password_new)
    new_file = open(users_credentials, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def change_username_user(username_user_old, title_user, password, username_user_new):
    """
    Searches for the old password in the users_credentials file that stores the masters data and replaces it with the new password.
    """

    match_line = get_line_number_user(users_credentials, username_user_old, password, title_user)
    old_file = open(users_credentials, "r")
    lines = old_file.readlines()
    old_file.close()
    lines[match_line] = lines[match_line].replace(username_user_old, username_user_new)
    new_file = open(users_credentials, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

def append_new_line(file_name, text_to_append):
    """
    a a line to a file with a specific text.

    Input:
    file_name: path file (string)
    text_to_append: storage_format (string)

    Output:
    New line (master || user) create  
    """
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)
        
def add_new_master (username, password):
    """
    The inputs are used to transform them according to storage format of masters_credentials.txt.
    Storage_format = "{username}|{password}"
    With the correct format, it will be added to the file that stores the masters.
    Input:
    username (string)
    password (string)

    Output:
    New master added to the file masters_credentials.txt
    """
    storage_format = f"{username}|{password}"
    append_new_line(masters_credentials, storage_format)

def add_new_user (username, password, title):
    """
    The inputs are used to transform them according to storage format of users_credentials.txt.
    Storage_format = "{username}|{password}|{title}"
    With the correct format, it will be added to the file that stores the users.

    Input:
    username (string)
    password (string)
    title (string)

    Output:
    New user added to the file users_credentials.txt
    """
    storage_format = f"{username}|{password}|{title}"
    append_new_line(users_credentials, storage_format)

def get_commands_information():
    """
    Reads the values stored in the users_credentials.txt file 
    """
    with open(commands_information) as f:
        contents = f.read()
        print(contents)
    f.close()