"""
The while loop will repeat a block of code unitl a certain condition becames false.

The while loop, in most of the time, you don't know how many times, you'll need to repeat the loop, very different from the for loop.

input() --> It's a function that you capture what the user type in.

!= --> this command means 'not equal to'.

"""

"""
x = 0

while x < 5:
	print(x)
	x += 1 #This notation is a shortcut for writing 'x = x + 1'
	
"""

print("Enter your relative names and yours. If you want to stop, just type 'stop'.")
s = ''

while s != 'stop':
	s = input('Enter you name here: ')