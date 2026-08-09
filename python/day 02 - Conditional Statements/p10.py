username = "jhanavi"
password = 12345

entered_username = input("Enter the username: ")
entered_password = int(input("Enter the password: "))

if entered_username == username and entered_password == password:
    print("Login Successful")
else:
    print("Invalid Login")