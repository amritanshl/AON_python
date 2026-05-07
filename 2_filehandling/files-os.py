import os
old_name = "D:\\Microsoft\\Microsoft\\PYTHON\\5MayPython\\2_filehandling\\data\\sample.txt"
new_name ="D:\\Microsoft\\Microsoft\\PYTHON\\5MayPython\\2_filehandling\\data\\amrit.txt"
# try:
#     #os.rename(old_name,new_name)
#     #os.remove(old_name)
# except FileNotFoundError:
#     print(f"file not found in the directory {old_name}")
# except FileExistsError:
#     print(f"file already exists at given location {old_name}")
# except Exception as e:
#     print(f"Exception occurred as e")
# 



# Technical Step: Identify where your script is "standing" right now
# current_location = os.getcwd()+r"\data"
# print(f"Current Working Directory: {current_location}")
# new_dir = "backups"

# try:
#     if not os.path.exists(new_dir):
#         os.mkdir(new_dir)
#         print(f"Directory '{new_dir}' created successfully.")
# except PermissionError:
#     print("Technical Error: You do not have 'Write' permissions for this location.")
# old_name = "backups"
# new_name = "archive_2026"

# if os.path.exists(old_name):
#     os.rename(old_name, new_name)
#     print("Directory metadata updated (Renamed).")


import os

path = os.getcwd()
path.join(r"data")# The dot represents the 'Current Working Directory'

# Fetching the list of items
items = os.listdir(path) 

print(f"Total items found: {len(items)}")
for item in items:
    # Technical check: Is this item a file or a folder?
    if os.path.isdir(item):
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")
# #2016/09/05/14/00/00/hdfc_20160905140000.csv
# #2016/09/05/14/00/10/hdfc_20160905140010.csv
# #2016/09/05/14/00/20/hdfc_20160905140020.csv
# .
# .
# #2016/09/05/15/00/10/hdfc_20160905150010.csv


