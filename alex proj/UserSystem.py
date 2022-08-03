from ast import Break
from fileinput import filename
from pickle import FALSE
from sys import breakpointhook
from User import user as createdUser
import CreateUser
import ast
import Matching
import urllib
import webbrowser
import time
import Main

"""
UserSystem.py does all the user cmd and save user information to UserCache.txt, and also match user.
"""


def main():
    currentuser = ""
    user_info = ""
    counter = 0
    signup = False
    justUpdatedInterests = False
    while True:
        if signup == False: 

            usercmd = input("What You Like To Do, (1) Sign Up, (3) Sign In, (4) Quit ")
        else:
            if justUpdatedInterests == True:
                usercmd = input("Thank you for updating interests! Please restart program and sign in to refresh our system: (4) Quit ")
            else:
                usercmd = input("What You Like To Do (2) Match Up, (4) Quit,  (5) Add Interest ")
        if usercmd == "1" and signup == False:
            items = CreateUser.main()
            currentuser = items[0]
            user_info = items[0]
            counter = items[1]
            signup = True
            justUpdatedInterests = False
        elif usercmd == "2":

            if user_info != "":
                username = ast.literal_eval(user_info)["username"]
                MatchUser = Matching.MatchUser(user_info, username) 
                # print(MatchUser)
                if MatchUser != "":
                    
                    print("You Are Matching With "+ ast.literal_eval(str(MatchUser))["username"] + ", WE ARE GOING TO SEND YOU BOTH TO A GOOGLE DOC")

                    time.sleep(5)
                    webbrowser.open("https://docs.google.com/document/d/1ww9t_2mnqMOK90e8IpXMNtUSEY8d_eEvNtyp4S-4Df8/edit?usp=sharing")
                justUpdatedInterests = False
        elif usercmd == "3":
            username = input("Input Your Username: ")
            file = open("UserCache.txt", 'r')
            reigstered_user = file.readlines()
            exist = False
            for user in reigstered_user:
                if exist == True:
                    file.close()
                    break
                


                user = str(user)
                user_info = ast.literal_eval(user)
                
                if ast.literal_eval(user_info)["username"] == username:
                    exist = True
                    currentuser = user
                    print("Login Successful")
                counter = counter + 1
            file.close()
            if exist == False:
                print(" User Not Found")          

            else:
                signup = True
            justUpdatedInterests = False
        elif usercmd == "5":
            FileName = input("What is Your txt file name ")
            FileName = FileName + ".txt"
            newinterest =  Main.run(FileName)
            user_info = ast.literal_eval(currentuser)
            oldinterests = ast.literal_eval(user_info)["interestList"]
            username = ast.literal_eval(user_info)["username"]
            userobject = createdUser(username, oldinterests)
            newinterests = userobject.assignlist(newinterest)

            open_dict = "\"{ "
            user_info = "\'username\': \'{}\', \'interestList\': {}".format(username, newinterests)
            closing_dict = "}\"\n"

            rpltext = open_dict + user_info + closing_dict
            #print(counter)
            replace_line("UserCache.txt", counter-1, rpltext)
            justUpdatedInterests = True
        
        else:
            break
            

        
def replace_line(file_name, line_num, rpltext):
    lines = open(file_name, "r").readlines()
    lines[line_num] = rpltext
    out = open(file_name, "w")
    out.writelines(lines)
    out.close()   
            

if __name__ == "__main__":
    main()


