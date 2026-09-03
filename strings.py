#Task: Vakidate user input 
#1.Username is no more than 12 characters 
#2.Usernames must not contain spaces
#3.Usernames must nit comtain digits 

username = input("Enter your username:")

if len(username) > 12:
	print("You have to have a username with less than 12 characters") #I used len() to help make sure that the username is no longer than 12 characters
elif not username.find(" ") == -1:
			print("You must not have spaces in your username") #I used .find() to help find any spaces in the username 
elif not username.isalpha():
	print("Your username cant have numbers included") #I used .isalpha() to help make sure that the username doesnt include digits
else:
		print(f"Welcome {username} nice to meet you!")
