
@staticmethod
def saveToFile(data, filename, how):
    """
    A method that save data on filename. The file is opened in write or append

    Parameters:
    -----------
    data : str
        The string(s) to write
    filename : str
        The name of the file
    how : str
        A letter that can be w (write) or a (append) to know how open the file
    """
    with open(filename, how) as file:
        file.write(data)

@staticmethod
def loadFromFile(filename):
    """
    A method that load data from filename.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()  
    except FileNotFoundError:
        return None