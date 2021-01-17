import smtplib
from tkinter import *
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
class MyWindow:
        def __init__(self, win):
                self.lbl1=Label(win, text='email')
                self.lbl2=Label(win, text='Second number')
                self.t1=Entry(bd=3)
                self.t2=Entry()
                self.btn1 = Button(win, text='login')
                self.btn2=Button(win, text='Subtract')
                self.lbl1.place(x=100, y=50)
                self.t1.place(x=200, y=50)
                self.lbl2.place(x=100, y=100)
                self.t2.place(x=200, y=100)
                self.b1=Button(win, text='login', command=self.login)
                self.b2=Button(win, text='Subtract')
                self.b2.bind('<Button-1>', self.sub)
                self.b1.place(x=100, y=150)
                self.b2.place(x=200, y=150)
        def login(self):
                email = getpass.getpass('Email: ')
                password = getpass.getpass('Password: ')
                smtp_object.login(email,password)
                from_address = email
                to_address = input("Enter the emails of whoever you want to send it to: ").split()
        def send_email(self):
                subject = input('Enter the subject line: ')
                name = input("Who are you sending the email to: ")
                body = input("What is the message you want to send: " )
                your_name = input("Enter your full name: ")
                message = "Hello " + name+ ","+ "\n" +body +"\n"+"Thanks,"+"\n"+your_name
                msg = 'Subject: '+subject+'\n'+message
                smtp_object.sendmail(from_address,to_address,msg)
send_email()
root = Tk()
root.title("email")
root.geometry("400x400")
root.mainloop()
