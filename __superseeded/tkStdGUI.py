'''A python script to generate a userform-type Tkinter GUI to entry up to 5 fields

Use:
1. Copy this file to the path of your project
2. Import module using 'import tkGUI'
3. Generate a list of labels (i.e., lines to be filled-in)
4. Call function 'tkGUI.ShowForm('Título de la ventana',label_list,'')' passing the required arguments
   and assign that the result to any variable of your project (shall be a list!)'''

import tkinter as tk
import random

__author__ = 'Juan Blas Carelli'
__version__ = 'July 15, 2021'

class MasterWindow():
    def __init__(self, master,masterTitle,masterLabel,masterEntry):
        '''Constants'''
        self.mTitle= masterTitle
        self.mLabel = masterLabel
        self.mEntry = masterEntry
        self.item = 1
        self.xposLabel = 10
        self.yposLabel = 10
        self.xposText = 200
        self.yposText = 10
        self.labels = []
        self.texts = []
        self.mOutput = []

        def calculate_it_position(self,item):
            ROW_SPACE = 100
            if item == 0:
                # self.xposLabel = 10
                # self.yposLabel = self.xposLabel
                # self.xposText = 200
                # self.yposText = self.yposLabel
                pass
            else:
                self.xposLabel = self.xposLabel
                self.yposLabel = self.yposLabel + ROW_SPACE
                self.xposText = self.xposText
                self.yposText = self.yposText +  ROW_SPACE

        '''Geometry, title and frame'''
        self.master = master
        self.master.geometry('600x600')
        self.master.title(self.mTitle)
        self.frame = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        '''Automatic item creation'''
        #Labels and text boxes
        i=0
        for it in self.mLabel:
            calculate_it_position(self,i)
            self.labels.append(tk.Label(self.frame,text=it))
            self.labels[i].place(x=self.xposLabel,y=self.yposLabel)
            self.texts.append(tk.Text(self.frame,width=47, height=4))
            self.texts[i].place(x=self.xposText,y=self.yposText)
            i=i+1

        self.buttonOK = tk.Button(self.frame, text = 'Ok', width = 15, command = self.buttonOK_press)
        self.buttonOK.place(x=400,y=500)

        '''
        ###Labels
        self.label1 = tk.Label(self.frame, text = self.mLabel)
        self.label1.place(x=10,y=10)
        # self.label1.grid(row=0, column=0, columnspan=100, padx=10, pady=10, sticky=tk.W)
        # self.label1.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        ###Entry boxes
        # self.entry1 = tk.Entry(self.frame,width=50) #,textvariable=self.mEntry
        # self.entry1.grid(row=0, column=2, columnspan=100, padx=10, pady=10, sticky=tk.W)
        # self.entry1.insert(0,self.mEntry)
        # self.entry1.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        ###Text boxes
        self.text1 = tk.Text(self.frame,width=47, height=4)
        self.text1.insert(tk.END,self.mEntry)
       # self.text1.configure(font=(tk.fonts.DefaultFont)) #'lucida 10'))
        # self.text1.configure(font=("Courier", 16, "italic"))
        self.text1.place(x=200,y=10) # x = 0 + 20 (frame padx) + 10 (label1 x) + 110 (label1 reserved space) + 10 (space) =  200
        ###Buttons
        # self.button1 = tk.Button(self.frame, text = 'Ok', width = 15, command = self.get_entry_data)
        # self.button1.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.SW)
        self.button2 = tk.Button(self.frame, text = 'Ok', width = 15, command = self.get_text_data)
        self.button2.place(x=400,y=200)
        '''

        '''Frame packing'''
        self.frame.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH)
        
    ''' New window function. Not used
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Inner window')
        self.newWindow.geometry('600x300')
        self.app = Demo2(self.newWindow)'''
    
    ''' Get entry function. Not used
    def get_entry_data(self):
        self.mOutput = self.entry1.get()
        self.master.destroy()'''

    def buttonOK_press(self):
        i=0
        for it in self.mLabel:
            self.mOutput.append(self.texts[i].get("1.0",tk.END).strip('\n'))
            i=i+1
        
        self.master.destroy()

class LogWindow():
    def __init__(self,master,content):
        '''Constants'''
        self.logTitle= 'LOG'
        self.logContent = content
        self.master = master
        '''Geometry, title and frame'''
        #self.master = tk.Tk()
        self.master.geometry('600x600')
        self.master.title(self.logTitle)
        self.frame = tk.Frame(self.master)
        
        self.text1 = tk.Text(self.frame,width=75, height=32)
        self.text1.place(x=10,y=10)
        self.text1.insert(tk.END,self.logContent)
        self.frame.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH)

        self.master.option_add("*Font", "lucida 10") #Change font used for all widgets
        #self.master.after(2000,self.update_log)
        #self.master.mainloop()

    # def update_log(self):
    #     self.text1.delete("1.0", tk.END)
    #     self.text1.insert(tk.END,self.logContent)
    #     self.text1.update()
    #     #self.master.after(2000,self.update_log)

    # def setLogValue(self,tx):
    #     self.logContent = tx

        # while True:
        #     self.root.update_idletasks()
        #     self.root.update()
        #DANGER

    # def write_to_log(self,logContent):
    #     self.text1.delete("1.0", tk.END)
    #     self.text1.insert(tk.END,logContent)
    #     self.text1.update()

'''Ahother class for inner windows. Not used
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()'''

def ShowForm(title,prompt,defaultValue):
    root = tk.Tk()
    root.option_add("*Font", "lucida 10") #Change font used for all widgets
    # root.option_add("*Label.Font", "lucida 10")
    # root.option_add("*Entry.Font", "lucida 10")
    # root.option_add("*Text.Font", "lucida 10")
    # root.option_add("*Button.Font", "lucida 10")

    app = MasterWindow(root,title,prompt,defaultValue)
    root.mainloop()
    return app.mOutput

def ShowLog(content):
    root = tk.Tk()
    root.option_add("*Font", "lucida 10") #Change font used for all widgets
    app = LogWindow(root,content)
    root.mainloop()

if __name__ == '__main__':
    pass
    #label_list = ['Label1','Label2','Label3','Label4','Label5']
    #print(ShowForm('Título de la ventana',label_list,'sssss'))
    #logContent = 'Contenido del log \nlinea 2'
    #log = ShowLog('LOG',logContent)
    #log.write_to_log('gg')
