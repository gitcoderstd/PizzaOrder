print ("Welcome to the pizza ordering system")
#TO PRINT MENU 
print (" Base Prcie as per size:")
print("\n Small :150/- \n Medium: 250/- \n Large :350/-")
print ("\n\nFor add-ons :")
print ("\n FOR EXTRA PANEER :50/- \n FOR EXTRA CHEESE :30/-")

#INPUT
size=input("what size do you want?S/M/L: ")
add_paneer=input("do you want to add paneer to it ?Y/N: ")
add_cheese=input("do you want to add extra cheese to it ?Y/N: ")

bill=0
#CALCULATE TOTAL BILL'
#size 
if size=='S':
    bill+=150
elif size=='M':
    bill+=250
else:
    bill+=350 
 
 #paneer
if add_paneer=='Y':
    if size=='S':
      bill+=50
    else:
        bill+=60
       

#add cheese
if add_cheese=='Y':
    bill+=30
else:
    bill+=0 

gst=round(0.18*bill)

#to add and display total bill
print(f"THE TOTAL AMOUNT FOR YOUR PIZZA ORDER +GST : Rs.{bill} + gst amt Rs.{gst}")
bill=bill+gst
print("So the net total for your order is: ",bill)

