import os.path
from company import Company
from project import Project

if not os.path.isfile("user.txt"):
    print("Creating user.txt...")
    with open("user.txt", "w") as f:
        f.write(input("dbname="))
        f.write("\n" + input("user="))
        f.write("\n" + input("password="))
    print("user.txt created successfully")

tag_cloud_1 = """(1) Generates tag cloud that shows the company names:
- font size based on number of projects (the more, the bigger)
- font color are a mixture of their project colors"""
tag_cloud_2 = """(2) Generates tag cloud that shows the project names:
- font size based on the budget of the project (the more, the bigger)
- font color based on the project colors"""
tag_cloud_3 = """(3) Generates tag cloud that shows the project names:
- font size based on the due date of the project (the older, the smaller)
- font color based on whether the project requires maintenance or not"""
tag_cloud_3 = """(3) Generates tag cloud that shows the names of the manager:
- font size based on the budget of the project (the older, the smaller)
- font color is based on the company they work for"""
for i in range(1, 3):
    print("(%d) Generate tag cloud. Type 'info %d' for more information." % (i, i))
user_input = input("").lower()
while True:
    if user_input == "info 1":
        print(tag_cloud_1)
        user_input = input("").lower()
    if user_input == "info 2":
        print(tag_cloud_2)
        user_input = input("").lower()
    if user_input == "info 3":
        print(tag_cloud_3)
        user_input = input("").lower()
    if user_input == "info 4":
        print(tag_cloud_3)
        user_input = input("").lower()
    if user_input == "1":
        break
    if user_input == "2":
        break
    if user_input == "3":
        break
    if user_input == "4":
        break
    else:
        print("Unavailable, please try again.")
        user_input = input("").lower()
