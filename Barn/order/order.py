import pandas as pd
import csv
import os
import sys
sys.path.append('D:\G\Barn\product\\')
from product import *

class create_order:
        wel_note = '*****WELCOME TO BARN COLLECTIONS***** \n'

        def __init__(self, product_id):
                self.product_id = product_id

        def order(self,product_id):

            print(create_order.wel_note)
            print("Product added to the CART")
            print("Please provide more information to complete the order")

            y = open('D:\G\Barn\product\product_list.csv', 'r', encoding='UTF8', newline='')

            read = csv.reader(y)
            next(read)

            for i in read:

                if int(i[0]) == product_id:  # this section searches the selected product from the list and
                                            # takes user input to add more information to the order
                    print(i)
                    add = input("add the address : ")
                    email = input("add the email address : ")
                    credit_card = input("enter credit card details : ")
                    i.append(add)
                    i.append(email)
                    i.append(credit_card)
                    print("credit added")
                    z = open('D:\G\Barn\order\order_list_new1.csv', 'a', encoding='UTF8', newline='')
                    wrt = csv.writer(z)
                    wrt.writerow(i)
                    print("\n\n========================================================")
                    print("Please see below Order confirmation detils ")
                    print("========================================================")

                    print("Product ordered : " + str(i[2]) + " -------------- Price: " + str(i[6]))
                    print("------------------------------------------------------------------------")
                    print("Colour:" + str(i[3]) + " ,Size" + str(i[5] + " , "))
                    print("Address : " + str(i[7]) )
                    b=str(i[9])
                    print("Last 4 digits of Credit Card : **** **** **** " + b[-4:])
                    print("=========================================================")
                    y.close()
                    z.close()
                    print("closing")

            print("Order added")


            print("Press 1 to go to the main menu")
            print("Press 2 to go to exit")
            choice = int(input("enter the choice"))
            match choice:
                case 1:
                    x = product('Male')
                    x.type('Male')
                case 2:
                    sys.exit()
                case _:
                    print("Invalid choice")
                    x = product('Male')
                    x.type('Male')


