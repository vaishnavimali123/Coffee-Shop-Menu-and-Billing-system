from tkinter import *
import pymysql
from tkinter import messagebox

def Ok():
    Pizza=e1.get()
    Burger=e2.get()
    Cold_Coffee=e3.get()
    Paneer_Roll=e4.get()
    Sandwich=e5.get()
    conn=pymysql.connect(host="localhost",user="root",password="",db="coffee")
    myCursor=conn.cursor()

    try:
        sql="INSERT INTO item(Pizza,Burger,Cold_Coffee,Paneer_Roll,Sandwich) VALUES (%s,%s,%s,%s,%s)"
        val=(Pizza,Burger,Cold_Coffee,Paneer_Roll,Sandwich)
        myCursor.execute(sql,val)
        conn.commit()
        messagebox.showinfo("Information","Record inserted successfully...")
        
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()
Ht=Tk()
Ht.geometry("700x500")
global e1
global e2
global e3
global e4
global e5
def calculate():
    Pizza=e1.get()
    Burger=e2.get()
    Cold_Coffee=e3.get()
    Paneer_Roll=e4.get()
    Sandwich=e5.get()
    total=((int(Pizza)*100)+(int(Burger)*120)+(int(Cold_Coffee)*40)+(int(Paneer_Roll)*90)+(int(Sandwich)*60))
    
    label14=Label(Ht,text=total,font="times 18")
    label14.place(x=200,y=520)



label1=Label(Ht,text="Coffee Shop",font="times 40 bold")
label1.place(x=350,y=20,anchor="center")

label2=Label(Ht,text="MENU",font="times 28 bold")
label2.place(x=450,y=70)

label3=Label(Ht,text="Pizza              Rs 100",font="times 18")
label3.place(x=450,y=120)

label4=Label(Ht,text="Burger            Rs 120",font="times 18")
label4.place(x=450,y=180)

label5=Label(Ht,text="Cold Coffee   Rs 40",font="times 18")
label5.place(x=450,y=150)

label6=Label(Ht,text="Paneer Roll    Rs 90",font="times 18")
label6.place(x=450,y=210)

label7=Label(Ht,text="Sandwich       Rs 60",font="times 18")
label7.place(x=450,y=240)


label8=Label(Ht,text="Select the menu  ",font="times 20 bold")
label8.place(x=70,y=70)

label9=Label(Ht,text="Pizza ",font="times 20 bold")
label9.place(x=20,y=120)

e1=Entry(Ht)
e1.place(x=20,y=150)

label10=Label(Ht,text="Burger ",font="times 20 bold")
label10.place(x=20,y=180)

e2=Entry(Ht)
e2.place(x=20,y=210)

label11=Label(Ht,text="Cold Coffee ",font="times 20 bold")
label11.place(x=20,y=250)

e3=Entry(Ht)
e3.place(x=20,y=280)

label12=Label(Ht,text="Paneer Roll ",font="times 20 bold")
label12.place(x=20,y=310)

e4=Entry(Ht)
e4.place(x=20,y=350)

label13=Label(Ht,text="Sandwich ",font="times 20 bold")
label13.place(x=20,y=380)

e5=Entry(Ht)
e5.place(x=20,y=410)

bt=Button(Ht,text="Calculate Bill",command=Ok,width=20)
bt.place(x=200,y=450)

bt1=Button(Ht,text="show total amount",command=calculate,width=20)
bt1.place(x=200,y=480)


Ht.mainloop()
                
