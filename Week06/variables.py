# lab6.1.2-variables.py
# This program to show Variables can be of type function.
# author: David Burke

def fun1():
    print("this is fun1")
def fun2():
    print("this is fun2")

whichFun = fun1
whichFun()
whichFun= fun2
whichFun()