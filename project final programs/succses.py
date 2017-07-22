'''
Created on 11-Nov-2016

@author: Administrator
'''
'''
Created on 03-Nov-2016

@author: Administrator
'''

from tkinter import *
#import tkinter
#from tkinter import Menu
import tkinter.scrolledtext as tkst
#from scrolledtext import *
#from tkinter.filedialog import askopenfilename

class Example(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)   

        self.parent = window        
        self.initUI()

    def initUI(self):

        sfin=""
        self.parent.title("SONOGRAPHY ASSISTANT")
        self.parent.textPad = tkst.ScrolledText(self.parent, wrap   = 'word',  # wrap text at full words only
                            width  = 70,      # characters
                            height = 80,      # text lines
                            bg='beige'       )
        #edit_space.pack(fill='both', expand=True, padx=8, pady=8)
        self.parent.textPad.pack(fill='both', expand=True, padx=8, pady=8)
        menubar=Menu(self)
         
        patientmenu=Menu(menubar)
        patientmenu.add_command(label="new")
        patientmenu.add_command(label="open")
        patientmenu.add_command(label="save")
        patientmenu.add_command(label="preview")
        menubar.add_cascade(label="file",menu=patientmenu)
        
        helpmenu=Menu(menubar)
        helpmenu.add_command(label="help")
        helpmenu.add_command(label="about")
        menubar.add_cascade(label="help",menu=helpmenu)
        
        
        exitmenu=Menu(menubar)
        exitmenu.add_command(label="Exit")
        menubar.add_cascade(label="exit",menu=exitmenu)
        '''menubar.add_cascade(cnf)'''
        self.parent.config(menu=menubar)
        
        self.parent.textPad.insert('1.0',"welcome doc ....start speaking")
        #self.parent.mainloop()
        #self.parent.textPad.insert('7.0'," hello")
        #just ADD END VARIABLE or add number above 1.0 eg 3.0 
       
        #self.onscreen()   
       
        def after1():
           
            sfin=self.parent.textPad.get('1.0', END)
            self.parent.destroy()
            self.parent = Tk()
            self.parent.textPad = tkst.ScrolledText(self.parent, wrap   = 'word',  # wrap text at full words only
                            width  = 70,      # characters
                            height = 80,      # text lines
                            bg='beige'       )
            #while(1):
                
            self.parent.textPad.insert(END,sfin+"\nYou have done it shibbu kuchi ku")
            self.parent.textPad.pack(fill='both', expand=True, padx=8, pady=8)
            self.parent.mainloop()
            
           
            
        
        self.parent.after(1,after1)  
        self.parent.mainloop()
        
    def onscreen(self):#''',unistr'''
        n=0
        while(n!=10):
            print(n)
            self.parent.textPad.update_idletasks()
            n=n+1

def main():
    window = Tk()
    ex = Example(window)
    #window.geometry("600x600")
    
    #ex.parent.textPad.Append()(END, "shivani")
    #Main Loop
    window.mainloop()

if __name__ == '__main__':
    main() 
