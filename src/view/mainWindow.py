import tkinter as tk 

import sys

from control.copyListener import copyBut
from control.enterListener import enter
from control.menuListener import *

class mainWindow:
    """
    The class which represent the main window of the application

    Attributes:
    -----------
    window : tK
        The window of the application
    textField : Entry
        A text field (read-only) where the password will be written
    copyBut : Button
        A button for copy the password 
    txt : StringVar
        A string that can be modified.
    slider : Scale
        A slider to choose the length of the password
    checkBoxLett : CheckButton
        A checkbox to choose if the letters of the string will be a-z and A-Z
    checkBoxNumb : CheckButton
            A checkbox to choose if in the string will be the numbers
    checkBoxSpecial : CheckButton
            A checkbox to choose if in the string will be special symbols
    enterBut : Button
        A button for generate the password
    menuBar : Menu
        The menu of the application
    fileMenu : Menu
        The choices for the menu


    

    Methods:
    --------
    getWindow():
        Return the window of the application
    setTextField(tex):
        Modify the value of Entry() with the string tex
    """

    def __init__(self, size, title):
        """
        Constructs all the necessary attributes for the view part of the application

        Parameters:
        -----------
        size : int
            The size (X x Y) of the window when the application starts
        title : str
            The title of the window
        """

        self.window = tk.Tk()
        self.window.geometry(size)
        self.window.title(title)
        self.window.minsize(width=380, height=420)
        self.window.grid_columnconfigure(0, weight=1)

        self.txt = tk.StringVar()

        self.textField = tk.Entry(self.window, width=50, font=(25))
        self.textField.config(state="readonly", textvariable=self.txt)
        self.textField.grid(row=0, column=0, sticky="we", padx=5, pady=5)        
        
        self.copyBut = tk.Button(text="Copy", font=(10), command=lambda: copyBut(self.textField))
        self.copyBut.grid(row=1, column=0, padx=5, pady=5)

        self.slider = tk.Scale(self.window, label="Length of the password", from_=5, to=24, orient="horizontal", length=400, font=(15))
        self.slider.grid(row=2, column=0, sticky="w", pady=10)

        checkVarLett = tk.IntVar()
        checkVarNumb = tk.IntVar()
        checkVarSpecial = tk.IntVar()

        self.checkBoxLett = tk.Checkbutton(self.window, text="a-z, A-Z", variable=checkVarLett, font=(15))
        self.checkBoxLett.grid(row=3, column=0, sticky="w", pady = 10)
        
        self.checkBoxNumb = tk.Checkbutton(self.window, text="0-9", variable=checkVarNumb, font=(15))
        self.checkBoxNumb.grid(row=4, column=0, sticky="w", pady = 10)

        self.checkBoxSpecial = tk.Checkbutton(self.window, text="!@#$%^&*", variable=checkVarSpecial, font=(15))
        self.checkBoxSpecial.grid(row=5, column=0, sticky="w", pady = 10)

        self.enterBut = tk.Button(text="Generate", font=(15), command=lambda: enter(checkVarLett.get(), checkVarNumb.get(), checkVarSpecial.get(), self.slider.get(), self))
        self.enterBut.grid(row=6, column=0, pady=10)

        self.menuBar = tk.Menu(self.window)
        self.window.config(menu=self.menuBar)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Save", command=lambda: saveList("psw.txt", self.textField.get()))
        self.fileMenu.add_command(label="Load", command=lambda: loadList("psw.txt", self))

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)


    
    def getWindow(self):
        """
        Return the main window of application
        """
        return self.window
    
    def setTextField(self, tex):
        """
        Modify the Entry() with the string tex

        Parameters:
        -----------
        tex : str
            the string to replace in the Entry()
        """
        self.txt.set(tex)
