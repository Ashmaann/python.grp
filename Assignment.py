#tkinter to create GUI
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#=========================================
#class declaration
#==========================================
class Window(Frame):
  def __init__(self, master=None):
      Frame.__init__(self,master)
      self.master=master
      self.init_windowa()
#==========================================
#function to call the main form
#==========================================
  def init_windowa(self):
      self.master.title("Tool Owner Home Page")
      self.pack(fill=BOTH, expand=1)
      menu = Menu(self.master)
      self.master.config(menu=menu)
      file = Menu(menu)
      file.add_command(label="View Profile",command=self.ViewProfiel) 
      file.add_command(label="View Last Invoice",command=self.ViewLastInvoice)
      file.add_command(label="View Booked Tools",command=self.ViewBookedTools)
      file.add_command(label="Add New Tool",command=self.AddNewTool)
      file.add_command(label="Log Out", command=self.client_exit)

      menu.add_cascade(label="File", menu=file)
      menu.add_cascade(label="Login", menu=file)
      menu.add_cascade(label="Register", menu=file)
      menu.add_cascade(label="Edit", menu=file)
      menu.add_cascade(label="Basket", menu=file)
      menu.add_cascade(label="Help", menu=file)
      edit = Menu(menu)
#=============================================
# Buttons Call functions
#=============================================
  def ViewProfiel(self):
      root2= Toplevel(self.master)
      myGUI = ProfileViewForm(root2)

  def ViewLastInvoice(self):
      root2= Toplevel(self.master)
      myGUI = ViewLastInvForm(root2)

  def ViewBookedTools(self):
      root2= Toplevel(self.master)
      myGUI = ViewBookedToolsForm(root2)

  def AddNewTool(self):
      root2= Toplevel(self.master)
      myGUI = AddNewToolForm(root2)

 
  def client_exit(self):
        exit()   

#=================================================
#View Profile Form
# ================================================

class ProfileViewForm():
   def __init__(self, window):

         self.window = window
         window.geometry('600x480') 
         window.config(bg='lightgray')  
         lbl = Label(window,text='View Profile',bg = 'lightgray',fg="black", relief=GROOVE, font= (None, 12),)
         lbl.place(x=250,y =10)
         listB = Listbox(window, width =50, height= 17, bg= 'white')
         #listB.bind('<<ListboxSelect>>',CurSelect)
         listB.place(x = 80,y =100)

         #btn use to insret a button
         btn=Button(window, text='Edit details', bg='gray')
         btn.place(x=60,y=430)

         btn=Button(window, text='Delete profiles', bg='gray')
         btn.place(x=180,y=430)

         btn=Button(window, text='Back', bg='gray',command=self.close)
         btn.place(x=500,y=430)

         #close is use to exit a program
   def close(self):
      self.window.destroy()
          

#===================================================
#View Last Invoice Form
#===================================================
        
class ViewLastInvForm():
   def __init__(self, window):

         self.window = window
         window.geometry('600x480') 
         window.config(bg='lightgray')  
         lbl = Label(window,text='View Last Invoice',bg = 'lightgray',fg="black", relief=GROOVE, font= (None, 12),)
         lbl.place(x=250,y =10)
         listB = Listbox(window, width =50, height= 17, bg= 'white')
         #listB.bind('<<ListboxSelect>>',CurSelect)
         listB.place(x = 80,y =100)

         #btn use to insret a button
         btn=Button(window, text='Print', bg='gray')
         btn.place(x=60,y=430)

         btn=Button(window, text='Download PDF', bg='gray')
         btn.place(x=180,y=430)

         btn=Button(window, text='Back', bg='gray',command=self.close)
         btn.place(x=500,y=430)

         #close is use to exit a program
   def close(self):
      self.window.destroy()

#===================================================
#View Booked Tools Form
#===================================================
        
class ViewBookedToolsForm():
   def __init__(self, window):

         self.window = window
         window.geometry('600x480') 
         window.config(bg='lightgray')  
         lbl = Label(window,text='View Booked Tools',bg = 'lightgray',fg="black", relief=GROOVE, font= (None, 12),)
         lbl.place(x=250,y =10)
         listB = Listbox(window, width =50, height= 17, bg= 'white')
         #listB.bind('<<ListboxSelect>>',CurSelect)
         listB.place(x = 80,y =100)

         #btn use to insret a button
         btn=Button(window, text='Display', bg='gray')
         btn.place(x=60,y=430)

         btn=Button(window, text='Report lost tool', bg='gray')
         btn.place(x=180,y=430)

         btn=Button(window, text='Back', bg='gray',command=self.close)
         btn.place(x=500,y=430)

         #close is use to exit a program
   def close(self):
      self.window.destroy()

#===================================================
#Add New Tool Form
#===================================================

class AddNewToolForm():
   def __init__(self, window):
         self.window = window
         window.geometry('600x480') 
         window.config(bg='lightgray')  
         lbl = Label(window,text='Add New Tool',bg = 'lightgray',fg="black", relief=GROOVE, font= (None, 12),)
         lbl.place(x=250,y =10)
         listB = Listbox(window, width =50, height= 17, bg= 'white')
         #listB.bind('<<ListboxSelect>>',CurSelect)
         listB.place(x = 80,y =100)

         #btn use to insret a button
         btn=Button(window, text='Submit', bg='gray')
         btn.place(x=60,y=430)

         btn=Button(window, text='Cancel', bg='gray')
         btn.place(x=180,y=430)

         btn=Button(window, text='Back', bg='gray',command=self.close)
         btn.place(x=500,y=430)



         #close is use to exit a program
   def close(self):
      self.window.destroy()

root = Tk()
root.geometry("800x450")
app = Window(root)
root.mainloop()
