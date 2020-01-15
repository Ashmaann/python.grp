from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import csv
#from Python.display import display

class Welcome():

    def __init__(self, master):

        self.master = master
        self.master.config(bg='lightblue') 
        self.master.geometry('800x490')
        self.master.title('View Booked Tools')

        btn = Button(master, text="Booked date", height='3',
                      width='65', command=self.bookeddateForm)
        btn.place(x=100, y=30)

        btn = Button(master, text="Due return date", height='3',
                      width='65', command=self.duereturndateForm)
        btn.place(x=100, y=100)

        btn = Button(master, text="Booking period", height='3',
                      width='65', command=self.bookingperiodForm)
        btn.place(x=100, y=170)

        btn = Button(master, text="Booking cost", height='3',
                      width='65', command=self.bookingcostForm)
        btn.place(x=100, y=240)

        btn = Button(master, text="Delivery/Collection", height='3',
                   width='65', command=self.deliverycollectionForm)
        btn.place(x=100, y=310)

        btn = Button(master, text="Return tool (Customer)", height='3',
                      width='30', command=self.returntoolForm)
        btn.place(x=110, y=400)

        btn = Button(master, text="Report lost tool (Customer)", height='3',
                      width='30', command=self.reportlosttoolForm)
        btn.place(x=410, y=400)

        BtnEn = Button(master, text='exit', command=self.close)
        BtnEn.place(x=720, y=460)
        
    def close(self):
        self.master.destroy()

    def bookeddateForm(self):
        root2 = Toplevel(self.master)
        myGUI = bookedForm(root2)

    def duereturndateForm(self):
        root2 = Toplevel(self.master)
        myGUI = duereturnForm(root2)

    def bookingperiodForm(self):
        root2 = Toplevel(self.master)
        myGUI = bookingpForm(root2)     

    def bookingcostForm(self):
        root2 = Toplevel(self.master)
        myGUI = bookingcForm(root2)     
     
    def deliverycollectionForm(self):
        root2 = Toplevel(self.master)
        myGUI = deliverycForm(root2)  

    def returntoolForm(self):
        root2 = Toplevel(self.master)
        myGUI = returntForm(root2)

    def reportlosttoolForm(self):
        root2 = Toplevel(self.master)
        myGUI = reportlostForm(root2)


class bookedForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Booked date',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=305,y =10)

         
         btn = Button(master, text="Time: 8:00am O,clock", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=100)

         btn = Button(master, text="Date:5/6/2019", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=170)

         btn = Button(master, text="Day - Thursday", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=250)

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()
         
class duereturnForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Due return date',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=295,y =10)

         btn = Button(master, text=" Due return date:5/6/2019", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=80)

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()      

class bookingpForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Booking period',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=295,y =10)

         btn = Button(master, text="Duration", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=80)

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()  


class bookingcForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Booking cost',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=300,y =10)

         btn = Button(master, text="cost", height='3', bg = 'white',
                      width='20')
         btn.place(x=100, y=80)

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()   

class deliverycForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x200') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='delivery and collection',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=280,y =10)

         btn = Button(master, text="delivery", height='3', bg = 'white',
                      width='20', command=self.gotoRegForm)
         btn.place(x=100, y=80)

         btn = Button(master, text="collection", height='3', bg = 'white',
                      width='20', command=self.gotoRegForm)
         btn.place(x=400, y=80)

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=170)

   def gotoRegForm(self):
        root2 = Toplevel(self.master)
        myGUI = RegForm(root2)
      

   def close(self):
       self.master.destroy()        


class returntForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Return tool',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=315,y =10) 

         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()

class reportlostForm():
   def __init__(self, master):

         self.master= master
         master.geometry('700x480') 
         master.config(bg='lightblue')  
         lbl = Label(master,text='Report lost tool',bg = 'lightgray',fg="black",  font= (None, 13),)
         lbl.place(x=295,y =10) 
         
         BtnEn = Button(master, text='Back', bg = 'white', command=self.close)
         BtnEn.place(x=600, y=450)

   def close(self):
       self.master.destroy()         

def main():
    root=Tk()
    myGUIWelcome = Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
  
