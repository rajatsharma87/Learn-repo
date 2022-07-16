import pandas as pd
import csv
import sys
sys.path.append('D:\G\Barn\product\\')
from product import *
from product import *

class auth:

    wel_note = '****WELCOME TO BARN***** \n'
    def login(self):
        try:
            print("##########################################\n\n")
            print("\t" + auth.wel_note)
            print("##########################################")
            print("please select from below options")
            # Here we are selecting the login or Sign up
            print("\t 1. Press \"1\" to LOGIN")
            print("\t 2. Press \"2\" to SIGN UP")
            print("\t 3. Press \"3\" to Quit")
            login_option = int(input("Please select your option : "))

            match login_option:
                case 1:  # This section is for authorised user to login into the application
                    user_id = input("User ID: ")
                    password = input("Password: ")
                    with open('D:\G\Barn\\auth\\user_list.csv', newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            #Here we are validating the user
                            if row['user_id'] == user_id and row['password'] == password:

                                check_user_type = row['type'] # this gets what type of user is this admin/customer
                                if check_user_type == 'admin':  # if admin user then the admin func is called from the product class
                                    y=admin()
                                    y.admin_task()
                                elif check_user_type == 'cust': # if Customer user then product func is called from prodcut class
                                    print("##########################################\n\n")
                                    print("\t" + auth.wel_note)
                                    print("\t****WELCOME CUSTOMER****\n\n")
                                    print("##########################################")

                                    male = input("please enter Male/Female: ") # here it is asking the user if they wat to see Male or female clothes
                                    male1 = male.capitalize()
                                    match male1:
                                        case 'Male':
                                            x = product(male1)
                                            x.type(male)
                                        case 'Female':
                                            x = product(male1)
                                            x.type(male)
                                        case _:                     # if other than Male/Female option is used then this section will be called
                                            print("invalid choice")
                                            z = auth()
                                            z.login()
                                else:
                                    print("Invalid role")
                            #else:
                             #   print("Please check user name and password")
                        print("Enter Correct Usename/Password")
                        z = auth()
                        z.login()


                case 2: # This section is used for the sign-up or adding new user
                    print("Please provide your Name,user ID, password and address to Sign UP")
                    p = []
                    d = input("please enter your name: ")
                    e = input("please enter User ID: ")
                    f = input("Please enter the Password: ")
                    g = input("Please enter the Addres: ")
                    p.append(d)
                    p.append(e)
                    p.append(f)
                    p.append(g)
                    print(p)

                    f = open('user_list.csv','a',encoding='UTF8')

                    wrt = csv.writer(f)

                    wrt.writerow(p)
                    f.close()
                    x = auth()
                    x.login()

                case 3: # Used if user wants to exit the application
                    #quit()
                    sys.exit()
                case _: # handles any invalid options
                    print("Invalid option")
                    x = auth()
                    x.login()


        except (ValueError) as ERROR:  # tried my best to handle the exceptions but need more research on it
            print("enter the number please")
        except pandas.errors.EmptyDataError:
            print("please select correct values")



