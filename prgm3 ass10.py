3#read the contents in a file using with statements
L=["This is london \n","This is paris \n","This is delhi \n"]
with open("myfile.txt","w") as file1:
	file1.write("Hello \n")
	file1.writelines(L)
	file1.close()
with open("myfile.txt","r+") as file1:
    print(file1.read())