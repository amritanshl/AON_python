path = "D:\\Microsoft\\Microsoft\\PYTHON\\5MayPython\\2_filehandling\\data\\test.txt"
path2 = "D:\\Microsoft\\Microsoft\\PYTHON\\5MayPython\\2_filehandling\\data\\HDFS_Hive_Infra.png"

# with open(path, "r") as f:
#     content = f.read()
# print(content)

# with open(path2, "rb") as f:
#     content = f.read()
# #print(content)

# with open(path, "r+", encoding="utf-8") as f:
#     content = f.read()
#     f.seek(0)
#     f.write("Amrit data for testing")
#ASCII, UTF-8, CP1252, Unicode


# with open("C:\\Users\\alal0\\Downloads\\color.png", "rb") as f:
#     image_content= f.read()
#     print(image_content)


# with open(path2, "wb") as f:
#     #content = f.read()
    
#     f.write(img_cont)

# with open(path, "w+") as f:
#     f.write("Hello World")
#     f.seek(0)
#     print(f.read())

# with open(path, "a") as f:
#     f.write("\nNew log entry.")


path = r"D:\Microsoft\Microsoft\PYTHON\5MayPython\2_filehandling\data\sample.txt"

# # Reading efficiently using a context manager
# with open(path, "r") as f:
#     f_line = f.readline()
#     s_line = f.readline()
#     t_line = f.readline()
#     ff_line = f.readline()
#     fi_line = f.readline()
#     si_line = f.readline()
#     se_line = f.readline()
#     print(f_line)
#     print(s_line)
#     print(t_line)
#     print(ff_line)
#     print(fi_line)
#     print(si_line)
#     print(se_line)

#     all_lines = f.readlines()
#     print(all_lines)

with open(path, "r+", encoding="utf-8") as f:
    line = f.readlines()
   # print(line)
line[7] = "Pulkit Kamboj,pulkit_updated,999\n"

with open(path, "w", encoding="utf-8") as amrit:
    amrit.writelines(line)