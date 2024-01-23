import sys

from model.copy import copyToClipboard 

@staticmethod
def copyBut(textField):
    """
    Function run when the copy button is pressed. Copy the value of Entry in clipboard
    """
    copyToClipboard(textField.get())