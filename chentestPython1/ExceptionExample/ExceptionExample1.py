'''
Created on May 25, 2017

@author: chenz
'''
import sys

def functioin2(input):
    try:
        a=5/input
    except ZeroDivisionError:
        raise ValueError('function 2 ZeroDivisionError ')

def function1(inputstring):
    if inputstring=='1':
        raise ValueError('level should not 1')
     

try:
    function1('11')
    functioin2(10)
    f = open("test111.txt")
except ValueError as ev:
    print("level error:", ev.args[0])
except IOError as ev:
    print("level IOError:", ev.args[0])
except Exception as e:
    print("Unexpected error in main function:", e.args[0])
finally:
    print("done")
     
     
     
 