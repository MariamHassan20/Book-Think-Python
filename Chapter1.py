# -----------------------------------------------
# This is soultion for exercises of chapter 1, from Think Python Book 
# written by: Mariam Hassan 
# -----------------------------------------------


#------------------------------------------------
#Exercise 1.1. It is a good idea to read this book in front of a computer so you can try out the examples as you go.
#Whenever you are experimenting with a new feature, you should try to make mistakes. 
#For example, in the “Hello, world!” program, what happens if you leave out one of the quotation marks? What if you leave out both? What if you spell print wrong?
#This kind of experiment helps you remember what you read; it also helps when you are programming, because you get to know what the error messages mean. It is better to make mistakes now and on purpose than later and accidentally.

#  1. In a print statement, what happens if you leave out one of the parentheses, or both?
#print ("Helo Worlg" # Leave one of the parentheses
#print "Helo Worlg" # Leave two of the parentheses

#  2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
#print ("Helo Worlg) # Leave one of the quotation marks
#print (Helo Worlg) # Leave two of the quotation marks

# 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
print (2++2) #normal add 

#  4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
#x=011
#print(x)

#  5. What happens if you have two values with no operator between them?
#print(2 6)
#------------------------------------------------

#------------------------------------------------
# Exercise 1.2. Start the Python interpreter and use it as a calculator.
#  1. How many seconds are there in 42 minutes 42 seconds?
seconds= 42
minutes= 42
seconds= (minutes*60)+ seconds
print("Seconds:", seconds)

#  2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilo= 10
miles= kilo/1.61
print("Miles:", miles)

#  3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
kilo= 10
miles = kilo/1.61 #first convert from kilo to mile
minutes= 42+(42/60) #given minutes plus seconds in minutes
seconds= 42+(42*60)#given minutes plus seconds in seconds 
paceINmin= minutes/miles 
paceINsec= seconds/miles
minTOhour= minutes/60 #convert minutes and seconds to hour 
speed= miles/minTOhour
print("The average pace the time per mile in minutes is:", paceINmin)
print("The average pace the time per mile in seconds is:", paceINsec)
print("The average speed in miles per hour is:", speed)
#------------------------------------------------

