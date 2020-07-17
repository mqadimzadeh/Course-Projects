#Name: Mahsa Qadimzadeh
#UCID:30057724
#To draw a picture including a house & some other  natural features
from SimpleGraphics import *   

#to set the background color of the window
background("deep sky blue")  

#creates the green grass at the bottom of window
setOutline("cyan2") 
setFill("chartreuse4")
rect(0,400,800,200)

#creates the body of the house in brown color
setOutline("black") 
setFill("chocolate4")
rect(200,200,300,250)

#creates the outline of the window
setOutline("Black")
setFill("Gold")
rect(400, 220, 90, 90)

#creatyes the cross mark for window to make it complete!
line(445, 220, 445, 310)
line(400, 265, 490, 265)

#creating some cool wind pattern!
setOutline("floral white") 
setFill("floral white")
curve(500, 100, 510, 100, 520, 100, 540, 100, 550, 100, 560, 100, 600, 85, 555, 60, 535, 80, 549, 90, 555, 80)

#Creates the roof!
setOutline("black") 
setFill("brown2")
polygon(200, 200, 350, 100, 500, 200)

#Creates the door!
setOutline("black") 
setFill("dark blue")
rect(290, 300, 70, 150)

#Creates the Clouds in teh sky!
setOutline("floral white") 
setFill("floral white")
ellipse(20, 50, 80, 50)
ellipse(25, 70, 60, 60)
ellipse(50, 90, 60, 60)
ellipse(95, 70, 60, 60)
ellipse(125, 70, 60, 60)
ellipse(145, 70, 70, 55)
ellipse(125, 60, 90, 60)
ellipse(145, 98, 50, 50)
ellipse(20, 30, 40, 40)
ellipse(20, 30, 40, 40)

#Creates the sun!
setOutline("Gold") 
setFill("Gold")
pieSlice(630, -180, 350, 350, 180, 90)

#The artist's name!
setOutline("black") 
setFill("black")
setFont("Times", "14", "italic")
text(650, 580, "By The Great Artist: Mahsa Qadimzadeh :)")
