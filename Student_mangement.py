from tkinter import *
import tkinter.messagebox  as MessageBox
import mysql.connector as mysql

def submit():
    name=entry_name.get()
    dob=entry_dob.get()
    usn=entry_usn.get()
    phone=entry_phone.get()
    branch=entry_branch.get()
    section=entry_section.get()
    address=entry_address.get()

    if(name=='' or dob==''or usn==''or phone=='' or branch=='' or section=='' or address==''):
        MessageBox.showinfo('submit Status','All Feilds are requird')
 
    else:
        con=mysql.connect(host='localhost',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("insert into student values('"+name+"','"+dob+"','"+usn+"','"+phone+"','"+branch+"','"+section+"','"+address+"')")
        cursor.execute("commit")

        entry_name.delete(0,'end')
        entry_dob.delete(0,'end')
        entry_usn.delete(0,'end')
        entry_phone.delete(0,'end')
        entry_branch.delete(0,'end')
        entry_section.delete(0,'end')
        entry_address.delete(0,'end')
        MessageBox.showinfo("Submit Status","Submitted successfully")
        con.close()

def delete():
    if entry_usn.get()=='':
        MessageBox.showinfo('Delete Status','USN is compalsory for delete')
    else:
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("delete from student where  usn='"+entry_usn.get()+"'")
        cursor.execute("commit");

        entry_name.delete(0,'end')
        entry_dob.delete(0,'end')
        entry_usn.delete(0,'end')
        entry_phone.delete(0,'end')
        entry_branch.delete(0,'end')
        entry_section.delete(0,'end')
        entry_address.delete(0,'end')
        MessageBox.showinfo("Delete Status","Deleted successfully");
        con.close()



def update():
    name=entry_name.get()
    dob=entry_dob.get()
    usn=entry_usn.get()
    phone=entry_phone.get()
    branch=entry_branch.get()
    section=entry_section.get()
    address=entry_address.get()

    if(name=='' or dob==''or usn==''or phone=='' or branch=='' or section=='' or address==''):
        MessageBox.showinfo('Update Status','All Feilds are requird')
 
    else:
        con=mysql.connect(host='localhost',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("update student set name='"+name+"',dob='"+dob+"',usn='"+usn+"',phone='"+phone+"',branch='"+branch+"',section='"+section+"',address='"+address+"'")
        cursor.execute("commit")

        entry_name.delete(0,'end')
        entry_dob.delete(0,'end')
        entry_usn.delete(0,'end')
        entry_phone.delete(0,'end')
        entry_branch.delete(0,'end')
        entry_section.delete(0,'end')
        entry_address.delete(0,'end')
        MessageBox.showinfo("update Status","Updated successfully")
        con.close()


def get():
    if entry_usn.get()=='':
        MessageBox.showinfo('fetch Status','USN is compalsory for  Fetch data')
    else:
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("select * from student where usn='"+entry_usn.get()+"'")
        rows=cursor.fetchall()

        for row in rows:
            entry_name.insert(0,row[0])
            entry_dob.insert(0,row[1])
            entry_phone.insert(0,row[3])
            entry_branch.insert(0,row[4])
            entry_section.insert(0,row[5])
            entry_address.insert(0,row[6])
            
        con.close()

def show():
        con=mysql.connect(host='127.0.0.1 ',user='root',password='',database='student_info')
        cursor=con.cursor()
        cursor.execute("select * from student ")
        rows=cursor.fetchall()

        for row in rows:
            insertData=row[0]+'   '+row[1]+'   '+row[2]+'   '+str(row[3])+'   '+row[4]+'   '+row[5]+'   '+row[6]
            list_s.insert(list_s.size()+1,insertData)

        con.close()


    
    
win =Tk()
win.title("STUDENT DETAILES")
win.geometry("1800x900")
win.configure(bg='black')

name= StringVar()
dob=StringVar()
usn=StringVar()
phone=IntVar()
branch=StringVar()
section=StringVar()
address=StringVar()


Label(win,text='\u2680 Student Registration Form \u2680',font=('italic',30,'bold'),bg="cyan",fg="black").place(x=450,y=20)

Label(win,text="STUDENT NAME :",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=120)
entry_name = Entry(win,textvariable=name,relief = "solid")
entry_name.place(x=290,y=120,height=30,width=200)


Label(win,text="DATE OF BIRTH: ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=190)
entry_dob = Entry(win,textvariable=dob,relief = "solid")
entry_dob.place(x=290,y=190,height=30,width=200)

Label(win,text="USN : ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=260)
entry_usn= Entry(win,textvariable=usn,relief = "solid")
entry_usn.place(x=290,y=260,height=30,width=200)

Label(win,text="MOBILE NO : ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=330)
entry_phone= Entry(win,textvariable=phone,relief = "solid")
entry_phone.place(x=290,y=330,height=30,width=200)

Label(win,text="BRANCH : ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=400)
entry_branch= Entry(win,textvariable=branch,relief = "solid")
entry_branch.place(x=290,y=400,height=30,width=200)

Label(win,text="SECTION : ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=470)
entry_section= Entry(win,textvariable=section,relief = "solid")
entry_section.place(x=290,y=470,height=30,width=200)


Label(win,text="ADDRESS : ",font=('Arial',15,'bold'),bg="yellow",fg="black").place(x=10,y=540)
entry_address= Entry(win,textvariable=address,relief = "solid")
entry_address.place(x=290,y=540,height=30,width=200)


submit=Button(win,text='Submit',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=submit,relief = "solid")
submit.place(x=100,y=700)

delete=Button(win,text='Delete',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=delete,relief = "solid")
delete.place(x=400,y=700)

update=Button(win,text='Update',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=update,relief = "solid")
update.place(x=700,y=700)

get=Button(win,text='Get',font=('italic',15,'bold'),width=10,height=1,bd=4,bg='orange',command=get,relief = "solid")
get.place(x=1000,y=700)

list_s=Listbox(win,font=('Times New Roman',10,'bold'),bg='yellow',bd=2,relief='sunken')
list_s.place(x=650,y=100,width=850, height=500)
show()
win.mainloop()

