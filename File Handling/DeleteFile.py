import os

if os.path.exists("C://Users//Ramesh//Desktop//Python//demofile1.txt"):
    os.remove("C://Users//Ramesh//Desktop//Python//demofile1.txt")
    print("The file deleted successfully")
else:
    print("The file does not exist")


# Delete Folder

os.rmdir("C://Users//Ramesh//Desktop//Python1")