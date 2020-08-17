# Login System Project

import time # to add sleep time between actions

def signup():
    ask_name = input("Name: ")
    ask_surname = input("Surname: ")

    emailAttempts = 100

    for x in range(emailAttempts):

        ask_email = input("Email:")

        if ask_email.count("@") == 1:  #If the input email has '@' then break the loop(email is valid), but if it does not have '@' ask 100 more times
            break
        else:
            print("Please enter a valid email address")
            x += 1

    ask_username = input("Username: ")
    ask_password = input("Password: ")

    confirmAttempts = 100

    for a in range(confirmAttempts):
        confirm_password = input("Confirm Password: ")

        if ask_password == confirm_password:  #If password is confirmed
            break
        else:                                 #If password is not confirmed
            print("Reenter your password")

    with open("info.txt","a",encoding = "utf-8") as newInfo:  #Adds new inputs to the info.txt file
        newInfo.write(ask_username)
        newInfo.write("\n")  #To enter a new line
        newInfo.write(ask_password)
        newInfo.write("\n")



#First ask user if they want to login or sign up

ask_action = input("Login or Sign-up: ")

# If the user selects to login

if ask_action == "login":
    attempt = 5
    for i in range(attempt):
        
        ask_username = input("Username: ")
        ask_password = input("Password: ")
        time.sleep(2)

        #Now that we took the inputs from the user we should check if these inputs match with the ones in the text file.(Assuming the user has an account already)
        
        userInfoList = []  # Empty list
        with open("info.txt","r",encoding="utf-8") as info:   #To read the text file named 'info.txt'.
            for line in info:
                line = line.strip("\n")  #For every line in info.txt strip the '\n' to remove whitespace
                userInfoList.append(line.split())  #line.split() returns every string into a list and adds them to the userInfoList

        username = ''.join(userInfoList[0])  #Takes the first item in userInfoList and joins with empty string to create one string which is the username saved in the info.txt
        password = ''.join(userInfoList[1])  #Takes the second item in userInfoList and joins with empty string to create one string which is the username saved in the info.txt

        if ask_username == username and ask_password == password:  #If both inputs are entered corrrectly
            time.sleep(0.5)  #Sleep 0.5 seconds
            print("Login Successful")
            break  # If login is successful do not check other options and end program
        
        elif ask_username != username and ask_password == password:  #If username is entered wrong but not the password
            print("Invalid Username")
                

        elif ask_username == username and ask_password != password:  #If username is correct but not the password
            print("Invalid Password")
               

        elif ask_username != username and ask_password != password:  #If both inputs are entered wrong
            print("Username and Password are invalid, please try again")

        i += 1  #increase i by 1

        if i == 5:  #If the attempt number is 5(i = 5) 
            print("You have exceeded your attempts, perhaps you do not have an account...\n")
            print("**********************************Sign-up**********************************\n")
            signup()  #Call signup function defined in the beginning

# If the user selects to signup            

elif ask_action == "signup":
    signup()  #Call signup function defined in the beginning


