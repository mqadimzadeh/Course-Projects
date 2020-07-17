#Name:Mahsa Qadimzadeh Alamdari
#UCID:30057724

#This programs extracts data from a text file and draws the related sankey diagram using simplegraphics

from SimpleGraphics import *

import sys

#setAutoUpdate(False)

##################################################################################################################################
#Function No.0: This function gets the file name from user and shows proper massages according to what is entered
#also checks if the file exists/entered by correct name or not and showes the proper massage
##################################################################################################################################
def openfile (argv):
    if len(argv)==1:      #if no file name is provided
        filename=input("Enter the name of the file")
        error=True
        while error:
            #filename=input("Please Provide a valid file name")
            try:
                file_open=open(filename,'r')
                file_data=file_open.read()
                error=False
                file_open.close()

            except FileNotFoundError:
                error=True
                filename=input("No file Exists!Eneter a correct File name:")

            except IndexError:
                error=True
                print(input("The file does not exist"))
                #while len(argv)==1:
            
   

    elif len (argv)==2:     #if one file name is provided
        filename = sys.argv[1]

    elif len(argv) > 2:     #if more than ine file name is provided
        print("please provide one file name only")
        close()
        exit()
   
    return(file_data)
##################################################################################################################################
#Function No.1: This is the main function which takes the file name from user, reads the data from that file and converst 
# the data to a dictioanary and uses command line arguments and sankey function
##################################################################################################################################
def main():
    file1 = openfile(sys.argv)
    file2= filedatalist(file1)
    file3=convert_dict(file2)
    sankey(file3)
    #print (file3)
#print(file)


##################################################################################################################################
#Function No.2:This function splits the lines in the file and creates the label for source and prints the title of the chart
#it returns the fiel data (each line seperated) as a list 
##################################################################################################################################

def filedatalist (file_data):
    w=getWidth()   #Height of screen
    h=getHeight() #Width of screen

    #defining magic numbers and splitting the file's data by line
    upperlimit=50       #distance of text from the border of the graphical  window
    file_data_list = file_data.split('\n')

    #pop function is to remove the last index of the list (empty index)
    file_data_list.pop()

    #Creating diagram's title and the label for source bar
    setFont("Times", "12", "regular")
    text(3*upperlimit/2,h/2, file_data_list[1])   #creates the source label  

    setFont("Times", "24", "bold")
    text(w/2,upperlimit,file_data_list[0])    #creates the title 
    return(file_data_list)


#print(file2)

##################################################################################################################################
#Function No.3: This function converts the data read from the file into keys and values in a dictionary and returns the 
#the catagories and associated values in a dictionary form(keys and values)///This dictionary will be used in sankey function
# to draw the diagram

##################################################################################################################################
def convert_dict(file_data_list):
    source_data={}
    for values in file_data_list[2:len(file_data_list)]:   #This "for" loop splits each data in the file seperated with comma
                                                           
        content_info=values.split(',')
        source_data[content_info[0]]=float(content_info[1]) #The values should be float numbers
        #print(content_info)
    return(source_data)


##################################################################################################################################
#Function No.4:This function is to draw the whole parts of sankey diagrams it takes s_v argument and draws the diagram
# with color gradients
# and source and destination bars+bars' labels. etc.
#does not return anything
##################################################################################################################################

def sankey(s_v):
    #Defining constants and magic numbers
    w=getWidth()   #Height of screen 
    h=getHeight() #Width of screen
    
    barwidth=20     #the width of source and destination bar
    xdistance=500    #This number indicates how wide the diagram is (in x axis directin)
    x_source=(w-xdistance)/2-(barwidth)
   
    flow_total=0
    ydistance=450    #This number indicates how high the diagram is (in y axis directin)
    gap=10           #Gap between destination bars

    margin2=1        #balck border margine for the destination bar side
    borderwidth=1    #blackborder width used to create the black border of the curves


    #Creating list for RGBs
    maroon=[128, 0, 0]
    brown=[170, 110, 40]
    olive=[128, 128, 0]
    teal=[0, 128, 128]
    yellow=[255, 225, 25]
    red=[230, 25, 75]
    cyan=[70, 240, 240]
    ####################################################################

    #This for loop calculastes the the total value of flows in a file
    for key in s_v.keys():
        flow_total= flow_total+s_v[key]
    #print(flow_total)  

    #####################################################################
    #Calculating variables needed to draw the source bars and defining colors in color palette 

    number_of_pixel=ydistance-(len(s_v)-1)*gap    
    number_of_pixel_per_unit=number_of_pixel/flow_total
    height_source=flow_total*number_of_pixel_per_unit    #calculating the height of the source bar using num of pixels/per unit pixels

    
    x_destination=x_source+barwidth+xdistance           #calculating the x-coordinate of the destination bar                                              
    y_destination=(h/2)-(ydistance/2)                   #calculating the x-coordinate of the destination bar
    y_source = (h/2)-(height_source/2)                  #Calculations for y coordinate of source bar to be centered in the screen
    
    
    #creating colorpalette list to use for gradient coloring parts
    colorPalette = [maroon, brown, olive, teal, yellow, red,cyan] 

    #####################################################################

    #this for loop goes through all the values of created dictionary to calculate the height of each destination bar using 
    # the values of created dictionary
    #This for loop creates the destination bars with sepearet colors defined in the colorpalette in gradient form
    #Creating bars and black borders 
    
    colorcount=0                   #this counter is defined to access the elemnts of color palette
    for key in s_v.keys():        
        height_key=s_v[key]* number_of_pixel_per_unit
       

        #Creating destination bars
        setColor(colorPalette[colorcount][0], colorPalette[colorcount][1], colorPalette[colorcount][2])
        rect(x_destination, y_destination,barwidth,height_key)


        #Creating the black borders around sourca and destination bars (right side and bottom part)
        setColor(0,0,0)
        rect(x_destination+barwidth, y_destination,borderwidth, height_key)
        #Creates the black border for upper border of  destination bar
        line(x_destination-margin2, y_destination,x_destination+barwidth, y_destination)

        #Creates the black border for upper border of  destination bar
        #line(x_destination-margin2, y_destination,x_destination+barwidth, y_destination)

        #creates the lower black border for destination bar
        line(x_destination-margin2, y_destination+height_key,x_destination+barwidth, y_destination+height_key)

        #Creating black borders for the right side of the destination bar
        #line(x_destination+40, y_destination,x_destination+40, y_destination+height_key)

       ####################################################################
       
       #This while loop creates the rectangles/lines(any of these two works/this code is set with rectangles) between the source and destination using linear interpolation method
        xt = 0.0           #initializing this variable to use the linear interpolation formula
        pi = 3.141592      #The famous "pi"!
        rect_step=2     #The increament for drawing the rectangles between source and destination
        interpolation_upperlimit=0.96
        interpolation_increment=0.001
        while xt < interpolation_upperlimit:
            import math

            #This part is to get a curved diagranm
            p = xt * pi - pi / 2
            p = (math.sin(p) + 1) / 2
            #print(p)
            
            #getting new coordinates for each point in the middle part of the diagram
            xnew=(x_source+barwidth)+(x_destination-x_source+barwidth)*xt
            ynew=y_source+(y_destination-y_source)*p

            #creating these lists to use for adding new colors from color palette for 
            # coloring the middle part of diagram in gradient form
            m1 = [60, 180, 75]       
            m2 = colorPalette[colorcount]

            #Creating a new list to put the gradient colors in it
            newcolor=[] 

            #Creating color gradient by appending RGB numbers to the list
            for color in range(0,len(m2)):
               rgb=m1[color]+(m2[color]-m1[color])*xt
               newcolor.append(rgb)

            #Drawing the middle part of diagram via drawing some rectangles(rectangles are faster)/lines and using color palette
            setColor(newcolor[0], newcolor[1], newcolor[2]) 

            rect(xnew, ynew, rect_step, height_key)  
            #line(xnew, ynew, xnew, ynew+height_key) 

            #drawing border lines in black for the middle part of the sankey diagram
            setColor(0,0,0)
            rect(xnew, ynew, margin2, margin2)
            rect(xnew, ynew+height_key, margin2, margin2)
           
            xt = xt + interpolation_increment
        
        y_source += height_key
        y_destination=y_destination+height_key+gap
        colorcount=colorcount+1


        #Here we create the source bars + indicating the text location for source bar +the black border 
        # for source bar

        setColor(60, 180, 75)       #setting the color of source bar in green
        rect(x_source,(h/2)-(height_source/2),barwidth,height_source)    #drawing the source bar
        
        #creates the black border for the left side of source bar 
        setColor(0,0,0)
        line(x_source-margin2,y_source,x_source-margin2,y_source-height_key ) 


    #This line creates two little black rectangles at the bottom and top of source bar
    setColor(0,0,0)
    rect(x_source, y_source, barwidth, margin2)    #for teh botoom part
    rect(x_source-margin2, y_source-height_source, barwidth, margin2)    #for the top part

    
    #Indicating text lables' location for destination bars
    text_location=((h/2)-(ydistance/2))

    #Creating labels for each destination bar
    for key in s_v.keys():
        tex_bar_gap=80        #The gap between label and destination bars
        height_key=s_v[key]* number_of_pixel_per_unit   #height of destination bar
        setColor(0,0,0)
        setFont("Times", "12", "regular")
        text(x_destination+tex_bar_gap,text_location+(height_key/2), key)  
        text_location=text_location+((height_key)/2)+gap        #Indicating the location of labels for each destination bar 
        text_location=text_location+(height_key/2)              #shifting the location of the next label for the nesxt destination bar 
    
    #update() 
    

  

main()                 #main call:drawing Sankey diagrams by reading the data from a txt file given by the user(using simplegraphics)

