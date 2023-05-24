# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:27:45 2022

@author: Bajpapa
"""

# HOTEL MANAGEMENT SYSTEM PROJECT
import random
import datetime
import pyodbc
from sys import exit
# Global Variables
custid = []
custname = []
custphoneno = []
checkin = []
checkout = []
address = []
room = []
price = []
rc = []
ph = []
roomno = []
day = []
conn = pyodbc.connect('Driver={SQL Server};'
'Server=dca-db-240;'
'Database=HMS;'
'Trusted_Connection=yes;')
i = 0
# Menu List
def Menu():
#Menu List
   print("\t\t\t\t\t\t WELCOME TO HOTEL TAJ\n")
   print("\t\t\t 1 Book Room\n")
   print("\t\t\t 2 Room Service(Menu Card)\n")
   print("\t\t\t 3 Payment\n")
   print("\t\t\t 4 Record\n")
   print("\t\t\t 0 Exit\n")
choice=int(input("Enter your choice from above : ->"))
if choice == 1:
   print(" ")
Booking()
elif choice == 2:
   print(" ")
Restaurant()
elif choice == 3:
   print(" ")
Payment()
elif choice == 4:
   print(" ")
Record()
else:
   print("Exited")
exit()
# Room Booking Function
def Booking():
#Declated global variable
global i
custname=[]
custphoneno=[]
address=[]
room=[]
price=[]
print(" BOOK ROOMS ")
print(" ")
i=0
while 1:
   n = str(input("Enter your Name:"))
   p1 = str(input("Enter your Phone No.:"))
   a = str(input("Enter your Address:"))
# check if Name,Phone or Address is empty
if n=="" and p1=="" and a=="" :
   print("\tName, Phone no. & Address cannot be empty..!!")
elif (p1.isnumeric())== False:
   print(" \t Enter valid Phone no.")
elif len(p1) > 10 or len(p1) < 10:
   print(" \t Enter valid 10 digit Phone no.")
else:
   custname.append(n)
   address.append(a)
break
#Enter the check in date in the format
isValid = True
while 1:
   cii=str(input("Enter Check-In Date(DD/MM/YYYY): "))
   checkin.append(cii)
   cii=cii.split('/')
   ci=cii
   ci[0]=int(ci[0])
   ci[1]=int(ci[1])
   ci[2]=int(ci[2])
   isValid = date(ci)
if isValid == True:
break
while 1:
   coo=str(input("Enter Check-OutDate(DD/MM/YYYY): "))
   checkout.append(coo)
   coo=coo.split('/')
   co=coo
   co[0]=int(co[0])
   co[1]=int(co[1])
   co[2]=int(co[2])
   isValid = date(co)
if isValid == True:
break
d1=datetime.datetime(ci[2],ci[1],ci[0])
d2=datetime.datetime(co[2],co[1],co[0])
x = datetime.datetime.now().strftime('%Y-%m-%d')
if d1.strftime('%Y-%m-%d') < x:
   isValid = False
   print("\n\tErr..!!\n\tCheckOut date must be grater than or fall after Check-In\n")
else:
pass
# checks if check-out date falls after check-in date
if co[1]<ci[1] and co[2]<ci[2]:
   isValid = False
   print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
   isValid = False
   print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
else:
pass
if isValid == False:
   n=int(input("0-BACK\n ->"))
if n == 0:
   Menu()
else:
   print("Exited")
exit()
d=(d2-d1).days
#print(d)
day.append(d)
print("----VIEW ROOM TYPE----")
print(" 1. Standard Non-AC ")
print("---------------------------------------------------------------")
print("Room amenities include: 1 Double Bed, Television,")
print("Closet, Balcony and an attached washroom with hot/cold
water.\n")
print(" 2. Standard AC ")
print("---------------------------------------------------------------")
print("Room amenities include: 1 Double Bed, Television,")
print("Closet, Balcony and an attached washroom with hot/cold
water + Window/Split AC.\n")
print(" 3. 3-Bed Non-AC ")
print("---------------------------------------------------------------")
print("Room amenities include: 1 Double Bed + 1 Single Bed,
Television,")
print("Closet, Balcony with an Accent table with 2 Chair and an")
print("attached washroom with hot/cold water.\n")
print(" 4. 3-Bed AC ")
print("---------------------------------------------------------------")
print("Room amenities include: 1 Double Bed + 1 Single Bed,
Television,")
print("Closet, Balcony with an Accent table with 2 Chair and an")
print("attached washroom with hot/cold water + Window/Split
AC.\n\n")
print("PRESS 0 FOR ROOM PRICES")
choice=int(input("Enter your choice for Room type : ->"))
# if-conditions to display alloted room type and it's price
if choice == 0:
   print(" 1. Standard Non-AC - Rs. 3500")
   print(" 2. Standard AC - Rs. 4000")
   print(" 3. 3-Bed Non-AC - Rs. 4500")
   print(" 4. 3-Bed AC - Rs. 5000")
choice=int(input("->"))
if choice == 1:
room.append('Standard Non-AC')
print("Room Type- Standard Non-AC")
price.append(3500)
print("Price- 3500")
elif choice == 2:
room.append('Standard AC')
print("Room Type- Standard AC")
price.append(4000)
print("Price- 4000")
elif choice == 3:
room.append('3-Bed Non-AC')
print("Room Type- 3-Bed Non-AC")
price.append(4500)
print("Price- 4500")
elif choice == 4:
room.append('3-Bed AC')
print("Room Type- 3-Bed AC")
price.append(5000)
print("Price- 5000")
else:
print("Wrong choice..!!")
# randomly generating room no. and customer id for customer
# random number from 200 to 150 for Room no's
rn = random.randrange(50)+200
# random number from 100 to 50 for Customer Id
cid = random.randrange(50)+100
# checks if alloted room no. & customer id already not alloted
while rn in roomno or cid in custid:
rn = random.randrange(60) + 200
cid = random.randrange(60) + 100
rc.append(0)
ph.append(0)
if p1 not in custphoneno:
custphoneno.append(p1)
elif p1 in custphoneno:
for n in range(0,i):
if p1==custphoneno[n]:
if ph[n] ==1:
custphoneno.append(p1)
print(custphoneno + "else if ustphoneno")
elif p1 in custphoneno:
for n in range(0,i):
if p1==custphoneno[n]:
if ph[n]==0:
print("\tPhone no. already exists and payment yet not
done..!!")
custname.pop(i)
address.pop(i)
custphoneno.pop(i)
checkin.pop(i)
checkout.pop(i)
Booking()
print()
print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
print("Room No. - ",rn)
print("Customer Id - ",cid)
print("Custphoneno - ",custphoneno[i])
print("Address - ",address[i])
cd1=d1.strftime('%Y-%m-%d')
print("Checkin - ",cd1)
cd2=d2.strftime('%Y-%m-%d')
print("Checkout - ",cd2)
print("Room - ",room[i])
print("Price - ",price[i])
print("No.ofdays - ",d)
Totalamount=(int(price[i])*d)
roomno.append(rn)
custid.append(cid)
cursor = conn.cursor()
cursor.execute('INSERT INTO
CustomerInfo(CustomerID,CustomerName,PhoneNo,Address,Chec
kinDate,CheckoutDate,RoomType,Price,NoofDays,TotalAmount,Cre
atedDate)
VALUES(?,?,?,?,?,?,?,?,?,?,?)',(cid,custname[i],custphoneno[i],addr
ess[i],d1,d2,room[i],price[i],d,Totalamount,x))
conn.commit()
i=i+1
n=int(input("0-Back\n ->"))
if n==0:
Menu()
else:
print("Exit")
exit()
#Date Validation function
def date(c):
isvalidcheckindate = True
if(c[1]==1 or c[1]==3 or c[1]==5 or c[1]==7 or c[1]==8 or c[1]==10
or c[1]==12):
max1=31
elif(c[1]==4 or c[1]==6 or c[1]==9 or c[1]==11):
max1=30
elif(c[2]%4==0 and c[2]%100!=0 or c[2]%400==0):
max1=29
else:
max1=28
if(c[1]<1 or c[1]>12):
print("Invalid date\n")
isvalidcheckindate = False
elif(c[0]<1 or c[0]>max1):
print("Invalid date\n")
isvalidcheckindate = False
return isvalidcheckindate
# RESTAURANT FUNCTION
def Restaurant():
phno=int(input("Customer Id : "))
menu = []
custid = []
global i
cursor = conn.cursor()
data=cursor.execute('SELECT CustomerID,NoofDays,Price
FROM CustomerInfo WHERE CustomerID=?', (phno)).fetchone()
conn.commit()
if data:
custid=data
price=data[2]
noofdays=data[1]
f=0
r=0
i=1
for n in range(0, i):
#if custid[n]==phno and ph[n]==0:
if not data:
print("Invalid Customer Id")
elif phno==custid[n]: #and ph[n]==0:
f=1
print("---------------------------------------------------------")
print(" Hotel TAJ")
print("---------------------------------------------------------")
print(" Menu Card")
print("---------------------------------------------------------")
print("\n BEVARAGES ")
print("---------------------------------")
print(" 1 Regular Tea............. 20.00 ")
print(" 2 Masala Tea.............. 25.00")
print(" 3 Coffee.................. 25.00 ")
print(" 4 Cold Drink.............. 25.00 ")
print(" 5 Bread Butter............ 30.00 ")
print(" 6 Bread Jam............... 30.00")
print(" 7 Veg. Sandwich........... 50.00 ")
print(" 8 Veg. Toast Sandwich..... 50.00 ")
print(" 9 Cheese Toast Sandwich... 70.00")
print(" 10 Grilled Sandwich........70.00")
print(" SOUPS ")
print("----------------------------------")
print(" 11 Tomato Soup............ 110.00")
print(" 12 Hot & Sour............. 110.00")
print(" 13 Veg. Munchow........... 110.00")
print(" MAIN COURSE ")
print("----------------------------------")
print(" 14 Kadai Paneer........... 120.00")
print(" 15 Palak Paneer........... 120.00")
print(" 16 Chilli Paneer.......... 140.00")
print(" 17 Matar Mushroom......... 140.00")
print(" 18 Mix Veg................ 140.00")
print(" 19 Malai Kofta............ 140.00")
print(" 20 Aloo Matar............. 140.00")
print("Press 0 -to end ")
choice=1
while(choice != 0):
choice=int(input(" -> "))
#if-elif-conditions to assign item prices listed in menu
card
if choice==1 :
menu.append("Regular Tea............. 20.00")
rs=20
r=r+rs
elif choice==2 :
menu.append("Masala Tea.............. 25.00")
rs=25
r=r+rs
elif choice==3 :
menu.append("Coffee.................. 25.00")
rs=25
r=r+rs
elif choice==4 :
menu.append("Cold Drink.................. 25.00")
rs=25
r=r+rs
elif choice==5:
menu.append("Bread Butter.................. 30.00")
rs=30
r=r+rs
elif choice==6:
menu.append("Bread Jam.................. 30.00")
rs=30
r=r+rs
elif choice==7 :
menu.append("Veg. Sandwich.................. 50.00")
rs=50
r=r+rs
elif choice==8 :
menu.append("Veg. Toast Sandwich..................
50.00")
rs=50
rs=70
r=r+rs
elif choice==10 :
menu.append("Grilled Sandwich.................. 70.00")
rs=70
r=r+rs
elif choice==11 :
menu.append("Tomato Soup............ 110.00")
rs=110
r=r+rs
elif choice==12 :
menu.append("Hot & Sour............. 110.00")
rs=110
r=r+rs
elif choice==13 :
menu.append("Veg. Munchow........... 110.00")
rs=110
r=r+rs
elif choice==14 :
menu.append("Kadai Paneer........... 120.00")
rs=120
r=r+rs
elif choice==15 :
menu.append("Palak Paneer........... 120.00")
rs=120
r=r+rs
elif choice==16:
menu.append("Chilli Paneer.......... 140.00")
rs=140
r=r+rs
elif choice==17:
menu.append("Matar Mushroom......... 140.00")
rs=140
r=r+rs
elif choice==18:
menu.append("Mix Veg................ 140.00")
rs=140
r=r+rs
elif choice==19:
menu.append("Malai Kofta............ 140.00")
rs=140
r=r+rs
elif choice==20:
menu.append("Aloo Matar............. 140.00")
rs=140
r=r+rs
elif choice==0:
pass
else:
print("Wrong Choice..!!")
print("You have ordered:")
print("\n".join(menu))
print("Total Bill: ",r)
Totalamount=(int(price)*int(noofdays))+int(r)
cursor = conn.cursor()
cursor.execute('UPDATE CustomerInfo SET
RestaurentCharges=?, TotalAmount=? WHERE CustomerID =
?',r,Totalamount,custid[n])
conn.commit()
else:
pass
n=int(input("0-BACK\n ->"))
if n==0:
Menu()
else:
exit()
# PAYMENT FUNCTION
def Payment():
phno=str(input("Enter Phone Number: "))
custphoneno= []
global i
cursor = conn.cursor()
data=cursor.execute('SELECT * FROM CustomerInfo WHERE
PhoneNo=?', (phno)).fetchall()
conn.commit()
#conn.close()
if data:
cphone=str(data[0][2])
noofdays=data[0][8]
price=data[0][7]
if data[0][9] != None:
restcost=data[0][9]
else:
restcost="0"
customername=data[0][1]
custphoneno.append(cphone)
custaddress=data[0][3]
custcheckindate=data[0][4]
cd1=custcheckindate.strftime('%Y-%m-%d')
custcheckoutdate=data[0][5]
cd2=custcheckoutdate.strftime('%Y-%m-%d')
custroomtype=data[0][6]
else:
print("no data")
i=1
f=0
for n in range(0,i):
if data and phno==custphoneno[n]:
#checks if payment is not already done
#if ph[n] == 0:
f=1
print(" Payment")
print(" -------------------------------")
print(" MODE OF PAYMENT")
print("1- Credit/Debit Card")
print("2- Paytm/PhonePe")
print("3- Using UPI")
print("4 - Cash")
x=int(input(" -> "))
print("\n No days: " + str(noofdays))
print("\n Room Price: "+ str(price))
print("\n Restaurent Charges: "+ str(restcost))
print("\n Total Amount:
",(int(price)*int(noofdays))+int(restcost))
print("\n Pay For TAJ")
print("(y/n)")
choice=str(input("->"))
if choice == 'y' or choice =='Y':
print("\n\n --------------------------------")
print(" Hotel TAJ")
print("--------------------------------")
print(" Bill")
print("--------------------------------")
print(" Name: ",customername,"\t\n Phone No.:
",cphone,"\t\n Address: ",custaddress,"\t")
print("\n Check-In: ",cd1,"\t\n Check-Out: ",cd2,"\t")
print("\n Room Type: ",custroomtype,"\t\n Room Charges:
",price*noofdays,"\t\n Restaurant Charges: " ,restcost ,"\t")
print("--------------------------------")
print("\n Total Amount:
",(int(price)*int(noofdays))+int(restcost),"\t")
print("--------------------------------")
print(" Thank You")
print(" Visit Again :)")
print("--------------------------------")
else:
for j in range(n+1 , i):
if ph==custphoneno[j]:
if ph[j]==0:
pass
else:
f=1
print("\n\tPayment has been Made :)\n\n")
if f==0:
print("Invalid Phone Number")
n=int(input("0-BACK\n ->"))
if n==0:
Menu()
else:
exit()
# RECORD FUNCTION
def Record():
cursor=conn.cursor()
data=cursor.execute('SELECT * FROM CustomerInfo').fetchall()
cursor.commit()
if data:
print(" *** HOTEL RECORD ***\n")
print("| CustomerID | Name | Phone No.| Address | Check-In |
Check-Out | Room Type | Price | NoofDays | RC | TotalAmount |")
print("----------------------------------------------------------------------------------
--------------------------------")
for n in range(0,len(data)):
CustomerID=data[n][0]
CustomerName=data[n][1]
PhoneNo=data[n][2]
Address=data[n][3]
CheckinDate=data[n][4].strftime('%Y-%m-%d')
CheckoutDate=data[n][5].strftime('%Y-%m-%d')
RoomType=data[n][6]
Price=data[n][7]
NoofDays=data[n][8]
RestaurentCharges=data[n][9]
TotalAmount=data[n][10]
print("|",CustomerID,"\t |",CustomerName,"\t
|",PhoneNo,"\t|",Address,"\t|",CheckinDate,"\t|",CheckoutDate,"\t|",R
oomType,"\t|",Price,"\t|",NoofDays,"\t|",RestaurentCharges,"\t|",Total
Amount)
print("----------------------------------------------------------------------------------
--------------------------------------------------------------------------------------")
else:
print("No Records Found")
n=int(input("0->BACK\n ->"))
if n ==0 :
Menu()
else:
exit()
#Main Mehtod
Menu()
