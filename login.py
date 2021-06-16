from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from functools import partial
import pymysql
import signin
import resetpass


class valid_login:
        def __init__(self,username,password):
            
            self.username=username.get()
            self.password=password.get()    
            
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="grocery")
                cur=con.cursor()
                cur.execute("select username from info where username=%s",self.username)
                user_name=cur.fetchone()
                cur.execute("select password from info where username=%s",user_name[0])
                pass_word=cur.fetchone()
                if self.username=="" or self.password=="":
                    messagebox.showerror("Error","Enter username and password both")
                elif self.username==user_name[0] and self.password==pass_word[0]:
                    messagebox.showinfo("Successfull",f"Welcome {username.get()}")
                    
                else :
                    messagebox.showerror("Error","Invalid username or password")
                con.close()
                                
            except Exception as e:
                messagebox.showerror("Error",str(e))

            

class LoginSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#126e82")
        a="times new roman"

        
        #Title of Login Window
        self.title=Label(self.root,text='User Login',bg="#126e82",fg="white",font=("times new roman",40,"bold")).place(x=0,y=50,relwidth=1)

        #First Image of page i.e. login icon 
        image=Image.open("Images\\login.jpeg")
        image=image.resize((150,150),Image.ANTIALIAS)
        self.login_icon=ImageTk.PhotoImage(image)
        login_icon=Label(self.root,image=self.login_icon,bg="#126e82",bd=5).place(x=600,y=150)

        #Login Frame
        frame2=Frame(self.root,bg="#126e82")
        frame2.place(x=450,y=370,width=600,height=400)

        #Label and TextField for username 
        image=Image.open("Images\\user.jpeg")
        image=image.resize((20,20),Image.ANTIALIAS)
        self.user_icon=ImageTk.PhotoImage(image)
        username_Label=Label(frame2,text='User Name',image=self.user_icon,compound=LEFT,bg="#126e82",fg="white",font=(a,25)).grid(row=1, column=0)
        self.username=StringVar()
        username_Entry=Entry(frame2,textvariable=self.username,font=(a,22)).grid(row=1, column=1,padx=20,pady=10)

        #Label and TextField for password
        image=Image.open("Images\\pass.jpeg")
        image=image.resize((20,20),Image.ANTIALIAS)
        self.pass_icon=ImageTk.PhotoImage(image)
        password_Label=Label(frame2,text='Password',image=self.pass_icon,compound=LEFT,bg="#126e82",fg="white",font=(a,25)).grid(row=2,column=0,padx=20)
        self.password=StringVar()
        password_Entry=Entry(frame2, textvariable=self.password, show='*',font=(a,22)).grid(row=2,column=1,padx=20,pady=10)

        #Checkbox for Remember me option
        check1=IntVar()
        Checkbutton(frame2, text="Remember me",bg="#126e82", variable=check1,font=(a,22)).grid(row=3,column=1)

        frgt_btn=Button(frame2,text="Forgot your password....",bg="#126e82",fg="white",bd=0,command=resetpass.ChangePassword,font=(a,15),width=25).grid(row=4,column=0)

        self.valid_login = partial(valid_login, self.username, self.password)

        #Sign in Button
        btn_sign=Button(frame2,text="Sign in",bg="#126e82",command=signin.login_data,font=(a,22),width=7).grid(row=5,column=0,pady=10)

        #Login Button
        btn_login=Button(frame2,text="Login",bg="#126e82",font=(a,22),width=7,command=self.valid_login).grid(row=5,column=1,pady=50)



    

