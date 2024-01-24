# Password generator
Password generator for your accounts

![funny image of password](https://github.com/simoare732/password_generator/blob/main/images/image2.png?raw=true)

# Description
This is a simple application to generate a secure password. The length of that could be between 5 and 24 characters. 
The application can save (and load) the password generated on a file (in the view directory) called psw.txt. The applicaton will save the encrypted password 

**_WARNING_** the file is composed by 2 rows. The first is the key for decrypt the password, the second one is the encrypted password.

**It's not secure to save your password in a txt file**, I'm done that just for fun.

# Requirments
* Python 3.10 or higher
* Library Tkinter 8.6 or higher
* Library pyperclip 1.8.2 o higher
```powershell
pip install pyclip
```
* Library cryptography 42.0.0 or higher
```powershell
pip install cryptography
```
* To run the application, you can run press /src/main.py, or (from the directory src)
```powershell
python ./main.py
```

# Screenshot
![Screenshot of application running](https://github.com/simoare732/password_generator/blob/main/images/image1.png?raw=true)

# Made by
Made by simoare732

Date : 01/22/2024 mm-dd-yyy
