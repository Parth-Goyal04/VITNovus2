import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Tae&kookie1997',database='foodelivery')
if mydb.is_connected()== False:
    print('Error')
mycursor = mydb.cursor()
print("\n                       **WELCOME**")

list_menu=[]
list_q=[]
list_price=[]
overall_sale=0.0

def arasanf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from arasan;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from arasan where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def foodcourtf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from foodcourt;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from foodcourt where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def hcf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from hangyandswig;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from hangyandswig where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def bbf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from buddysbites;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from buddysbites where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def dccf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from dccafe;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from dccafe where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def enzof():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from enzo;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from enzo where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def ofwf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from onefoodworld;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from onefoodworld where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def dcf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from dccanteen;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from dccanteen where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost
def qbf():
    n=0
    i=0
    total_cost=0.0
    while(n!=1):
        mycursor.execute("select * from quickbites;")
        for x in mycursor:
            print(x)
        foodItem=input("\nEnter the food item :")
        query1="select * from quickbites where itemname = %s"
        mycursor.execute(query1,(foodItem,))
        d=int(input("Enter quantity of the item you want : "))
        data=mycursor.fetchall()
        list_menu.append(data[0][i])
        costp=0
        costp=data[0][2]*d
        list_price.append(costp)
        total_cost=total_cost+costp
        list_q.append(d)
        
        z=int(input("to order further type any other digit and if you want to end ordering type 0 "))
        i+=1
        if (z==0):
            n=1
    return total_cost





entry=input("Enter restraunts name")
if entry =='arasan':
    c=arasanf()
    print(c)
elif entry== 'food court':
    c=foodcourtf()
    print(c)
elif entry== 'hangy & swigy':
    c=hcf()
    print(c)
elif entry== "buddy's bites" :
    c=bbf()
    print(c)
elif entry== "dc cafe" :
    c=dccf()
    print(c)
elif entry== "enzo" :
    c=enzof()
    print(c)
elif entry== "one food world" :
    c=ofwf()
    print(c)
elif entry== "DC canteen" :
    c=dcf()
    print(c)
elif entry== "quick bites" :
    c=qbf()
    print(c)


mydb.commit()



    
    
    
