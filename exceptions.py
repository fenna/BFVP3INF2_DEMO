"""
Met exception handling kunnen we dus op een nette manier omgaan met fouten 
en er ook iets zinvols aan doen. Bijvoorbeeld een bericht geven aan de gebruiker 
als een bestand niet is gevonden. 
Python handelt de exception handling af met try, except Basis Syntax:

try:
    # write some code 
    # that might throw exception
except <ExceptionType>: 
    # Exception handler, alert the user

Uitgebreide syntax:

try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:# deze wordt alleen uitgevoerd als er geen fout is opgetreden
    <process_else>
finally: #deze wordt altijd uitgevoerd
    <process_finally>
"""

try:
    num1, = input()
    num2 = input()
    result = num1 + num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")