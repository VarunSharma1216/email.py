import smtplib
from tkinter import *
root = Tk()
root.title("email")
root.geometry("400x400")
root.mainloop()
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
import getpass
def login:
    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')
    smtp_object.login(email,password)
from_address = email
to_address = input("Enter the emails of whoever you want to send it to: ").split()
def send_email():
    subject = input('Enter the subject line: ')
    name = input("Who are you sending the email to: ")
    body = input("What is the message you want to send: " )
    your_name = input("Enter your full name: ")
    message = "Hello " + name+ ","+ "\n" +body +"\n"+"Thanks,"+"\n"+your_name
    msg = 'Subject: '+subject+'\n'+message
    smtp_object.sendmail(from_address,to_address,msg)
send_email()
