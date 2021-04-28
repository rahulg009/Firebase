# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:26:17 2021

@author: Rahul
"""

import pyrebase
import urllib

firebaseConfig = {
    'apiKey': "AIzaSyCvD8vWeyx5rA6VyzmsJQcWlmzAmg27rds",
    "databaseURL" : "",
    'authDomain': "fir-rg-8e296.firebaseapp.com",
    'projectId': "fir-rg-8e296",
    'storageBucket': "fir-rg-8e296.appspot.com",
    'messagingSenderId': "774016773412",
    'appId': "1:774016773412:web:b81be5d5f879db78e217b1",
    'measurementId': "G-4HL8PQ6L40"}
firebase=pyrebase.initialize_app(firebaseConfig)

# db= firebase.database()
# auth=firebase.auth()
storage=firebase.storage()
# Upload
filename=input("Enter name of the file you want to upload")
cloudfilename=input("Enter Name of the file on the cloud")
storage.child(cloudfilename).put(filename)

print(storage.child(cloudfilename).get_url(None))


#download
cloudfilename=input("Enter name of the file on the cloud you want to download")

try:
    storage.child("googlestry.txt").download("", "downloaded.txt")
    print("Downloaded")
    
except:
    print("Error")
    
# readingfile
cloudfilename=input("Enter name of the file on the cloud you want to read")

url=storage.child(cloudfilename).get_url(None)
f= urllib.request.urlopen(url).read()
print(f)

