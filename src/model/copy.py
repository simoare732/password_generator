import pyperclip

def copyToClipboard(text):
    """
    Copy the text given as parameter in the clipboard

    Parameters:
    -----------
    text : str
        The string to copy in the clipboard
    """

    pyperclip.copy(text)