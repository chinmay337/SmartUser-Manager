users = {}

print("******************USER MANAGEMENT SYSTEM*****************")

choice = 0
while choice != 4:
    print("\n1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")
    
    choice = int(input("\nEnter Your Choice: "))
    if choice > 4:
        print("Invalid Choice!!! Please choose the correct option")
        choice = int(input("\nEnter Your Choice: "))
    
    if choice == 1:
        print("\n----Enter Your Registration Details----")
        username = input("Enter Your Name: ")
        
        if username in users:
            print("User Already Exists!!! Try Another Name")
            continue
        
        email = input("Enter Your Email: ")
        address = input("Enter Your Address: ")
        
        phone = input("Enter Your Phone Number (Must contain 10 digits): ")
        while len(phone) != 10 or not phone.isdigit():
            print("Invalid Number! It must be 10 digits.")
            phone = input("Enter Your Phone Number: ")

        password = input("Enter Your Password (At least 8 characters): ")
        while len(password) < 8:
            print("Invalid Password! Must contain at least 8 characters.")
            password = input("Enter Your Password: ")

        users[username] = {"email": email, "address": address, "phone": phone, "password": password}
        print(f"User {username} registered successfully!")

    elif choice == 2:
        print("\n----Enter Login Details----")
        username = input("Enter your Username: ")
        password = input("Enter Your Password: ")

        if username in users and users[username]["password"] == password:
            print("Login Successful!!")
        else:
            print("Invalid Username or Password")

    elif choice == 3:
        print("\n----Forgot Password----")
        username = input("Enter Username: ")

        if username in users:
            new_password = input("Enter New Password: ")
            users[username]["password"] = new_password
            print("Password Updated Successfully!")
        else:
            print("Username Not Found!!!!")

    elif choice == 4:
        print("----Thank you for using User Management System----")
        break

    else:
        print("Invalid Choice! Please enter again.")
