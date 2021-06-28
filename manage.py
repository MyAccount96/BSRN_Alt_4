#!/usr/bin/python3
import string
import random
import pyperclip
import time
import sys
import getpass
from login_system import *

cmd = sys.argv[1]

if cmd == "CreateMaster":
	"""
	With this function a master user would be created 

	Input:
	Enter Username: masteruser (string)
	Enter Password: masterpassword (string)

	Output:
	New Master created
    """
	masteruser = input("Enter your MasterUser: ")
	masterpassword = getpass.getpass("Enter your Master-Password: ")
	add_new_master (masteruser, masterpassword)
	print("Master user has been created")
	 
elif cmd == "Add":
	"""
	With this function create an user, need master password.

	Input:
	Enter Master-Pass: password_master (string)
	Enter Username: username (string)
	Enter Password: password (string)
	Enter Title: title (string) 

	Output:
	New User created
    """
	password_master = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password_master)

	if verification_password:
		
		username = input("Enter Username: ")
		password = getpass.getpass("Enter Password: ")
		title = input("Enter Title: ")
		add_new_user (username, password, title)
		print("User account has been created")
	else: 
		print("Wrong Master-Password") 

elif cmd == "Delete":# -MasterUser -title -Username
	"""
	With this function the he user would delete an master
	The user has to confirm again with Yes or No if he wants to delete the password
	
	Input:
	masteruser: master_user (string)
	title_user: title (string)
	username_user: username (string)
	Enter Master-Pass: password_master (string) 
	Confirmation: Are you sure?: Yes/No (string)

	Output:
	Master deleted
    """
	master_user = sys.argv[2]
	title = sys.argv[3]
	username = sys.argv[4]
	password_master = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password_master)
	if verification_password:
		confirmation = input("Are you sure?: ") 
		if confirmation.lower() == "yes":
			del_existing_masters(master_user,password_master)
			print("Master was deleted.")
		elif confirmation.lower() == "no":
			print("Master was not deleted.")
	else:
		print("Wrong Master-Password")

elif cmd == "DeleteEntry":# -title
	"""
	With this function the he user would delete an entry
	The user has to confirm again with Yes or No if he wants to delete the password
	
	Input:
	title_user: title (string)
	Enter Master-Pass: password_master (string) 
	Confirmation: Are you sure?: Yes/No (string)

	Output:
	Entry deleted
    """
	title = sys.argv[2]
	password_master = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password_master)
	if verification_password:
		confirmation = input("Are you sure?: ") 
		if confirmation.lower() == "yes":
			del_existing_users(title)
			print("Entry was deleted.")
		elif confirmation.lower() == "no":
			print("Entry was not deleted.")
	else:
		print("Wrong Master-Password")

elif cmd == "Copy":# -MasterUser -title
	"""
	With this function you can get the password of a user, ready to paste it. 
	It will be stored in cache for 30 seconds or before if the script is stopped.
	
	Input:
	masteruser: master_user (string)
	title_user: title (string)

	Output:
	user_password stored in cache for 30 seconds. We use pyperclip.copy(user_password) to save the password in the cache.
    """
	try:
		master_user = sys.argv[2]
		title = sys.argv[3]
		password_master = getpass.getpass("Enter Master-Password: ")
		verification_password = master_pass_exists(password_master)
		if verification_password:
			username, password = get_user_pass_title(title)
			print(f"Usuario: {username}") 
			pyperclip.copy(password)
			print("Password was stored in the cache for 30s.") 
			time.sleep(30)
			pyperclip.copy('')
			print("Password was delete from cache.")
		else:
			print("Wrong Master-Password") 

	except KeyboardInterrupt:
		pyperclip.copy('')

elif cmd == "GeneratePassword": # -Lenght -Capital -SpecialCase
	"""
	With this function you generate a ramdom password with especific parameters and the ramdom_password will be ready to paste.
	
	Input:
	lenght: number (int)
	capital: Yes/No (string)
	specialcase: Yes/No (string)
	If none of the arguments have any values, they take the following default values:
		lenght: 8
		capital: Yes
		specialcase: Yes

	Output:
	random_password stored in cache. We use pyperclip.copy(user_password) to save the password in the cache.
    """
	try:
		try:
			length = int(sys.argv[2])
		except:
			length = 8
		try:
			capital = sys.argv[3].lower()
		except: 
			capital = "true"
		try: 
			specialcase = sys.argv[4].lower()
		except:
			specialcase = "true"
		lower = string.ascii_lowercase
		num = string.digits
	
		if capital  == "true":
			upper = string.ascii_uppercase
		elif capital == "false":
			upper = ""
		if specialcase == "true":
			symbols = string.punctuation 
		elif specialcase == "false":
			symbols = "" 

		all = lower + upper + num + symbols
		random_password = "".join(random.sample(all,length))
		print(random_password)
		pyperclip.copy(random_password)
		print("Password was stored in the cache.") 
	except: 
		print("Error!, some lost argument\nReminder arguments:-Length(int) -Capital(bool) -SpecialCase(bool)") 

elif cmd == "ExportAll":
	"""
	Reads the values stored in the users txt file

	Output: 
	username|password|title
	user1|upass1|title1
	user2|upass2|title2
	user3|upass3|title3
	user4|upass4|title4
	user5|upass5|title5
    """
	password = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password)

	if verification_password:
		print("Passwords stored.") 
		get_table_users()
	else:
		print("Wrong Master-Password") 


elif cmd == "ChangeMasterPassword":
	"""
	With this function a master would change a master password
	The new password requires a confirmation
	
	Input:
	Enter Master-User: user_master (string) 
	Enter Master-Pass: password_master (string) 
	New Master-Password: new_password (string)
	Confirm new Master-Password: confirm_new_password (string)  

	Output:
	The old password will be replace by the new password. We use change_pass_master(password_master, new_password) to change the password.
    """
	master_user = input(("Enter Master-User: "))
	password = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password)

	if verification_password:
		new_password = getpass.getpass("New Master-Password: ")
		confirm_new_password = getpass.getpass("Confirm new Master-Password: ")
		if new_password == confirm_new_password:
			change_pass_master(master_user,password, new_password)
			print("Master-Password changed.") 
		
		elif new_password != confirm_new_password:
			print("Passwords do not match.")
	else:
		print("Wrong Master-Password") 

elif cmd == "ChangeUserPassword": # -title -user
	"""
	With this function we can change the password of a user. 
	
	Input:
	title_user: title (string)
	username_user: username_user (string) 
	Enter User-Pass: password_old (string) 
	Enter Master-Pass: password_master (string) 
	Enter new password: password_new (string) 	

	Output:
	If user_pass_exists(password_old):
		change_password_user (username_user, title_user, password_old, password_new)
		"Password was changed"
	Else:
		"Incorrect user information entered || User not found"
	"""
	title_user = sys.argv[2]
	username_user= sys.argv[3]
	password_old = getpass.getpass("Enter User-Password: ")
	password_master = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password_master)

	if verification_password:
		password_new = getpass.getpass("Enter new password: ")
		if user_pass_exists(password_old):
			change_password_user (username_user, title_user, password_old, password_new)
			print("Password was changed")
		else: 
			print("Incorrect user information entered || User not found")
	else:
		print("Wrong Master-Password")

elif cmd == "ChangeUserUsername": # -title -user
	"""
	With this function we can change the username of a user. 
	
	Input:
	title_user: title (string)
	username_user: username_user (string) 
	Enter User-Pass: password_old (string) 
	Enter Master-Pass: password_master (string) 
	Enter new username: password_new (string) 	

	Output:
	If user_exists(username_user_old):
		change_username_user (username_user_old, title_user, password_user, username_user_new)
		"Username was changed"
	Else:
		"Incorrect user information entered || User not found"
	"""
	title_user = sys.argv[2]
	username_user_old= sys.argv[3]
	password_user = getpass.getpass("Enter User-Password: ")
	password = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password)

	if verification_password:
		username_user_new = input("Enter new username: ")
		if user_exists(username_user_old):
			change_username_user (username_user_old, title_user, password_user, username_user_new)
			print("Username was changed")
		else: 
			print("Incorrect user information entered || User not found")
	else:
		print("Wrong Master-Password")
		
elif cmd == "CheckPassword":
	"""
    With this function the master would check if a password has been used more than once for the same title. 
    All passwords are compared between them. 
    If passwords are the same. The output will be like: 
    Follow titles {title_with_the same_password} have the same password: {password}
	"""
	password = getpass.getpass("Enter Master-Password: ")
	verification_password = master_pass_exists(password)

	if verification_password:
		pass_duplicates = get_user_repeat_pass()
		if pass_duplicates == None: 
			print("No duplicates password.")
		else:
			print(pass_duplicates)
			print("Please change it.")
	else:
		print("Wrong Master-Password") 	

elif cmd == "Help":
	"""
	Reads the information of the commands stored in the information txt file
	"""
	get_commands_information()


