from machine import Pin
import time

from LCD_1_8_file import LCD_1inch8

import UI

LCD = LCD_1inch8()
LCD.fill(LCD.WHITE)
LCD.show()


class Menu():
    def __init__(self):
        self.selected_item_index = 0
        self.menuItemList=[]
        self.back_item = menuItem('Back',None)
        self.menuItemList.append(self.back_item)



    def show(self):
        y=5
        for obj in self.menuItemList:
            LCD.text(obj.ItemLine, 2, y, LCD.BLACK)
#            print(obj.ItemLine)
            y = y + 20
        LCD.show()
    def highlight(self):
        LCD.fill(LCD.WHITE)
        self.show()
        LCD.rect(1, 3+(self.selected_item_index)*20, 150, 20, 0X0000)
        LCD.show()

    def AddMenuItem(self, MI):
        self.menuItemList.insert(-1,MI)

    def up(self):
        self.selected_item_index = (self.selected_item_index + 1)%len(self.menuItemList)
        self.highlight()

    def down(self):
        self.selected_item_index = (self.selected_item_index - 1)
        if (self.selected_item_index < 0):
            self.selected_item_index = len(self.menuItemList) -1
        self.highlight()

    def select(self):
         self.menuItemList[self.selected_item_index].execute()

    def execute(self):
        self.highlight()
        while True:
            [u, d, s] = UI.UserInput()
            #print([u,d,s])
            if u:
                self.up()
            if d:
                self.down()
            if s:
                if self.menuItemList[self.selected_item_index].function != None:
                    self.select()
                    self.highlight()
                else:
                    return



class menuItem():
    def __init__(self,line,f):
        self.ItemLine = line
        self.function = f

    def execute(self):
        self.function()



def getnumber(start=None):
    if not start:
        n = 0
    else:
        n=start
    #clear display
    # vis n
    LCD.fill(LCD.WHITE)
#    LCD.text(info, 30, 30, LCD.BLACK)  hjælpetext ønsket.. fex  "indtast skonummer"
    LCD.text(str(n), 60, 60, LCD.BLACK)
    LCD.show()
    while True:
        [u, d, s] = UI.UserInput()
        #print([u, d, s])
        if u:
            n = n + 1
            #vis n
            LCD.fill(LCD.WHITE)
            LCD.text(str(n), 60, 60, LCD.BLACK)
            LCD.show()
        if d:
            n = n - 1
            #vis n
            LCD.fill(LCD.WHITE)
            LCD.text(str(n), 60, 60, LCD.BLACK)
            LCD.show()
        if s:
            print(n)
            return n


def getnumber_DC(start=None):
    if not start:
        n = 0
    else:
        n=start
    x = getnumber(n)
    t1= time.time()
    UI.select_released()
    while True:
        if UI.Select_active():
            time.sleep(0.02)
            return None
        if time.time() > (t1 + 1):
            return x
