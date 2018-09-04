'''
    get input from user (any number)
    unless user inputs a negative number
    repeat getting input from user.
'''
number = input("Input any number: ")

while int(number) >= 0:
    number = input("Input any number: ")
print("We got a negative")