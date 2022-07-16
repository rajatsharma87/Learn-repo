import pandas as pd
import csv
import os
import sys
sys.path.append('D:\G\Barn\order\\')
from order import *

class product:
    wel_note = '*****WELCOME TO BARN COLLECTIONS***** \n'
    def __init__(self,Gender): # gender is passed from the login case 1 section
        self.Gender = Gender

    def type(self,Gender):
        #global wel_note
        print("##########################################\n\n")
        print("\t" + product.wel_note)
        print("##########################################")
        print( "****"+ Gender + " SECTION****")

        df = pd.read_csv('D:\G\Barn\product\product_list.csv')
        Men_prod = df[(df['Gender']) == self.Gender]  # filters data based on the gender selected
        Men_prod1= Men_prod[["Prod_Id","Category","Gender"]] # limited columns are displayed for user to select the required product for more details
        print(Men_prod1)

        prod_name=input("Enter the product name to see more details: ")
        prod_name_capitalise=prod_name.capitalize() # this handles the upper and lower case mismatch
        print(prod_name_capitalise)
        Men_prod2 = df[(df['Category'] == prod_name_capitalise)] # based on the product name, all the matching product row is fetched and displayed
        print(product.wel_note)
        print(Men_prod2)
        product_id = int(input("Enter product id you want to buy: "))
        product_selected_buy =  df[(df['Category'] == product_id)] # based on the unique product id the product row is fetched and displayed
        add_to_cart = int(input("Select 1 to add product in cart or select 0 to go to Main Menu: "))


        match add_to_cart:
            case 1: # after user selects to add to cart this section calls the order file/class to get order details and save it in file
                print(product.wel_note)
                print("Order added")
                x = create_order(product_id)
                x.order(product_id)
            case _:
                x=product(self.Gender).type(self.Gender)



class admin(product):
    Wel_admin_note = '****WELCOME ADMIN USER****'
    def __init__(self):
        # self.admin = admin
        pass

    def admin_task(self):
        print("##########################################\n\n")
        print("\t" + product.wel_note)
        print("\t" + admin.Wel_admin_note + "\n\n")
        print("##########################################")
        print("Select 1 to ADD product")
        print("Select 2 to DELETE product")
        print("Select 3 to EXIT")

        add_delete_prod = int(input("Please select your Choice : "))

        product_row=[]

        match add_delete_prod:
            case 1: # this section add the new product to the list
              prod_id = input("Prod_id : ")
              prod_name = input("Prod_name : ")
              category = input("Category : ")
              colour = input("Colour : ")
              gender = input("Gender : ")
              size = input("Size : ")
              price = input("Price : ")
              product_row.append(prod_id)
              product_row.append(prod_name)
              product_row.append(category)
              product_row.append(colour)
              product_row.append(gender)
              product_row.append(size)
              product_row.append(price)


              f = open('D:\G\Barn\product\product_list.csv', 'a', encoding='UTF8')
              wrt = csv.writer(f)

              wrt.writerow(product_row)
              f.close()
              print("Congrats ! PRODUCT WAS SUCCESSFULLY ADDED")
              x = admin()
              x.admin_task()

            case 2: # this section deletes the product by simply moving all the products to new file and then renaming it as old file
                prod_id = int(input("Please enter the prod ID you want to delete : "))

                z = open('D:\G\Barn\product\product_list.csv', 'r', encoding='UTF8', )
                lt = []
                for row in csv.reader(z):
                    if row[0].isnumeric():
                        a = int(row[0])
                        if a != prod_id:
                            y = open('D:\G\Barn\product\product_list_new.csv', 'a', encoding='UTF8', newline='')
                            wrt = csv.writer(y)
                            wrt.writerow(row)
                            print(row)
                    else:
                        print(row)
                        p = open('D:\G\Barn\product\product_list_new.csv', 'w', encoding='UTF8', newline='')
                        wrt1 = csv.writer(p)
                        wrt1.writerow(row)

                z.close()
                os.remove('D:\G\Barn\product\product_list.csv')
                os.rename('D:\G\Barn\product\product_list_new.csv','product_list.csv')

                print("Congrats ! PRODUCT WAS SUCCESSFULLY DELETED")
                x = admin()
                x.admin_task()

            case 3:
                sys.exit()

            case _:
                print("What is going on")
                x = admin()
                x.admin_task()


