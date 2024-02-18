import time
from machine import Pin, PWM
from menuclass import Menu, menuItem ,getnumber, getnumber_DC
import _thread

BPM = 60
def core1_thread():
    speaker = Pin(22,Pin.OUT)
    global BPM
    while True:
        if (BPM > 5):
             speaker(1)
             time.sleep(0.001)  # pulsbredde 1 millisekund
             speaker(0)
             time.sleep(60/BPM)
        else:
            time.sleep(1)

second_thread = _thread.start_new_thread(core1_thread, ())






from LCD_1_8_file import LCD_1inch8


BL = 13

if __name__ == '__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)  # max 65535
    r = Pin(16, Pin.OUT)
    r(1)
    g = Pin(17, Pin.OUT)
    r(1)
    b = Pin(18, Pin.OUT)
    r(1)
    for n in range(8):
        if (n%2 == 0):
            r(1)
        else:
            r(0)
        if (int(n/2)%2 == 0):
            g(1)
        else:
            g(0)
        if (int(n/4)%2 == 0):
            b(1)
        else:
            b(0)
        time.sleep(0.2)



def metronom():
    global BPM
    print("metronom")
    while True:
        x = getnumber_DC(BPM)
        if  None == x:
            return  #magic stop dobbel click exit
        else:
            BPM = x



def f1():
    print("Hej fra f1")
    time.sleep(0.5)



def f2():
    print("Hej fra f2")
    time.sleep(0.5)

def setPinHi():
    n = getnumber()
    p = Pin(n,Pin.OUT)
    p(1)

def setPinLo():
    n = getnumber()
    p = Pin(n,Pin.OUT)
    p(0)

def led_test():
    while True:
        n = getnumber()
        if (n%2 == 0):
            r(1)
        else:
            r(0)
        if (int(n/2)%2 == 0):
            g(1)
        else:
            g(0)
        if (int(n/4)%2 == 0):
            b(1)
        else:
            b(0)
        if n==10: return

mp1 = menuItem("mp1-object",f1)
mp2 = menuItem("mp2-object",f2)
lt = menuItem("RGB led test",led_test)

metronometest = menuItem("Metronom v0.3",metronom)

mainmenu = Menu()
mainmenu.AddMenuItem(mp1)
mainmenu.AddMenuItem(lt)
mainmenu.AddMenuItem(metronometest)



submenu1 = Menu()
submenu1.AddMenuItem(mp1)
submenu1.AddMenuItem(mp1)
submenu1.AddMenuItem(mp2)
submenu1Item = menuItem("sub menu 1",submenu1.execute)
mainmenu.AddMenuItem(submenu1Item)


enteritem = menuItem("test of enter digit",getnumber)
setpinhiItem = menuItem('set a gp pin hi',setPinHi)
setpinloItem = menuItem('set a gp pin low',setPinLo)


submenu_gpio = Menu()
submenu_gpio.AddMenuItem(enteritem)
submenu_gpio.AddMenuItem(setpinhiItem)
submenu_gpio.AddMenuItem(setpinloItem)
submenu_gpioItem = menuItem("gpio menu",submenu_gpio.execute)
mainmenu.AddMenuItem(submenu_gpioItem)



ServoPinNumber = 0



enterservopinnr_Item = menuItem("Enter servo pinnumber",getnumber)
submenu_servo = Menu()
submenu_servo.AddMenuItem(enterservopinnr_Item)
#submenu_servo.AddMenuItem(setpinhiItem)
submenu_servoItem = menuItem("servo menu",submenu_servo.execute)
mainmenu.AddMenuItem(submenu_servoItem)



print ('mainmenu starter')

mainmenu.execute()

print ('mainmenu slutter')
