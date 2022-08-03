from User import user
import Main


'''create a new user and store it in UserCache.txt.'''
reigster_user = "UserCache.txt"

def main():
    name = input("What can we call you?")                                                                                                                                                                                                                                                                                                                               
    file = open (reigster_user, 'a+')



    username = user(name, [])
    # interest = Main.run()
   
    interest = []
    interest = str(interest)
    interest.replace("'", '"')
              
    open_dict = "\"{ "
    user_info = "\'username\': \'{}\', \'interestList\': {}".format(name, interest)
    closing_dict = "}\"\n"

    new_user = open_dict + user_info + closing_dict
    file.write(new_user)
    file.seek(0) 
    reigster = file.readlines()
    filelen = len(file.readlines())
    file.close()

    username.assignlist(interest)
    return [new_user, filelen]


if __name__ == "__main__":
    main()

