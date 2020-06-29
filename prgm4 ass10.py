4#import file and directory
import os
file="file1.txt"
location="D:/projects/python assignment/shashank/"
path=os.path.join(location, dir)
os.remove(path)
print("%s has been removed successfully"%dir)