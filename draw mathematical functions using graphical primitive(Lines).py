#This peogram is to draw mathematical functions using graphical primitive(Lines)
#Name: Mahsa Qadimzadeh Alamdari
#UCID: 30057724

from SimpleGraphics import *   
from math import *

# Defining variables in terms of axes length and unit length
unit=30                  # Each crtisian unit is devided to 30 pixels
full_x=800               # Screen's Length (in pxels)
full_y=600               # Screen's width  (in pixels)
half_x=400               # X position of Cartisian coordinate center (in pixels)
half_y=300               # Y position of Cartisian coordinate center (in pixels)
x_start = -13            # Start point of the cartisina x axes
x_stop = 14              # End point of the cartisina x axes
y_start = -10            # Start point of the cartisina y axes
y_stop = 11              # End point of the cartisina y axes
step = 0.1               # Increment for marching through x axes
unit_line=5              #The length of each segment used for indicating units on each axes
yaxes_distance=20        #Distance of unit numbers from y axes (in pixels)
xaxes_distance=15        #Distance of unit numbers from x axes (in pixels)

#Creating the main axis of x and y
line(0, half_y, full_x, half_y)
line(half_x, 0, half_x, full_y)
line(half_x+unit, half_y, half_x+unit, half_y+unit_line)

#Creating the small units on x axes
for x in range (half_x,full_x, unit): 
    line(x , half_y, x, half_y+unit_line)
for x in range (half_x,0, -unit): 
    line(x , half_y, x, half_y+unit_line)

#Creating the small units on Y axes
for y in range (0,half_y, unit): 
    line(half_x, y,half_x+unit_line, y)
for y in range (half_y,full_y, unit): 
    line(half_x, y,half_x+unit_line, y)

#Labeling the units on X axis
    z=-(x_stop) 
    for i in range (10, full_x, unit): 
     z=z+1
     text(i, half_y-10, z)

#Labeling the units on Y axis
    z= y_stop
    for j in range (0, full_y+yaxes_distance , unit):  
      z=z-1
      text(half_x+xaxes_distance, j, z)

#Asking for mathematical expression and drawing the curve with ellipses in three different colors by sequence

count=0            #Counter for the color sequence

while True:

  expression = input("Enter an arithmetic expression (blank line to quit):")
  
  if expression == "":
    close()
  else:
    x = x_start
    while x <= x_stop:
      
        if count % 3 ==0:
            pen_color = "red"
        elif count % 3 == 1:
            pen_color = "green"
        elif count % 3 ==2:
            pen_color = "blue"
            
       # Evaluating the mathematical expression using the method below     
        print(y)
        y=eval(expression)
        x_pos1=(half_x)+(x*unit)
        y_pos1=(half_y)-(y*unit)

        x= x + step

        y=eval(expression)
        x_pos2=(half_x)+(x*unit)
        y_pos2=(half_y)-(y*unit)

        setColor(pen_color)
        setFill(pen_color)
        line(x_pos1, y_pos1, x_pos2, y_pos2)
      

    count=count+1

# The body of Main program is 90 lines!

# This part is for the bonus part!
