'''
    print out n number of numbers
    where the sequence is 1, 2, 3, 6, 11, 20, 37.
    so it prints out the first 3 numbers and then
    every subsequent number takes the last 3 numbers
    that came before it and adds them together.
'''
n = int(input("Enter the length of the sequence: ")) # Do not change this line

x = 1
y = 2
c = 3
number = 0
print(x)
print(y)
print(c)

for i in range(3,n):
    number = x + y + c
    print(number)
    x = y
    y = c
    c = number