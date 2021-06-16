from tkinter import*
from tkinter import messagebox
from functools import partial
import pymysql


class login_data:
    def __init__(self):
        self.a=Tk()
        b="#126e82"
        self.a.title("Sign in Window")
        self.a.geometry("1350x700+0+0")
        self.a.configure(background=b)
        f="times new roman"
        
        title_lbl=Label(self.a,text="Sign in",font=(f,50,"bold"),bg=b,fg="white").place(x=0,y=0,relwidth=1,height=100)

        lbl_fname=Label(self.a,text='First Name *',bg="#126e82",fg="white",font=(f,20)).place(x=200,y=170,height=40)
        self.fname=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.fname.place(x=200,y=210,height=40,width=300)

        lbl_lname=Label(self.a,text='Last Name *',bg="#126e82",fg="white",font=(f,20)).place(x=900,y=170,height=40)
        self.lname=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.lname.place(x=900,y=210,height=40,width=300)

        lbl_contact=Label(self.a,text='Contact No. *',bg="#126e82",fg="white",font=(f,20)).place(x=200,y=270,height=40)
        self.contact=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.contact.place(x=200,y=310,height=40,width=300)

        lbl_add=Label(self.a,text='Address *',bg="#126e82",fg="white",font=(f,20)).place(x=900,y=270,height=40)
        self.address=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.address.place(x=900,y=310,height=40,width=300)

        lbl_username=Label(self.a,text='User Name *',bg="#126e82",fg="white",font=(f,20)).place(x=200,y=370,height=40)
        self.username=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.username.place(x=200,y=410,height=40,width=300)

        lbl_email=Label(self.a,text='Email ID *',bg="#126e82",fg="white",font=(f,20)).place(x=900,y=370,height=40)
        self.email=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.email.place(x=900,y=410,height=40,width=300)

        lbl_pass=Label(self.a,text='Password *',bg="#126e82",fg="white",font=(f,20)).place(x=200,y=470,height=40)
        self.password=Entry(self.a,bg="lightgray",bd=5,font=(f,22))
        self.password.place(x=200,y=510,height=40,width=300)

        lbl_cpass=Label(self.a,text='Confirm Password *',bg="#126e82",fg="white",font=(f,20)).place(x=900,y=470,height=40)
        self.cpass=Entry(self.a, bg="lightgray",bd=5,font=(f,22))
        self.cpass.place(x=900,y=510,height=40,width=300)

        btn_signin=Button(self.a,text="Submit ",bg="#126e82",fg="white",font=(f,22),command=self.register_info).place(x=600,y=600,width=150,height=60)

    def register_info(self):
        if self.fname.get()=="" or self.lname.get()=="" or self.contact.get()=="" or self.address.get()=="" or self.username.get()=="" or self.email.get()=="" or self.password.get()=="" or self.cpass.get()=="" :
            messagebox.showerror("Error","* fields are mandatory.",parent=self.a)
        elif len(self.contact.get())!=10 or self.contact.get().isdigit()!=True:
            messagebox.showerror("Error","Enter 10 digit valid number.",parent=self.a)
        elif self.password.get()!=self.cpass.get():
            messagebox.showerror("Error","Password and Confirm Password are not same.",parent=self.a)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="grocery")
                cur=con.cursor()
                cur.execute("select * from info where email=%s",self.email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User already exist, use another email id... ",parent=self.a)
                else:
                    cur.execute("insert into info (fname, lname, contact, address, username, email, password) values (%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.fname.get(),
                                self.lname.get(),
                                self.contact.get(),
                                self.address.get(),
                                self.username.get(),
                                self.email.get(),
                                self.password.get(),
                            ))
                    con.commit()
                    messagebox.showinfo("Successful","Registration Successful.",parent=self.a)
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error",str(e),parent=self.a)
            finally:
                con.close()
    
    def clear_fields(self):
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.contact.delete(0,END)
        self.address.delete(0,END)
        self.username.delete(0,END)
        self.email.delete(0,END)
        self.password.delete(0,END)
        self.cpass.delete(0,END)

