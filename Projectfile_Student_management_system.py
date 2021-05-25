from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1920x1080+0+0") 

        title=Label(self.root,text="Student Mangement System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #*************ALL VARIABLES*************#
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.branch_var=StringVar()
        self.yop_var=StringVar()
        self.city_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        #****************************MANAGE FRAME*******************************************#

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=550,height=680)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15,padx=20)
        
        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=15,padx=15,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable= self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=15,padx=65,sticky="w")
        
        lbl_roll=Label(Manage_Frame,text="Roll No",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=2,column=0,pady=15,padx=15,sticky="w")
        txt_roll=Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=2,column=1,pady=15,padx=65,sticky="w")
        '''
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_Gender.grid(row=3,column=0,pady=15,padx=15,sticky="w")
        txt_Gender=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Gender.grid(row=3,column=1,pady=15,padx=65,sticky="w")
        '''
        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=3,column=0,pady=15,padx=15,sticky="w")
        txt_Email=Entry(Manage_Frame,textvariable= self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=15,padx=65,sticky="w")

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_Contact.grid(row=4,column=0,pady=15,padx=15,sticky="w")
        txt_Contact=Entry(Manage_Frame,textvariable= self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=4,column=1,pady=15,padx=65,sticky="w")

        lbl_dob=Label(Manage_Frame,text="DOB",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_dob.grid(row=5,column=0,pady=15,padx=15,sticky="w")
        txt_dob=Entry(Manage_Frame,textvariable= self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=5,column=1,pady=15,padx=65,sticky="w")

        lbl_branch=Label(Manage_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_branch.grid(row=6,column=0,pady=15,padx=15,sticky="w")
        txt_branch=Entry(Manage_Frame,textvariable= self.branch_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_branch.grid(row=6,column=1,pady=15,padx=65,sticky="w")       

        lbl_yop=Label(Manage_Frame,text="Year of Passing",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_yop.grid(row=7,column=0,pady=15,padx=15,sticky="w")
        txt_yop=Entry(Manage_Frame,textvariable= self.yop_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_yop.grid(row=7,column=1,pady=15,padx=65,sticky="w")

        lbl_city=Label(Manage_Frame,text="City",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_city.grid(row=8,column=0,pady=15,padx=15,sticky="w")
        txt_city=Entry(Manage_Frame,textvariable= self.city_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_city.grid(row=8,column=1,pady=15,padx=65,sticky="w")

        #********************************BUTTON FRAME******************************************************#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=600,width=470)

        Addbtn=Button(btn_Frame,text="Add",width=12,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=12,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=12,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=12,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #****************************Detail FRAME*******************************************#
        
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=600,y=100,width=910,height=680)

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",25,"bold"))
        lbl_search.grid(row=0,column=0,pady=15,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=30,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=15,padx=30,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=12,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show all",width=12,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #***********************************TABLE FRAME*************************************#
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=20,y=70,width=860,height=600)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("name","roll","email","contact","dob","branch","yop","city"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("email",text="Email id")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="Date of Birth")
        self.Student_table.heading("branch",text="Branch")
        self.Student_table.heading("yop",text="Year of Passing")
        self.Student_table.heading("city",text="City")
        self.Student_table['show']='headings'
        self.Student_table.column("name",width=150)
        self.Student_table.column("roll",width=150)
        self.Student_table.column("email",width=150)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("branch",width=100)
        self.Student_table.column("yop",width=100)
        self.Student_table.column("city",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.name_var.get()=="" or self.Roll_No_var.get()=="":
            messagebox.showerror("Error","Name and roll are required.")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(), 
                                                                                    self.Roll_No_var.get(), 
                                                                                    self.email_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.branch_var.get(),
                                                                                    self.yop_var.get(),
                                                                                    self.city_var.get() ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.name_var.set("")
        self.Roll_No_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.branch_var.set("")
        self.yop_var.set("")
        self.city_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.name_var.set(row[0])
        self.Roll_No_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[3])
        self.dob_var.set(row[4])
        self.branch_var.set(row[5])
        self.yop_var.set(row[6])
        self.city_var.set(row[7])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set roll_no=%s,email=%s,contact=%s,dob=%s,branch=%s,yop=%s,city=%s where name=%s",(
                                                                            self.Roll_No_var.get(), 
                                                                            self.email_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.branch_var.get(),
                                                                            self.yop_var.get(),
                                                                            self.city_var.get(),
                                                                            self.name_var.get() ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("Delete from students where name=%s",self.name_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()