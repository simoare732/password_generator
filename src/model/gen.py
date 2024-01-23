import random

@staticmethod
def genLetter():
    """
    Generate (and return) a capital letter or a small letter
    """
    # from capital letters to small letters there is a difference of 32 in the ASCII code. For example 'a' == 97, 'A' == 65
    off = [0,32] 
    
    # chr() func, convert a number to its symbol in ASCII code. The difference first operand is a number from 97 to 122 (a-z) the second 
    # is a number between 0 and 32. Whether the second operand is 0 the letter given will be small or will be 32 se letter given will be capital
    lett = chr(random.choice(range(97,122))-random.choice(off))
    return lett

@staticmethod
def genNumber():
    """
    Generate (and return) a number among 0 and 9
    """
    return str(random.randint(0,9))

@staticmethod
def genSymbol():
    """
    Generate (and return) a symbol
    """

    symbols = ["!","@","#","$","%","^","&","*"]
    return random.choice(symbols)

@staticmethod
def genPassword(isLetter, isNumber, isSymbol, length):
    """
    Generate (and return) a password of a length given

    Parameters:
    -----------
    isLetter : boolean
        is true if in the password there will be letters
    isNumber : boolean
        is true if in the password there will be numbers
    isSymbol : boolean 
        is true if in the password there will be symbols
    length : int
        the length of the password generated

    """

    string = ""
    if (not isLetter and not isNumber and not isSymbol) or length < 5:
        return string
    elif isLetter and isNumber and not isSymbol:
        for i in range(0,length):
            ch = random.randint(1,2)
            if ch == 1:
                string += genLetter()
            else: string += genNumber()
    elif isLetter and not isNumber and isSymbol:
        for i in range(0,length):
            ch = random.randint(1,2)
            if ch == 1:
                string += genLetter()
            else: string += genSymbol()
    elif not isLetter and isNumber and isSymbol:
        for i in range(0,length):
            ch = random.randint(1,2)
            if ch == 1:
                string += genNumber()
            else: string += genSymbol()
    elif isLetter and not isNumber and not isSymbol:
        for i in range(0,length):
            string += genLetter()
    elif not isLetter and isNumber and not isSymbol:
        for i in range(0,length):
            string += genNumber()
    elif not isLetter and not isNumber and isSymbol:
        for i in range(0,length):
            string += genSymbol()
    elif isLetter and isNumber and isSymbol:
        for i in range(0,length):
            ch = random.randint(1,3)
            if ch == 1:
                string += genLetter()
            elif ch == 2: 
                string += genNumber()
            else: string += genSymbol()
    return string