#Name;Mahsa Qadimzadeh
#UCID:30057724
#To calculate the number of comma seperated values

#to get file name from user and use it to open the file
import sys
print(sys.argv, len(sys.argv))

#Creating teh path of the file
path = sys.argv[1]


#opening and reading the file
f = open(path,'r')
#f=open('/Users/mahsa/Documents/CPSC/ASSIGNMENT4/test1.txt','r')
x = f.read()

l = x.split("\n")

#calculate the total number of comma seperated values in each element of teh list
total=0
for i in l:
    s = i.split(",")
    ss=len(s)
    total=total+ss

print(total)