import sys

from model.crypt import * 
from model.saveLoad import *

@staticmethod
def saveList(filename, txt):
    """
    Method run when Save is pressed. Save the txt  in the file called filename

    Parameters:
    ------------
    filename : str
        The name of the file
    txt : str
        The text (password) to save
    """
    key = genKey()
    cypText = encryptText(txt, key)
    saveToFile(key, filename, 'w')
    saveToFile("\n", filename, 'a')
    saveToFile(cypText, filename, 'a')


@staticmethod
def loadList(filename, wind):
    """
    Method run when Load is pressed. Load from a file called filename and write it in the Entry()

    Parameters: 
    -----------
    filename : str
        The name of the file
    wind : Tk
        The main windows of the application
    """
    string = loadFromFile(filename)
    key = string[0]
    print(key)
    cypText = string[1]
    text = decryptText(cypText.encode("utf-8"), key.encode("utf-8"))
    wind.setTextField(text)


