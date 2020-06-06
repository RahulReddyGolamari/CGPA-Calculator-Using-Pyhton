from tkinter import *
import os
def main_screen():
    global screen
    screen =Tk()
    screen.geometry("300x250")
    screen.title("SIGN UP",) #to store
    Label(text="SIGN UP", bg="Grey", width ="300", height="2", font=("Garamond",15)).pack()
    Label(text ="").pack()
    Button(text="Login",bg="Silver", height="2", width = "40", command=login).pack()
    Label(text ="").pack()
    Button(text="Register",bg="Silver",height="2", width = "40", command=register).pack()
    
    screen.mainloop()
    

def register():
    global screen1

    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()

    Label(screen1, text ="Please Enter details below").pack()
    Label(screen1, text ="").pack()

    Label(screen1, text ="Username").pack()
    username_entry=Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text ="Password").pack()
    password_entry=Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text ="").pack()
    Button(screen1,text="Register",bg="Silver",height=2, width = 10, command=reg_user).pack()
    
    
    
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text ="Please Enter details below to Login").pack()
    Label(screen2, text ="").pack()
    
    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()
    
    global username_entry1
    global password_entry1
    
    Label(screen2, text ="Username").pack()
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text ="").pack()
    
    Label(screen2, text ="Password").pack()
    password_entry1=Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text ="").pack()
   
    Button(screen2, text="Login", height=1, width=10, command=login_verify).pack()
def reg_user():

    username_info = username.get()
    password_info = password.get()
    
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registered successfully", fg="green", font=("calibri",11)).pack()
    
    
    
    
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            cgpa()
        else:
            Password_not_recognised()
    else:
        user_not_defined()
        
    
    
def Password_not_recognised():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("unsuccessful")
    screen4.geometry("150x100")
    Label(screen4, text ="Password invalid").pack()
    Button(screen4, text="OK", command=delete3).pack()
    
def user_not_defined():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("unsuccessful")
    screen5.geometry("150x100")
    Label(screen5, text ="User not defined").pack()
    Button(screen5, text="OK", command=delete4).pack()
    
def delete3():
    screen4.destroy() 
def delete4():
    screen5.destroy()
    
    
def cgpa():
    screen2.destroy()
    global window
    window=Toplevel(screen)
    window.geometry("1080x1080")
    window.title("CGPA CALCULATION")
    
    
    
    
    
    l3=Listbox(window,width=103,height=26,font="AgencyFB 18",bg="light blue")
    l3.grid(row=0,column=0,columnspan=10,rowspan=15)
    
    l=Label(window,text="Course",bg="skyblue4")
    l.grid(row=0,column=0)
    
    
    
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16
    global c17
    global c18
    global c19
    global c20
    global c21
    global c22
    global c23
    global c24
    global c25
    global c26
    global c27
    global c28
    global c29
    global c30
    global c31
    global c32
    global c33
    global c34
    global c35
    global c36
    global c37
    global c38
    global c39
    global c40
    global c41
    global c42
    global c43
    global c44
    global c45
    global c46
    global c47
    global c48
    global c49
    global c50
    global c51
    
    
    
    c1=StringVar()
    e=Entry(window,textvariable=c1)
    e.grid(row=1,column=0)
    
    l=Label(window,text="CA1",bg="skyblue4")
    l.grid(row=0,column=1)
    
    c2=IntVar()
    e=Entry(window,textvariable=c2)
    e.grid(row=1,column=1)
    
    l=Label(window,text="CA2",bg="skyblue4")
    l.grid(row=0,column=2)
    
    c3=IntVar()
    e=Entry(window,textvariable=c3)
    e.grid(row=1,column=2)
    
    l=Label(window,text="MTE",bg="skyblue4")
    l.grid(row=0,column=3)
    
    c4=IntVar()
    e=Entry(window,textvariable=c4)
    e.grid(row=1,column=3)
    
    
    l=Label(window,text="ETE",bg="skyblue4")
    l.grid(row=0,column=4)
    
    c5=IntVar()
    e=Entry(window,textvariable=c5)
    e.grid(row=1,column=4)
    
    l=Label(window,text="Att_marks",bg="skyblue4")
    l.grid(row=0,column=5)
    
    c6=IntVar()
    e=Entry(window,textvariable=c6)
    e.grid(row=1,column=5)
    
    l=Label(window,text="Credits",bg="skyblue4")
    l.grid(row=0,column=6)
    
    c7=IntVar()
    e=Entry(window,textvariable=c7)
    e.grid(row=1,column=6)
    
    
    
    
    
    c8=StringVar()
    e=Entry(window,textvariable=c8)
    e.grid(row=2,column=0)
    
    c9=IntVar()
    e=Entry(window,textvariable=c9)
    e.grid(row=2,column=1)
    
    c10=IntVar()
    e=Entry(window,textvariable=c10)
    e.grid(row=2,column=2)
    
    c11=IntVar()
    e=Entry(window,textvariable=c11)
    e.grid(row=2,column=3)
    
    c12=IntVar()
    e=Entry(window,textvariable=c12)
    e.grid(row=2,column=4)
    
    c13=IntVar()
    e=Entry(window,textvariable=c13)
    e.grid(row=2,column=5)
    
    c14=IntVar()
    e=Entry(window,textvariable=c14)
    e.grid(row=2,column=6)
    
    
    
    
    
    
    
    
    c15=StringVar()
    e=Entry(window,textvariable=c15)
    e.grid(row=3,column=0)
    
    c16=IntVar()
    e=Entry(window,textvariable=c16)
    e.grid(row=3,column=1)
    
    c17=IntVar()
    e=Entry(window,textvariable=c17)
    e.grid(row=3,column=2)
    
    c18=IntVar()
    e=Entry(window,textvariable=c18)
    e.grid(row=3,column=3)
    
    c19=IntVar()
    e=Entry(window,textvariable=c19)
    e.grid(row=3,column=4)
    
    c20=IntVar()
    e=Entry(window,textvariable=c20)
    e.grid(row=3,column=5)
    
    c21=IntVar()
    e=Entry(window,textvariable=c21)
    e.grid(row=3,column=6)
    
    
    
    
    
    
    
    
    c22=StringVar()
    e=Entry(window,textvariable=c22)
    e.grid(row=4,column=0)
    
    c23=IntVar()
    e=Entry(window,textvariable=c23)
    e.grid(row=4,column=1)
    
    c24=IntVar()
    e=Entry(window,textvariable=c24)
    e.grid(row=4,column=2)
    
    c25=IntVar()
    e=Entry(window,textvariable=c25)
    e.grid(row=4,column=3)
    
    c26=IntVar()
    e=Entry(window,textvariable=c26)
    e.grid(row=4,column=4)
    
    c27=IntVar()
    e=Entry(window,textvariable=c27)
    e.grid(row=4,column=5)
    
    c28=IntVar()
    e=Entry(window,textvariable=c28)
    e.grid(row=4,column=6)
    
    
    
    
    
    
    c29=StringVar()
    e=Entry(window,textvariable=c29)
    e.grid(row=5,column=0)
    
    c30=IntVar()
    e=Entry(window,textvariable=c30)
    e.grid(row=5,column=1)
    
    c31=IntVar()
    e=Entry(window,textvariable=c31)
    e.grid(row=5,column=2)
    
    c32=IntVar()
    e=Entry(window,textvariable=c32)
    e.grid(row=5,column=3)
    
    c33=IntVar()
    e=Entry(window,textvariable=c33)
    e.grid(row=5,column=4)
    
    c34=IntVar()
    e=Entry(window,textvariable=c34)
    e.grid(row=5,column=5)
    
    c35=IntVar()
    e=Entry(window,textvariable=c35)
    e.grid(row=5,column=6)
    
    
    
    
    
    
    
    c36=StringVar()
    e=Entry(window,textvariable=c36)
    e.grid(row=6,column=0)
    
    c37=IntVar()
    e=Entry(window,textvariable=c37)
    e.grid(row=6,column=1)
    
    c38=IntVar()
    e=Entry(window,textvariable=c38)
    e.grid(row=6,column=2)
    
    c39=IntVar()
    e=Entry(window,textvariable=c39)
    e.grid(row=6,column=3)
    
    c40=IntVar()
    e=Entry(window,textvariable=c40)
    e.grid(row=6,column=4)
    
    c41=IntVar()
    e=Entry(window,textvariable=c41)
    e.grid(row=6,column=5)
    
    c42=IntVar()
    e=Entry(window,textvariable=c42)
    e.grid(row=6,column=6)
    
    
    
    
    
    l=Label(window,text="Marks for PES")
    l.grid(row=7,column=1)
    
    l=Label(window,text="CA1",bg="skyblue4")
    l.grid(row=8,column=0)
    c43=IntVar()
    e=Entry(window,textvariable=c43)
    e.grid(row=9,column=0)
    
    l=Label(window,text="CA2",bg="skyblue4")
    l.grid(row=8,column=1)
    c44=IntVar()
    e=Entry(window,textvariable=c44)
    e.grid(row=9,column=1)
    
    l=Label(window,text="CA3",bg="skyblue4")
    l.grid(row=8,column=2)
    c45=IntVar()
    e=Entry(window,textvariable=c45)
    e.grid(row=9,column=2)
    
    l=Label(window,text="CA4",bg="skyblue4")
    l.grid(row=8,column=3)
    c46=IntVar()
    e=Entry(window,textvariable=c46)
    e.grid(row=9,column=3)
    
    l=Label(window,text="ETE",bg="skyblue4")
    l.grid(row=8,column=4)
    c47=IntVar()
    e=Entry(window,textvariable=c47)
    e.grid(row=9,column=4)
    
    l=Label(window,text="Att_marks",bg="skyblue4")
    l.grid(row=8,column=5)
    c48=IntVar()
    e=Entry(window,textvariable=c48)
    e.grid(row=9,column=5)
    
    l=Label(window,text="Credits",bg="skyblue4")
    l.grid(row=8,column=6)
    c49=IntVar()
    e=Entry(window,textvariable=c49)
    e.grid(row=9,column=6)    

    
    
    
    
    
    
    l=Label(window,text="Marks_for_MGN")
    l.grid(row=10,column=1)
    
    l=Label(window,text="ETE",bg="skyblue4")
    l.grid(row=11,column=1)
    c50=IntVar()
    e=Entry(window,textvariable=c50)
    e.grid(row=12,column=1)
    
    l=Label(window,text="Credits",bg="skyblue4")
    l.grid(row=11,column=2)
    c51=IntVar()
    e=Entry(window,textvariable=c51)
    e.grid(row=12,column=2)
    
    
       
    b3=Button(window, text="Estimate", height=2, width=20, bg="Silver", font=("Garamond",10), command=session)
    b3.grid(row=12, column=5)
    
    

def session():
    
    l2=Listbox(window,width=103,height=26,font="AgencyFB 18",bg="light blue")
    l2.grid(row=0,column=0,columnspan=10,rowspan=15)
    
    
    
    
    l=Label(window,text="Course",bg="skyblue4")
    l.grid(row=0,column=0)
    
    l=Label(window,text="TOTAL MARKS",bg="skyblue4")
    l.grid(row=0,column=1)
    
    l=Label(window,text="GRADE POINTS",bg="skyblue4")
    l.grid(row=0,column=2)
    
    l=Label(window,text="GRADES",bg="skyblue4")
    l.grid(row=0,column=3)
    
    l=Label(window,text="CGPA",bg="skyblue4")
    l.grid(row=4,column=4)
    
    e=Entry(window,textvariable=c1)
    e.grid(row=1,column=0)
    e=Entry(window,textvariable=c8)
    e.grid(row=2,column=0)
    e=Entry(window,textvariable=c15)
    e.grid(row=3,column=0)
    e=Entry(window,textvariable=c22)
    e.grid(row=4,column=0)
    e=Entry(window,textvariable=c29)
    e.grid(row=5,column=0)
    e=Entry(window,textvariable=c36)
    e.grid(row=6,column=0)
    e=Label(window,text="PES")
    e.grid(row=7,column=0)
    e=Label(window,text="MGN")
    e.grid(row=8,column=0)
    

    m1=c1.get()
    m2=c2.get()
    m3=c3.get()
    m4=c4.get()
    m5=c5.get()
    m6=c6.get()
    m7=c7.get()
    m8=c8.get()
    m9=c9.get()
    m10=c10.get()
    m11=c11.get()
    m12=c12.get()
    m13=c13.get()
    m14=c14.get()
    m15=c15.get()
    m16=c16.get()
    m17=c17.get()
    m18=c18.get()
    m19=c19.get()
    m20=c20.get()
    m21=c21.get()
    m22=c22.get()
    m23=c23.get()
    m24=c24.get()
    m25=c25.get()
    m26=c26.get()
    m27=c27.get()
    m28=c28.get()
    m29=c29.get()
    m30=c30.get()
    m31=c31.get()
    m32=c32.get()
    m33=c33.get()
    m34=c34.get()
    m35=c35.get()
    m36=c36.get()
    m37=c37.get()
    m38=c38.get()
    m39=c39.get()
    m40=c40.get()
    m41=c41.get()
    m42=c42.get()
    m43=c43.get()
    m44=c44.get()
    m45=c45.get()
    m46=c46.get()
    m47=c47.get()
    m48=c48.get()
    m49=c49.get()
    m50=c50.get()
    m51=c51.get()
    



    TC=m7+m14+m21+m28+m35+m42+m49+m51
    t1=m7/TC
    t2=m14/TC
    t3=m21/TC
    t4=m28/TC
    t5=m35/TC
    t6=m42/TC
    t7=m49/TC
    t8=m51/TC
    
    d1=((25*(m2+m3)/60)+(m4/2)+(50*m5/70)+m6)
    d2=((25*(m9+m10)/60)+(m11/2)+(50*m12/70)+m13)
    d3=((25*(m16+m17)/60)+(m18/2)+(50*m19/70)+m20)
    d4=((25*(m23+m24)/60)+(m25/2)+(50*m26/70)+m27)
    d5=((25*(m30+m31)/60)+(m32/2)+(50*m33/70)+m34)
    d6=((25*(m37+m38)/60)+(m39/2)+(50*m40/70)+m41)
    d7=((30*(m43+m44+m45+m45)/120)+(55*m47/100)+m48)
    d8=m50
    
    
    
    if d1>90:
        p1=10
        g1="O"
    elif 80<d1<91:
        p1=9
        g1="A+"
    elif 70<d1<81:
        p1=8
        g1="A"
    elif 60<d1<71:
        p1=7
        g1="B+"
    elif 50<d1<61:
        p1=6
        g1="B"
    elif 45<=d1<51:
        p1=5
        g1="C"
    elif 40<=d1<45:
        p1=4
        g1="D"
    else:
        p1=3
        g1="E"
    
    
    if d2>90:
        p2=10
        g2="O"
    elif 80<d2<91:
        p2=9
        g2="A+"
    elif 70<d2<81:
        p2=8
        g2="A"
    elif 60<d2<71:
        p2=7
        g2="B+"
    elif 50<d2<61:
        p2=6
        g2="B"
    elif 45<=d2<51:
        p2=5
        g2="C"
    elif 40<=d2<45:
        p2=4
        g2="D"
    else:
        p2=3
        g2="E"
        
        
    if d3>90:
        p3=10
        g3="O"
    elif 80<d3<91:
        p3=9
        g3="A+"
    elif 70<d3<81:
        p3=8
        g3="A"
    elif 60<d3<71:
        p3=7
        g3="B+"
    elif 50<d3<61:
        p3=6
        g3="B"
    elif 45<=d3<51:
        p3=5
        g3="C"
    elif 40<=d3<45:
        p3=4
        g3="D"
    else:
        p3=3
        g3="E"
        
        
    if d4>90:
        p4=10
        g4="O"
    elif 80<d4<91:
        p4=9
        g4="A+"
    elif 70<d4<81:
        p4=8
        g4="A"
    elif 60<d4<71:
        p4=7
        g4="B+"
    elif 50<d4<61:
        p4=6
        g4="B"
    elif 45<=d4<51:
        p4=5
        g4="C"
    elif 40<=d4<45:
        p4=4
        g4="D"
    else:
        p4=3
        g4="E"
        
        
    if d5>90:
        p5=10
        g5="O"
    elif 80<d5<91:
        p5=9
        g5="A+"
    elif 70<d5<81:
        p5=8
        g5="A"
    elif 60<d5<71:
        p5=7
        g5="B+"
    elif 50<d5<61:
        p5=6
        g5="B"
    elif 45<=d5<51:
        p5=5
        g5="C"
    elif 40<=d5<45:
        p5=4
        g5="D"
    else:
        p5=3
        g5="E"
        
        
    if d6>90:
        p6=10
        g6="O"
    elif 80<d6<91:
        p6=9
        g6="A+"
    elif 70<d6<81:
        p6=8
        g6="A"
    elif 60<d6<71:
        p6=7
        g6="B+"
    elif 50<d6<61:
        p6=6
        g6="B"
    elif 45<=d6<51:
        p6=5
        g6="C"
    elif 40<=d6<45:
        p6=4
        g6="D"
    else:
        p6=3
        g6="E"
        
        
    if d7>90:
        p7=10
        g7="O"
    elif 80<d7<91:
        p7=9
        g7="A+"
    elif 70<d7<81:
        p7=8
        g7="A"
    elif 60<d7<71:
        p7=7
        g7="B+"
    elif 50<d7<61:
        p7=6
        g7="B"
    elif 45<=d7<51:
        p7=5
        g7="C"
    elif 40<=d7<45:
        p7=4
        g7="D"
    else:
        p7=3
        g7="E"
        
        
    if d8>90:
        p8=10
        g8="O"
    elif 80<d8<91:
        p8=9
        g8="A+"
    elif 70<d8<81:
        p8=8
        g8="A"
    elif 60<d8<71:
        p8=7
        g8="B+"
    elif 50<d8<61:
        p8=6
        g8="B"
    elif 45<=d8<51:
        p8=5
        g8="C"
    elif 40<=d8<45:
        p8=4
        g8="D"
    else:
        p8=3
        g8="E"
    
    
    
    cgpa=(t1*p1)+(t2*p2)+(t3*p3)+(t4*p4)+(t5*p5)+(t6*p6)+(t7*p7)+(t8*p8)
  
    e=Label(window,text=d1)
    e.grid(row=1,column=1)
    e=Label(window,text=d2)
    e.grid(row=2,column=1)
    e=Label(window,text=d3)
    e.grid(row=3,column=1)
    e=Label(window,text=d4)
    e.grid(row=4,column=1)
    e=Label(window,text=d5)
    e.grid(row=5,column=1)
    e=Label(window,text=d6)
    e.grid(row=6,column=1)
    e=Label(window,text=d7)
    e.grid(row=7,column=1)
    e=Label(window,text=d8)
    e.grid(row=8,column=1)
    
    
    e=Label(window,text=p1)
    e.grid(row=1,column=2)
    e=Label(window,text=p2)
    e.grid(row=2,column=2)
    e=Label(window,text=p3)
    e.grid(row=3,column=2)
    e=Label(window,text=p4)
    e.grid(row=4,column=2)
    e=Label(window,text=p5)
    e.grid(row=5,column=2)
    e=Label(window,text=p6)
    e.grid(row=6,column=2)
    e=Label(window,text=p7)
    e.grid(row=7,column=2)
    e=Label(window,text=p8)
    e.grid(row=8,column=2)
    

    e=Label(window,text=g1)
    e.grid(row=1,column=3)
    e=Label(window,text=g2)
    e.grid(row=2,column=3)
    e=Label(window,text=g3)
    e.grid(row=3,column=3)
    e=Label(window,text=g4)
    e.grid(row=4,column=3)
    e=Label(window,text=g5)
    e.grid(row=5,column=3)
    e=Label(window,text=g6)
    e.grid(row=6,column=3)
    e=Label(window,text=g7)
    e.grid(row=7,column=3)
    e=Label(window,text=g8)
    e.grid(row=8,column=3)
    
    
    e=Label(window,text=cgpa)
    e.grid(row=5,column=4)
main_screen()