import pandas as pd
import csv
import sys
user_id = 'dd'
password = 'test'
user_df = pd.read_csv('D:\G\Barn\\auth\\user_list.csv', index_col = False)

nf_user_df = user_df.loc[(user_df['user_id']== user_id) & (user_df['password'] == password)]

check_user_type = nf_user_df['type'] # this gets what type of user is this admin/customer
print(check_user_type)
# if nf_user_df['type'] == 'admin':  # if admin user then the admin func is called from the product class
#     y=admin()
#     y.admin_task()
# elif nf_user_df['type'] == 'cust': # if Customer user then product func is called from prodcut class
#     print("##########################################\n\n")
#     print("\t" + auth.wel_note)
#     print("\t****WELCOME CUSTOMER****\n\n")
#     print("##########################################")