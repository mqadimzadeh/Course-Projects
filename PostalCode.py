
#Name:Mahsa Qadimzadeh Alamdari
#UCID:30057724

#This program takes the postal code as input and returns the corresponding province

#pcp:Postal Code of Provinces
pcp={"T":"Alberta", "V":"BritishClombia", "R":"Manitoba", "E":"New Brunswick", "A":"Newfoundland", "B":"Nova Scotia", "X":"North West Theritories or Nunavut", "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario", "C":"Prince Edward island", "G":"Quebec", "H":"Quebec", "J":"Quebec", "S":"Saskatchewan", "Y":"Yukon"}

#get the postalcode from the user
name=input("enter a 6 character postal code") 

#converts all teh letters to uppercase and stores in a list
name=name.upper() 
name = list(name)
 

#Check which prvince the postalcode belongs to
print("That postal code resides in", pcp.get(name[0]))
