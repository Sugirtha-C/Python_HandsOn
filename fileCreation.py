
# open('filepath','access mode')

"""
modes:
w
a-append
t text
b binary
x xclusive creation
r read"""
import os
from datetime import datetime

fp=open("sample.txt",'w')
fp.write("first line \n")
fp.write("second line \n")
fp.write("third line \n")
fp.write("fourth line \n")
fp.close()

#list files from working directory
print(os.listdir())
#verify file exists
print(os.path.exists('sample.txt'))


with open(r'/home/zadmin/Documents/Python_Learnings/pythonLearnings/basics/sample.txt','w') as fp:
    fp.write('first line \n Second line \n Third line \n fourth line' )
    pass

filepath="/home/zadmin/Documents/Python_Learnings/pythonLearnings/basics/sample.txt"
if os.path.exists(filepath):
    print("exists")
else:
    print("file not found")

x=datetime.now()
filename=x.strftime("%Y%m%d-%H%M%S")
with open(filename,'w') as fp:
    fp.write("Hello")

#opening a file

try:
    fp=open(r'sample.txt','r')
    #print(fp.read()) #read entire file contents
    line=fp.readline() #reads first line
    while(line != ''):
        print(line, end='')
        line=fp.readline()
    #print(line)
    """for i in range(3):
        print(fp.readline().strip()) #strip: used to remove whitespaces and new lines
        """
    fp.close()

except IOError:
    print("File not found")

finally:
    print("Exiting")

with open(r'sample.txt','r') as fp:
    lines=fp.readlines()
    print(lines)

lines=["First line", "Second line" ,"third line"]
with open("listsamplefile.txt",'w') as fp:
    fp.writelines(lines)
    fp.close()

with open(r'listsamplefile.txt','r') as fp:
    fp.read()
    fp.close()
