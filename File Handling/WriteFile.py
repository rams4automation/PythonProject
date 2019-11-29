
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content


fs = open("C://Users//Ramesh//Desktop//Python//demofile3.txt", "w")
fs.write("Welcome to Python")
fs.close()

fs=open("C://Users//Ramesh//Desktop//Python//demofile3.txt", "a")
fs.write("I am Appending the content")
fs.close()

fs=open("C://Users//Ramesh//Desktop//Python//demofile1.txt", "x")

