# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:50:38 2021

@author: Rahul
"""

import pyrebase

firebaseConfig = {

    "databaseURL" : "",
    'authDomain': "fir-rg-8e296.firebaseapp.com",
    'projectId': "fir-rg-8e296",
    'storageBucket': "fir-rg-8e296.appspot.com",
    'messagingSenderId': "774016773412",
    'appId': "1:774016773412:web:b81be5d5f879db78e217b1",
    'measurementId': "G-4HL8PQ6L40"}
firebase=pyrebase.initialize_app(firebaseConfig)

# db= firebase.database()
auth=firebase.auth()
# storage=firebase.storage()


#Authentication
#login

email=input("Enter Your Email")
password=input("Enter Your Password")

try:
    auth.sign_in_with_email_and_password(email, password)
    print("Succesfully SignedIn")
    
except:
    print("Invalid User Or Password")

#signup

email=input("Enter @email")
password=input("Enter Password")
confirm_Password=input("Enter Password Again")

if(password==confirm_Password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Succesfully Signedup")
        
    except:
        print("User Already Exist")
        
    