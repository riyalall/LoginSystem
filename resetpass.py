from tkinter import *
from tkinter import messagebox
import pymysql
        
class ChangePassword:
    def __init__(self):
        self.a=Tk()
        self.a.title("Change Password")
        self.a.geometry("1350x700+0+0")
        self.a.configure(background="#126e82")
        f="times new roman"

        title_lbl=Label(self.a,text="To reset your Password",font=(f,30),bg="#126e82",fg="white").place(x=0,y=50,relwidth=1,height=50)

        
        lbl_username=Label(self.a,text='Enter Username',bg="#126e82",fg="white",font=(f,20)).place(x=400,y=210,height=50)
        self.username=Entry(self.a,bg="#126e82",bd=2,fg="white",font=(f,15))
        self.username.place(x=750,y=210,height=50,width=310)

        lbl_password=Label(self.a,text='Enter new Password',bg="#126e82",fg="white",font=(f,20)).place(x=400,y=310,height=50)
        self.password=Entry(self.a,show='*',bg="#126e82",bd=2,fg="white",font=(f,15))
        self.password.place(x=750,y=310,height=50,width=310)

        lbl_cpass=Label(self.a,text='Re-Enter your password',bg="#126e82",fg="white",font=(f,20)).place(x=400,y=410,height=50)
        self.spassword=Entry(self.a,show='*',bg="#126e82",bd=2,fg="white",font=(f,15))
        self.spassword.place(x=750,y=410,height=50,width=310)

        ch_pas=Button(self.a,text="Set Password",bg="#126e82",fg="white",font=(f,22),command=self.update_password)
        ch_pas.place(x=520,y=560,height=50,width=330)

    def update_password(self):
        self.username=self.username.get()
        self.password=self.password.get()
        self.spassword=self.spassword.get()

        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="grocery")
            cur=con.cursor()
            cur.execute("select username from info where username=%s",self.username)
            user_name=cur.fetchone()
            if user_name==None:
                messagebox.showerror("Error","Invalid Username")
            elif self.password!=self.spassword:
                messagebox.showerror("Error","Password doesn't match!")
            else:
                cur.execute("update info set password=%s where username=%s",(self.password,self.username))
                cur.execute("select password from info where username=%s",self.username)
                pass_word=cur.fetchone()
                if self.password==pass_word[0]:
                    messagebox.showinfo("Successfull","Password Changed...")
            con.commit()
            con.close()
                                
        except Exception as e:
            messagebox.showerror("Error",str(e))
