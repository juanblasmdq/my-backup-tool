### Use Tkinter for python 2, tkinter for python 3
import tkinter as tk

class MasterWindow():
    def __init__(self, master,masterTitle,masterLabel,masterEntry):
        self.mTitle= masterTitle
        self.mLabel = masterLabel
        self.mEntry = masterEntry
        
        self.master = master
        self.master.geometry('600x300')
        self.master.title(self.mTitle)
        
        self.frame = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        
        '''self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack(side=tk.TOP,anchor=tk.NW)'''

        self.label1 = tk.Label(self.frame, text = self.mLabel)
        #self.label1.grid(row=0, column=0, columnspan=100, padx=10, pady=10, sticky=tk.W)
        self.label1.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)

        self.entry1 = tk.Entry(self.frame,width=50) #,textvariable=self.mEntry
        #self.entry1.grid(row=0, column=2, columnspan=100, padx=10, pady=10, sticky=tk.W)
        self.entry1.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        self.entry1.insert(0,self.mEntry)
        
        self.frame.pack(side=tk.LEFT, padx=30, pady=30, expand=True, fill=tk.BOTH)
        
    '''def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title('Inner window')
        self.newWindow.geometry('600x300')
        self.app = Demo2(self.newWindow)'''

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def ShowForm(title,prompt,defaultValue):
    root = tk.Tk()
    app = MasterWindow(root,title,prompt,defaultValue)
    root.mainloop()

if __name__ == '__main__':
    tit = 'Master window title'
    lab = 'My label'
    defv = 'Default text value'
    ShowForm(tit,lab,defv)
