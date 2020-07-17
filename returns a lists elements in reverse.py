#Name: Mahsa Qadimzadeh Alamdar
#UCID: 30057724
#This function returns a lists elements in reverse

#def reverse_list(mylist):
   # mylist = []
   # mylist.reverse()
    #return (mylist)



def main():
    mylist = []
    ele=(input("eneter an element(blank line to quit):"))

    while ele!="":
        mylist.append(ele)
        ele=(input("eneter an element(blank line to quit):"))

    if ele == "":
        mylist.reverse()
        for ele in mylist:
            print (ele)

  
if __name__== "__main__":
  main()


