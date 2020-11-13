#######---------------------------------------########
# Book: Think python
# This is soultion for exercises of chapter 3, from Think Python Book 
# by: Mariam Hassan
#######---------------------------------------########


#######---------------------------------------########
#Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
#and prints the string with enough leading spaces so that the last letter of the string is in column 70
#of the display.
#>>> right_justify('monty')
#monty
#Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
#that returns the length of a string, so the value of len('monty') is 5.

def right_justify(text):
    space= ' '*(70-len(text)) # multiply the space with 70 - the lenght of text to ensure that the text start at the 70th position 
    full_text= space + text
    print(full_text)

right_justify("monty")
#######---------------------------------------########



#######---------------------------------------########

#Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and calls it twice:
#def do_twice(f):
#f()
#f()
#Here’s an example that uses do_twice to call a function named print_spam twice.
#def print_spam():
#print('spam')
#do_twice(print_spam)
    #1. Type this example into a script and test it.

#def do_twice(f):
#    f()
#    f()
#def print_spam():
#    print('spam')
#do_twice(print_spam)

    #2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
    #function twice, passing the value as an argument.
#def do_twice(f,v):
#	f(v)
#	f(v)
	
    #3. Copy the definition of print_twice from earlier in this chapter to your script.
#def print_twice(bruce):
#    print(bruce)
#    print(bruce)
    #4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument
#def do_twice(f,text):
#	f(text)
#	f(text)
	
#def print_twice(s):
#	print(s)
#	print(s) # to print onlt two lines remove this print statment 

#do_twice(print_twice,"spam")

    #5.Define a new function called do_four that takes a function object and a value and calls the
    #function four times, passing the value as a parameter. There should be only two statements in
    #the body of this function, not four.
def do_twice(f,text):
	f(text)
	f(text)

def do_four(f,text):
	do_twice(f,text)
	do_twice(f,text)
	
def print_twice(s):
	print(s)
	print(s)

do_four(print_twice,"four")


#######---------------------------------------########

#Exercise 3.3. Note: This exercise should be done using only the statements and other features we
#have learned so far.
#1. Write a function that draws a grid like the following:
#Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
#print('+', '-') By default, print advances to the next line, but you can override that behavior and put a
#space at the end, like this:
#print('+', end=' ')
#print('-')
#The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line

def do_two(f):
	f()
	f()

def print_two(v):
	print (v*2)

	
def do_four(f):
	f()
	f()
	f()
	f()
	

def print_dash():
	print ( '-', end=' ' )

def print_line_short():
	print ("+", end=' ')
	do_four(print_dash)
	

def print_line():
	do_two(print_line_short)
	print ("+", end=' ')

def print_line_four():
	do_four(print_line_short)
	print ("+", end=' ')
	
def print_vbar():
	print(("|"+" "*9)*2+"|")

def print_vbar_four():
	print(("|"+" "*9)*4+"|")


def print_grid_two():
	print_line()
	print("")
	do_four(print_vbar)
	print_line()
	print("")
	do_four(print_vbar)
	print_line()
	

print_grid_two()

#2. Write a function that draws a similar grid with four rows and four columns

def print_grid_four():
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()

print(" \n")
print_grid_four()
#######---------------------------------------########
