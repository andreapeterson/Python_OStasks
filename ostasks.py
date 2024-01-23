#!/usr/bin/python3

import os

user = input("Type each user separated by a space: ")
user_list = user.split()

print("Adding users to system . . . ")


for user in user_list:
    if os.system(f"id {user}") == 256:
        print(f"Adding {user} now . . .")
        os.system(f"useradd {user}")
    else: 
        print(f"{user} already exists..")

print("##################################################")

group = input("What group do you want to create: ")

if os.system(f"grep {group} /etc/group") == 256:
    print(f"Creating {group} . . .")
    os.system(f"groupadd {group}")
    print(f"{group} created.")
else:
    print(f"{group} already exists.")

print("##################################################")

add = input("Do you want to add these users to a group? Type y or n: ")

if add == "y":
    user_group = input("Which group? Enter  with exact spelling: ")
    for user in user_list:
        os.system(f"usermod -G {user_group} {user}")

print("Done!")
