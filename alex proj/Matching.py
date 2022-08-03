import ast
from tkinter import Y

''' Matching.py -   
    Takes current user's interests and compares it to all other user's interests.
    The user with the most similiar interests is matched with the current user.'''

def MatchUser(User_info, username):
    User_info = ast.literal_eval(User_info)
    CurrentUserInterest = User_info["interestList"]
    file = open("UserCache.txt", 'r')
    reigster_user = file.readlines()
    FindMatch = ""
    intersection = ""
    foundUser = ""
    intersection_size = 0
    for x in reigster_user:
        user = str(x)
        user =  ast.literal_eval(user)
        if username != ast.literal_eval(user)["username"]:

            FindMatch = ast.literal_eval(user)["interestList"]
            intersection = set(CurrentUserInterest).intersection(FindMatch)
            # print(intersection)
            if len(intersection) > 0 and intersection_size < len(intersection):
                foundUser = user
                intersection_size = len(intersection)
                

    return foundUser
        