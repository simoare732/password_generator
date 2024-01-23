import sys

from model.gen import genPassword 


@staticmethod
def enter(letBox, numbBox, symBox, length, wind):
    """
    Function run when enterbutton is pressed. Generate a password and the func going to write the password in the Entry

    Parameters:
    ------------
    letBox : int
        the value of checkBox of letters. It is 1 if the box is selected, 0 otherwise
    numbBox : int
        the value of checkBox of numbers. It is 1 if the box is selected, 0 otherwise
    symBox : int
        the value of checkBox of symbols. It is 1 if the box is selected, 0 otherwise
    length : int
        the value of slider
    wind : Tk
        The main window


    """
    if letBox == 1:
        l = True
    else: l = False

    if numbBox == 1:
        n = True
    else: n = False

    if symBox == 1:
        s = True
    else: s = False

    password = genPassword(l,n,s,length)
    print(password)
    wind.setTextField(password)

