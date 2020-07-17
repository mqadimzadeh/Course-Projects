#Name: Mahsa Qadimzadeh Alamdari
#UCID No.:30057724
#This program creates a smily centered to the point defined by the user


#Importing SimpleGraphics and sets the background color
from SimpleGraphics import *
background("black")   #Sets the background color


#Ctreating the outline of face with the given center point 
xc=int(input("enter the x position for the center point of smiley position:"))
yc=int(input("enter the y position for the center point of smiley position:"))
r=350
setColor("Gold")
ellipse(xc-(r/2), yc-(r/2), r, r)



#Creating the left eye in green color
r_left=0.3*r
r_left=0.3*r
x_left=(xc-(r/4))-(r_left/2)
y_left=(yc-(r/2))+(r/4)
setColor("green")
ellipse(x_left, y_left, r_left, r_left)



#Creating the right eye in green color
r_right=0.3*r
r_right=0.3*r
x_right=(xc+(r/4))-(r_right/2)
y_right=(yc-(r/2))+(r/4)
setColor("green")
ellipse(x_right, y_right, r_right, r_right)



#Creates the mouth in red
setColor("red")
pieSlice(x_left+(r_left/2), (y_left)+(r_left)+20, 0.5*r, 0.3*r, 180, 180)



#Creates the hat in blue
setColor("blue")
polygon(xc-(r/2), yc-(r/2), (xc-(r/2))+350, yc-(r/2), xc, yc-250)
line(xc-(r/2), yc-(r/2), xc-(r/2), yc-(r/2)+50)
ellipse(xc-(r/2)-10, yc-(r/2)+50, 30, 30)


setOutline("gold") 
setFill("gold")
setFont("Times", "14", "italic")
text(xc, yc+200, "SMILE!")











