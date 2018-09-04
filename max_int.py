'''
    get input from user (any number)
    unless user inputs a negative number
    repeat getting input from user.
    if max is lower than current input
    repleace max int
    print max int when a negative number is inputted
'''
num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int

while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if max_int < num_int:
        max_int = num_int
print("The maximum is", max_int)