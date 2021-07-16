'''A python script to generate a GUI for Python project my-backup-tool

Note: This script is part of Python project my-backup-tool
Full code: https://github.com/juanblasmdq/my-backup-tool/'''

import tkinter as tk
from tkinter import font
from tkinter import messagebox

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        def UnderlinedWidget(self,widget):
            f = font.Font(widget, widget.cget("font"))
            f.configure(underline=True)
            widget.configure(font=f)
            return widget
            pass

        #Parent frame and wrapper
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent
        self._bgcolor = self._parent['bg'] # SystemButtonFace
        self._parent.geometry('800x600')
        self._parent.title('My backup tool')
        self.wrapper = tk.Frame(self._parent, highlightbackground="black", highlightthickness=1)
        self.wrapper.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill=tk.BOTH)
        
        #Text 'labels' and Text 'boxes'
        colwidth = 39
        colspan =2
        self.text1Q = tk.Text(self.wrapper,width=colwidth, height=2) # 1Q = First question
        self.text1Q.grid(row=0, column=0, columnspan = colspan, padx = 30, pady=(30,0))
        self.text1Q['bg'] = self._bgcolor
        self.text1Q['borderwidth']=0
        self.text1Q.insert('1.0', 'BACKUP PATH:\n(destination for the zip):')
        self.text1Q.bind("<Button-1>", lambda e: "break")

        self.text1A = tk.Text(self.wrapper,width=colwidth, height=4) #1A = First Answer
        self.text1A.grid(row=1, column=0, columnspan = colspan)

        self.text2Q = tk.Text(self.wrapper,width=colwidth, height=2) # 2Q = First question
        self.text2Q.grid(row=2, column=0, columnspan = colspan, padx = 30, pady=(30,0))
        self.text2Q['bg'] = self._bgcolor
        self.text2Q['borderwidth']=0
        self.text2Q.insert('1.0', 'FILES PATH:\n(origin of the files to secure):')
        self.text2Q.bind("<Button-1>", lambda e: "break")

        self.text2A = tk.Text(self.wrapper,width=colwidth, height=17) #2A = First Answer
        self.text2A.grid(row=3, column=0, columnspan = colspan)

        #Text LOG
        self.textLogL = tk.Text(self.wrapper,width=colwidth, height=2) # LogL = Label for LOG
        self.textLogL.grid(row=0, column=3, columnspan = colspan, padx = 30, pady=(30,0))
        self.textLogL.tag_configure('tag-center', justify='center')
        self.textLogL['bg'] = self._bgcolor
        self.textLogL['borderwidth']=0
        self.textLogL.insert('end', ' '*10 + 'LOG' +' '*10, 'tag-center')
        UnderlinedWidget(self,self.textLogL)
        self.textLogL.bind("<Button-1>", lambda e: "break")
        
        self.textLogO = tk.Text(self.wrapper,width=colwidth, height=25) #LogO = First Answer
        self.textLogO['bg'] = 'azure'
        self.textLogO.grid(row=1, column=3, columnspan = colspan, rowspan=3)

        #Buttons

        self.buttonGetConfig = tk.Button(self.wrapper, text = 'Get config paths', width = 15, command = self.getConfig) # Do not include () after function name!!!!! 
        self.buttonGetConfig.grid(row=4, column=0, pady=30)                                                             # Function gets invoked when loading if () are added

        self.buttonGetDefaults = tk.Button(self.wrapper, text = 'Get default paths', width = 15, command = self.getDefault)
        self.buttonGetDefaults.grid(row=4, column=1, pady=30)

        self.buttonOK = tk.Button(self.wrapper, text = 'Generate backup', width = 15, command = self.getEntiedPaths)
        self.buttonOK.grid(row=4, column=3, columnspan=colspan, pady=30)

    def getConfig(self):
        '''Development pending'''
        #text = text.get('1.0', 'end')
        pass
    def getDefault(self):
        '''Development pending'''
        #text = text.get('1.0', 'end')
        pass
    def getEntiedPaths(self):
        '''Development pending'''
        print(messagebox.askyesno('Are you sure?','Continue and run?',icon='warning')) #Returns True / False

        #Other messagebox types:
        # .showinfo
        # .showwarning
        # .showerror
        # .askquestion
        # .askokcancel
        # .askyesno
        # .askretrycancel

        # Other icons possible:
        # icons= "error"
        # icons= "info"
        # icons= "question"
        # icons= "warning"
        
        #text = text.get('1.0', 'end')
        pass


    def updateLog(self):
        '''Development pending'''
        pass


def AppRun():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    AppRun()