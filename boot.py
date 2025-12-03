import os
import time
import random
import requests
import hashlib

        
def create_account(username, password):
    # Encode strings to bytes
    username_bytes = username.encode('utf-8')
    password_bytes = password.encode('utf-8')
    
    # Proper way: get the hex digest as string
    username_hash = hashlib.sha512(username_bytes).hexdigest()
    password_hash = hashlib.sha512(password_bytes).hexdigest()
    
    # Or even better: use a single line with both (common format)
    line = f"{username_hash}:{password_hash}\n"
    file_path = r"C:\\Users\\User\\Desktop\\BlackFox_toolkit_v2\\filesystem\\~\\User\\security\\login_sha512.txt"
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(line)  # write(), not writelines() for a single line
def c():
    os.system("cls")
def login():
    passes=[]
    usrs=[]
    with open("C:\\Users\\User\\Desktop\\BlackFox_toolkit_v2\\filesystem\\~\\User\\security\\login_sha512.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            usr_temp,pass_temp=line.split(":")
            usrs.append(usr_temp)
            passes.append(pass_temp[:-1])
        print("done reading passes and users")
    username=input("username:")
    password=input("password:")
    c()
    
    username_bytes = username.encode('utf-8')
    password_bytes = password.encode('utf-8')
    
    username = hashlib.sha512(username_bytes).hexdigest()
    password = hashlib.sha512(password_bytes).hexdigest()
    
    
    if username not in usrs and password not in passes:
        print("wrong credentials.")
        time.sleep(3)
        c()
        return (False)
    else:
        if usrs.index(username) != passes.index(password):
            print("wrong credentials.")
            time.sleep(3)
            c()
            return (False)
        else:
            return (True,username_bytes.decode('utf-8'))
def boot():
    #integrity checher
    #login
    #os version check