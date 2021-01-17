import smtplib
from tkinter import *
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Email:')
        self.lbl2=Label(win, text='Password:')
        self.lbl3=Label(win, text='Email address of person you want to send the email to:')
        self.lbl4=Label(win, text='Subject:')
        self.lbl5=Label(win, text='Main Message:')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.b2 = Button(win, text='Send email:',command = self.sendEmail)
        self.b3 = Button(win, text='Formal',command = self.formal)
        self.b4 = Button(win, text='Informal',command = self.informal)
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.b1=Button(win, text='Login', command=self.login)
        self.b1.place(x=100, y=150)
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=100)
    
    def login(self):
        global from_address 
        from_address = str(self.t1.get())
        password = str(self.t2.get())
        smtp_object.login(from_address,password)
        
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=450, y=200)
        self.b2.place(x = 100, y = 250)
        self.b3.place(x=100, y=300)
        self.b4.place(x = 200, y = 300)
        self.lbl4.place(x = 100, y = 350)
        self.t4.place(x = 200, y = 350)
        self.t5.place(x = 200, y = 400)
        
    def formal(self):
        global m
        global body
        m = "Dear, " + name + ","+ "\n" +body +"\n"+"Regards,"+"\n"+your_name
    
    def informal(self):
        m = "Hello, " + name + ","+ "\n" +body +"\n"+"Thanks,"+"\n"+your_name
    def sendEmail(self):
        subject = self.t4.get()
        m = slef.t5.get()
        msg = 'Subject: '+subject+'\n'+ m
        smtp_object.sendmail(from_address,to_address,msg)
        
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
