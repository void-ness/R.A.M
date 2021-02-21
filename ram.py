print("""          press 1 for menu
          press 2 for order
          press 3 to update menu
          press 0 to exit """)
print()


import mysql.connector as sql
import pandas as pd


q=sql.connect(host="localhost",\
              user="root", passwd="noob")
w=q.cursor()

w.execute("create database if not exists mainu")

q=sql.connect(host="localhost",\
              user="root", passwd="noob",database="mainu")

w=q.cursor()

w.execute("show tables")

w1=w.fetchall()

if ("menu",) and ("admin",) not in w1:
    
    w.execute("create table menu(s_no int primary key,\
                dish_name varchar(30),\
                type varchar(30),\
                price int,\
                category varchar(30))")

    w.execute("create table admin(id varchar(30) primary key,\
                name varchar(40))")

    t1=[[1, 'french fries', 'VEG', 80, 'fries'],\
       [2, 'Piri-Piri fries', 'VEG', 100, 'fries'],\
       [3, 'baked fries', 'VEG', 120, 'fries'],\
       [4, 'chis pijja', 'VEG', 100, 'pizza'],\
       [5, 'pineapple pijja', 'VEG', 100, 'pizza'],\
       [6, 'chow roll', 'VEG', 75, 'rolls'],\
       [7, 'chik roll', 'NON-VEG', 120, 'rolls'],\
       [8, 'grilled sundwitch', 'VEG', 50, 'sandwich']]

    t2=[["w01","rahul"],["w02","rashmi"]]

    w.executemany("insert into menu values(%s,%s,%s,%s,%s)",t1)

    w.executemany("insert into admin values(%s,%s)",t2)

    q.commit()

test=0
tp=0        
bill=""     

while test<1:
    w.execute("select * from menu")
    w2=w.fetchall() 
    r=pd.DataFrame(w2,columns=["S.no",\
                              "Dish name",\
                              "type",\
                              "price",\
                              "category"])

    w.execute("select * from admin")
    w2=w.fetchall()
    r1=pd.DataFrame(w2,columns=["id","name"])
    


    a=int(input("Enter Your Choice "))
    print()

    if a==1:
        print("""        Press 1 to display whole menu
        Press 2 to apply Search Filters""")
        print()

        b1=int(input("Enter Your Choice "))
        print()

        if b1==1:
            print(r)
            print()

        elif b1==2:
            print("""        1 to search category-wise
        2 to search type-wise""")
            print()

            b2=int(input("Enter Your Choice "))
            print()

            if b2==1:
                b3=eval(input("Enter Category "))
                print()

                print(r[r["category"].isin(b3)])
                
            elif b2==2:
                b3=eval(input("Enter Type "))
                print()

                print(r[r["type"].isin(b3)])
        print()

    
    if a==2:
        a1=eval(input("Enter Item codes "))
        print()
        print("   !!! - thank you for ordering - !!!")
        print("       please find your bill down    ")
        print()
        print("="*98)
        print()
        for a4 in a1:
            for a2,row in r.iterrows(): 
                if int(a4)==row[0]:
                        tp+=row[3]
                        bill=row[1]+\
                              " "*(49-len(row[1]\
                            +str(row[3])))\
                            +str(row[3])
                        print(bill)
                        print("-"*49)
        print()
        print("="*98)
        print()
        print("Net Bill"+" "*(40-len(str(tp))),tp)
        print("-"*49)
        print("TAXES"+" "*(43-\
                           len(str(round(tp*0.18,2)))),\
                           round(tp*0.18,2))
        print("-"*49)
        print()
        print("="*49)
        print("Final Pay"+" "*(39-\
                           len(str(round(tp*0.18+tp))))\
                               ,round(tp+tp*0.18))
        print("="*49)
        print()
        print("   Thank You and have a \
Wonderful Day\n   or night, \
or whatever suits you")
        print()
        print("="*98)
        print()
              

    elif a==3:

        c1=input("enter id ")
        c2=input("enter name ")

        for c3,row in r1.iterrows():

            if c1==row[0] and c2==row[1]:

                d1=r.shape[0]+1
                d2=input("Enter Dish Name ")
                d3=input("Enter its Type ")
                d4=int(input("Enter Price "))
                d5=input("Enter Category ")
                d6=[d1,d2,d3,d4,d5]
                w.execute("insert into menu values(%s,%s,%s,%s,%s)",d6)
                q.commit()
                print()
                print("menu updated")

            elif c1!=row[0] or c2!=row[1]:
                c4=0

        if c4==0:
                print("Access Denied")

    elif a==0:
        
        print("happy to serve you :-) ")

        q.close()

        break
                             
            
        
   
        

    
