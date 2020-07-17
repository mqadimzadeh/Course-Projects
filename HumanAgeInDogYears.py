#Computing human age in dog years
#Name:Mahsa Qadimzadeh Alamdari
#UCID: 30057724

human_age=float(input("Enter your age in yeras:"))

while human_age>2:
    human_age2=(human_age) - 2  
    human_age3=human_age2 * 4
    dog_years= (2*10.5) + human_age3
    print("your age in dog years is:", dog_years)
    human_age=float(input("Enter the next human age you want to calculate in dog years:"))
while 0<=human_age<=2:     
    dog_age=human_age * 10.5
    print("Your age in dog years is:", dog_age)
    human_age=float(input("enter the next human age:"))
else:
    print("You need to enter a positive number for age!3")
    
