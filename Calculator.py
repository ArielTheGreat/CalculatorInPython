from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.master.iconbitmap('C:\\Users\\UX533\\Desktop\\calculatorInPython\\icono\\calc.ico')
        self.master.geometry("400x550")
        self.pack(fill="both",expand=True)
       # createButtons()
    #def createButtons(self):
        
window = Tk()
app = Application(window)
app.mainloop()