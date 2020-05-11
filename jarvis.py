import webbrowser
import hashlib,binascii
import os
import datetime
import calendar
import time
from time import sleep
import sys
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
from tqdm import tqdm, trange
import requests
import socket
#import crypto
import base64
#from jarvis_updater import openfile, closefile
import random
import profile
from pynput.keyboard import *
import pyautogui as pg
#from shh import hash_password, hash_reader
try:
    import FRIDAY
except:
    pass


update_date = datetime.date(2019, 12, 13)
jb_yea = datetime.date(1953, 12, 7)
yar = datetime.date.today()
db_year = 6
jb_year = 1953
lk_year = 1988
rk_year = 2010
md_year = 2006
tw_year = 2007
userlist = []
password = '2468', 'unicorn37', '8642', '1006', 'gogo1234',
username = 'logan_andrew2', 'unicornwonder37', 'lck1988', 'gmaof9', 'masontha_beast21',
m7=open('jaruserlog.txt', 'a')
m8=open('jaruserkey.txt', 'a')
m9=open('jarusername.txt', 'a')
m10=open('jarname.txt', 'a')
os.system('clear')
print('________________________________________________________________jarvis___________________________________________________________________________')
print('')
print('')

if yar >=datetime.date(2020, 5, 30):
    print("<{jarvis needs to update}>")
    print('')
    eb5=input('this may take a wile do not trun off your computer: <{y = contenu}> ')
    if eb5 =='y':
        try:
            yt = 'FRIDAY086775'
            host_ip = ('127.0.1.1')
            print('conecting to jarvis.server''\n')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((yt, 8080))
            print('conected to jarvis_server''\n')
            full_msg = ''
            while True:
                msg = s.recv(9999)
        
                if len(msg) <= 0:
                    break
                full_msg += msg.decode("utf-8")
                break

            print(full_msg)
            print('jarvis will reset in 30 seconts''\n')
            time.sleep(10)
            print('you can use jarvis in 2 min')
            time.sleep(20)
        except:
            time.sleep(15)
            keyboard = Controller()
            
            #pg.hotkey('winleft')
            #keyboard.type('cmd')
            #pg.hotkey('enter')
            #time.sleep(3)

            keyboard.type('')
            pg.hotkey('enter')
            
            #keyboard.type('ssh pi@FRIDAY086775')
            #pg.hotkey('enter')
            #time.sleep(10)
            keyboard.type('ssh pi@FRIDAY086775')
            pg.hotkey('enter')
            time.sleep(10)
            keyboard.type('gogo1234')
            pg.hotkey('enter')
            time.sleep(10)
            keyboard.type('cd Desktop')
            pg.hotkey('enter')
            keyboard.type('cd server.80648')
            pg.hotkey('enter')
            keyboard.type('python3 jarvis.server.py')
            pg.hotkey('enter')



            yt = 'FRIDAY086775'
            host_ip = ('127.0.1.1')
            print('conecting to jarvis.server''\n')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((yt, 8080))
            print('conected to jarvis_server''\n')
            full_msg = ''
            while True:
                msg = s.recv(9999)
        
                if len(msg) <= 0:
                    break
                full_msg += msg.decode("utf-8")
                break

            print(full_msg)
            print('jarvis will reset in 30 seconts''\n')
            time.sleep(10)
            print('you can use jarvis in 2 min')
            time.sleep(20)
        os.system('clear')
        quit()


#if yar.day < logs:
while True:
    u8=input('do you want to login or register? ')
    if u8 =='login':
        break
    if u8 =='register':
        break
print('  ')

if u8 =='login':
    while True:
        username_entry1=input('what is your username? ')
        print("")
        password_entry1=input('what is your password? ')
        value2 = password_entry1
        value = username_entry1
        hash_obj = hashlib.pbkdf2_hmac('sha256', bytes(value2, 'utf-8'), b's', 500000)
        value1 = binascii.hexlify(hash_obj)
        e2 = value
        access1 = 'mr.stark'
        access_1 = b'd6fa389651a955d30baf5576f1a2b44a0f96aee36a24fdf93e735fd133b31d06'
        access2 = 'unicornwonder37'
        access_2 = b'a32b7edb530738f4d3b69908172a027878399380602faa3d4ffacd376f610c64'
        access3 = 'lck1988'
        access_3 = b'0babc9db21bec8d3331f82eeedfde65488048648d6c37036fe17b2cb78f37711'
        access4 = 'gmaof9'
        access_4 = b'bdfae0f96f6a2997dcd480c9e839b9154f981a85b029233fd89395ee6bf65ea5'
        access5 = 'don75'
        access_5 = b'ced81d77c5b6b9188acfc9872a0c96798b3bded640516c4a58ae90a3028eb30c'
        access6 = 'mason_thabeast21'
        access_6 = b'0f48bdf360ab1d3410e72eb26bd7cf528f48285d87da09c90e664e13652c0c49'
        access8 = 'tim'

        if value1 == access_1:
            if value == access1:
                break
        if value1 == access_2:
            if value == access2:
                break
        if value1 == access_3:
            if value == access3:
                break
        if value1 == access_4:
            if value == access4:
                break
        if value1 == access_5:
            if value == access5:
                break
        if value1 == access_6:
            if value == access6:
                break
        else:
            attempts = 0 + 1
            if attempts == 5:
                quit()
            print("incorect")
            print('')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - attempts))
        
uselist = 'mr.stark', 'unicornwonder37', 'lck1988', 'gmaof9', 'mason_thabeast21', 
if u8 =='register':
    u3=input('enter your name ') 
    m10.write('u3'+'\n')
    print('  ')

if u8 =='register':
    while True:
        u1=input('create a passkey ')
        if len(u1) < 4:
            print('!!to short!!')
        if len(u1) > 3:
            print('  ')
            break


if u8 =='register':
    while True:
        f67="true"
        u2=input('create a username ')
        if u2 in uselist:
            f67="false"
            print('that username has been taken!!')
            print('  ')
        if f67 =="true":
            if len(u2) < 4:
                print('!!to short!!')
            elif len(u2) > 3:
                print('  ')
                break



print("     ")


if u8 =='login':
    pslogs = open('login_logs.txt', 'w')
    pslogs.write(value + ' ' + str(yar.day))
    pslogs.close
    m7.write(value)
    m7.close()



os.system("clear")
print('________________________________________________________________jarvis___________________________________________________________________________')
print('')
print('')
if u8 =='login':
    print('login was successful!')
if u8 =='register':
    print('your registration was successful!')
print('')
print("")
if u8 =='login':
    print('wellcome back ' + value + '!!!!')
if u8 =='register':
    print('helo to you new user ',u2)

if u8 =='login':
    print('how may i help you today? ',value)
if u8 =='register':
    print('how may i help you today? ',u2)




while True:
    v=input('  ')
    if v =='hello':
        print("whats up")
    elif v =='hi how are you today?':
        print('good. how are you? ')
    elif v =="i'm good today!":
        print('nice')
    elif v =="what's your favorite food?":
          print('pizza maccoroni and cookies! ')
    elif v =='how do you blink?':
        print("When you blink, your eyelids use suction to pull fluid from your tear ducts and spread it over your eyeballs. If you've ever had something in your eyes, you know it can be a very painful and irritating experience. Blinking also helps protect your eyes from foreign objects such as dust, dirt and sand")
    elif v =='can you even eat food?':
        print('no im a computer program. but if we wanted to use our imagintion yes!!')
    elif v =='calculator':
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        
        print("slect operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multply")
        print("4. Divide")
        print("5. exit calculator")
        while True:
            choice = input('Enter choice(1/2/3/4/5: ')
            print('')
            if choice =='5':
                exit_cal = input('are you sure you want to exit calculator[Y/N] ')
                if exit_cal =='Y':
                    break
                if exit_cal =='y':
                    break
                if exit_cal =='YES':
                    break
                if exit_cal =='yes':
                    break
                if exit_cal =='yEs':
                    break
                if exit_cal =='yES':
                    break
                if exit_cal =='yeS':
                    break
                if exit_cal =='YeS':
                    break
                if exit_cal =='YEs':
                    break
                if exit_cal =='Yes':
                    break
            num1 = float(input("Enter First Number: "))
            print('')
            num2 = float(input("Enter Second Number: "))
            print('')
            if choice =='1':
                print(num1, "+", num2, "=", add(num1,num2))
            elif choice =='2':
                print(num1, "-", num2, "=", subtract(num1,num2))
            elif choice =='3':
                print(num1, "*", num2, "=", multiply(num1,num2))
            elif choice =='4':
                print(num1, "/", num2, "=", divide(num1,num2))
            elif choice =='5':
                exit_cal = input('are you sure you want to exit calculator[Y/N] ')
                if exit_cal =='Y':
                    break
                if exit_cal =='y':
                    break
                if exit_cal =='YES':
                    break
                if exit_cal =='yes':
                    break
                if exit_cal =='yEs':
                    break
                if exit_cal =='yES':
                    break
                if exit_cal =='yeS':
                    break
                if exit_cal =='YeS':
                    break
                if exit_cal =='YEs':
                    break
                if exit_cal =='Yes':
                    break
                
        
            else:
                print("invalid input")
    elif v =='who is your crator?':
        print('    <Trenton,c Waters>      ')
        print('  he crated me  10/8/2019.  ')
        print(' for his frst time codeing. ')
    elif v =='what are you?':
        print('im a ai asstistant to help you day/night')
    elif v =='what is your favorite number?':
        print('                     binary!!!                         ')
        print('1010100100101001011001010100101001010010101101001101010')
    elif v =='jarvis shutdown':
        f5=input('ok are you sure [Y/N] ')
        if f5 =='y':
            break
    elif v =='how to make cinnamon toast?':
        print('1.Butter a slice of bread.')
        print('')
        print('2.Combine sugar and cinnamon in a bowl…')
        print('')
        print('3.Stir it to combine.')
        print('')
        print('4.Sprinkle the cinnamon/sugar mixture on top of the butter, then pop it in the oven: 10 minutes at 350, then finish it off under the broiler (I’ll give you my reasons for this method later.)')
    elif v =='give me the ipad':
        print('ummmm, no.')
    elif v =='what is your favorite animal?':
        print('turtles cats and hedgehogs')
    elif v =='about':
        print('name <jarvis>')
        print('')
        print('version  <jos 3.2.5>')
        print('')
        print('url <6>')
        print('')
        print('users <5>')
        if u8 =='login':
            print('current user ',value)
        if u8 =='register':
            print('current user',u2)
    elif v =='what is my name?':
        if u8 == 'login':
            if e2 == 'gmaof9':
                print('Jan Bright')
            if e2 =='logan_andrew2':
                print('  Trenton c waters')
                print(' you are my crator')
            if e2 =='lck1988':
                print('lauren c kunkel')
            if e2 =='unicornwonder37':
                print('Raegan e kunkel')
        if u8 =='register':
            print(u3)
    elif v =='webbrowser':
        c=input("where do you want to go? ")
        print("   ")
        print('ok i will send you to',c)
        t=input("[y/n] ")
        if t =='y':
            while True:
                if c =='youtube':
                    new=2; url='https://www.youtube.com'; webbrowser.open(url,new=new);
                if c =='youtube':
                    break
                if c =='google':
                    new=2; url='https://www.google.com'; webbrowser.open(url,new=new);
                if c =='google':
                    break
                if c =='amazon':
                    new=2; url='https://www.amazon.com'; webbrowser.open(url,new=new);
                if c =='amazon':
                    break
                if c =='pioneer woman':
                    new=2; url='https://www.thepioneerwoman.com'; webbrowser.open(url,new=new);
                if c =='pioneer woman':
                    break
                if c =='pizza hut':
                    new=2; url='https://www.pizzahut.com'; webbrowser.open(url,new=new);
                if c =='pizza hut':
                    break
                if c =='dominos':
                    new=2; url='https://www.dominos.com'; webbrowser.open(url,new=new);
                if c =='dominos':
                    break
    elif v =='how to make crescent roll pizza?':
        print('1.open two cans of crescent rolls, and make a circle')
        print('')
        print('2.take two tbs of butter in a bowl <heat till melted> then put garlic powder and garlic salt in butter, and brush on creccent roll dough')
        print('')
        print('3.rool up eges of circle <for stuffed crust put cheese sticks in crust>, then put itallion seasoning on crust, then cover inside with pizza sauce, then cover sauce with pizza and itallion cheese')
        print('')
        print('4.put in 375`oven <350` for dark or greesy pan> for 16/25 minutes')
        print(' ')
        print('enjoy!!!')
    elif v =='how old am i?':
        if u8 == 'login':
            if e2 == 'gmaof9':
                if datetime.date.today() ==datetime.date(2019, 11, 5):
                    age = 2019 - jb_year
                    print('you are ' + str(age) + ' years old!!!')
                elif datetime.date.today() > datetime.date(2019, 12, 7):
                    if datetime.date.today() ==datetime.date(2020, 12, 7):
                        age =2020 - jb_year
                        print('you are ' + str(age) + + ' years old!!!')
                    if datetime.date.today() > datetime.date(2019, 12, 7):
                        age2 = 2019 - jb_year
                        print('you are ' + str(age2) + ' years old!!!')
                else:
                    age = 2018 - jb_year
                    print('you are ' + str(age) + ' years old!!!')
            if e2 == 'lck1988':
                    age = 2019 - lk_year
                    print('you are ' + str(age) + ' years old!!!')
            if e2 == 'logan_andrew2':
                    age = 2019 - tw_year
                    print('you are ' + str(age) + ' years old!!!')
            if e2 == 'unicornwonder37':
                    age = 2019 - rk_year
                    print('you are ' + str(age) + ' years old!!!')
            if e2 == 'masontha_beast21':
                age = int(yar.year) - md_year
                print('you are ' + str(age) + ' years old!!!')
    elif v =='what is today`s date?':
        today = datetime.date.today()
        print('today`s date is ' + str(today))
    elif v =='what is the time?':
        time_string = time.strftime("%H:%M:%S")
        print(time_string)
    elif v =='calendar':
        print(calendar.calendar(yar.year))
    elif v =="poop":
        print('fart')
    elif v =='this months calendar':
        print(calendar.month(yar.year, yar.month))
    elif v =='jarvis check for updates':
        progresbar = tqdm([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100])
        for item in progresbar:
            sleep(0.5)
        progresbar.set_description('processing element'.format(item))
        for i in tqdm(range(100)):
            sleep(0.1)
        print("jarvis is up to date")
    elif v =='go away':
        print('ok! good bye')
        f09=input('are you shore you want to exit [Y/N] ')
        if f09 =='Y':
            break
        if f09 =='y':
            break
        if f09 =='YES':
            break
        if f09 =='yes':
            break
        if f09 =='yEs':
            break
        if f09 =='yES':
            break
        if f09 =='yeS':
            break
        if f09 =='YeS':
            break
        if f09 =='YEs':
            break
        if f09 =='Yes':
            break
    elif v =='mixx':
        os.system('cd C:\Program Files\Mixxx')
        os.system('"C:\Program Files\Mixxx\mixxx.exe"')
        os.system('cls')
        print('________________________________________________________________jarvis___________________________________________________________________________')
        print('')
        print('jarvis had to clear becuz of a app was opened')
        print('')
    elif v =='help':
        pass
    elif v =='chat':
        pass
    elif v =='when is the next update':
        print(f'your next update is on {update_date}:')
    elif v =='music':
        pass
    elif  v =='jarvis flip a coin':
        flip=input('how meny time`s t flip the coin ')
        flip1 = int(flip)
        tails_cow = 0
        heads_cow = 0
        for i in range(flip1):
            rand = random.randint(1,2)
            if rand == 1:
                tails_cow += 1
                print(tails_cow, 'tails')
            else:
                heads_cow += 1
                print(heads_cow, 'heads')
        print('talis', tails_cow)
        print('heads', heads_cow)
    elif v =='cls':
        os.system('clear')
        print('________________________________________________________________jarvis___________________________________________________________________________')
        print('')
        print('')
        print('')
    elif v =='go v8':
        print('lets gooooooooooo!')
    elif v =='ok boomer':
        print('ummmmmmm, ok')
        os.system('clear')
        quit()
    elif v =='do you like siri?':
        print("siri is trash! XP")
    elif v =='hey siri':
        print("that's like compering gold and trash and saying their the same!")
    elif v =='i like siri more':
        print("we are not friends")
        time.sleep(60)
        os.system('clear')
        print('good bye old friend')
        time.sleep(15)
        os.system('clear')
        quit()
    elif v =='help':
        pass
    elif v =='ipconfig':
        os.system('ipconfig')
    elif v =='jarvis run prodicall F.R.I.D.A.Y':
        hgw2=input('are you sure boss [Y/N] ')
        if hgw2 =='y':
            try:
                print('ok boss')
                time.sleep(4)
                os.system('clear')
                FRIDAY.FRIDAY()
            except:
                print('sory F.R.I.D.A.Y is not working')
    else:
        print('~<{invalid input}>~')
    
    
    
    
    
    
    
    
    
    
    
######################################################

progresbar = tqdm([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100])
for item in progresbar:
    sleep(0.6)
    progresbar.set_description('processing element'.format(item))

for i in tqdm(range(100)):
    sleep(0.1)
    pass

os.system('clear')
time.sleep(2)
quit()