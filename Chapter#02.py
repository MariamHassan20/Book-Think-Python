# -----------------------------------------------
# This is soultion for exercises of chapter 1, from Think Python Book 
# by: Mariam Hassan 
# -----------------------------------------------


#------------------------------------------------

#Exercise 2.1. Repeating my advice from the previous chapter, whenever you learn a new feature,
#you should try it out in interactive mode and make errors on purpose to see what goes wrong.
#       • We’ve seen that n = 42 is legal. What about 42 = n?
#42 = n # ie illegal, SyntaxError: cannot assign to literal 
#       • How about x = y = 1?
x = y = 1 # x and y will have the same value which is 1 
print(x)
print(y)
#       • In some languages every statement ends with a semi-colon, ;. What happens if you put a
#         semi-colon at the end of a Python statement?
print("Hi there we are putting semi-colon at the end"); # it works however, it shows a warning massage that there is no need for a semi-colon 
# semi-colon is not a must in python, but we use it if we want to print multiple statments at the same line 
print("Hi there before semi-colon"); print("Hi there after the semi-colon") # they will be print in two lines as if they are written here in two lines 
#       • What if you put a period at the end of a statement?
#print("Hi there we are putting a period at the end of this statment"). yntaxError: invalid syntax
#       • In math notation you can multiply x and y like this: xy. What happens if you try that in
#       Python?
#print(xy) # xy is considered a varibale , NameError: name 'xy' is not defined
#------------------------------------------------



#------------------------------------------------
#Exercise 2.2. Practice using the Python interpreter as a calculator:
#1. The volume of a sphere with radius r is () What is the volume of a sphere with radius 5?
import math
r=5
volume = (4/3)*math.pi*math.pow(r, 3) # I can use also r**3 instead of pow() function 
print("The Volume of a sphere with radius r=5 is:", volume)
#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
#$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
#60 copies?
book_price= 24.95
book_price_after_discount= (book_price*60)/100
first_ship= 3
any_ship= 0.75
num_ships= 60
#total wholesale cost for 60 copies
cost= (book_price_after_discount*60) + first_ship + (any_ship*(num_ships-1))
print(f"The total wholesale cost for 60 copies is: {cost} dollars")
#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
# Basic calculations :
     # 1- Hour to min = hour*60
     # 2- min to sec  = min*60
     # 3- Hour to sec = Hour*60*60 
     # to go versa devide 
# pace is speed 
# He left home at 6:52 am 
# he took 8 min and 15 sec per mile in easy pace 
# he took 7 min and 12 sec per mile at tempo pace 
# beacuse we have min and seconds convert all to seconds to unify the unit 
number_mile_easy_pace= 2
number_mile_tempo_pace = 3
time_easy_pace= (8*60)+15    # in seconds per mile 
time_tempo_pace= (7*60)+12   # in seconds per mile  
total_time_easy_pace= number_mile_easy_pace* time_easy_pace     # in seconds 
total_time_tempo_pace= number_mile_tempo_pace* time_tempo_pace  # in seconds 
total_time= total_time_easy_pace+total_time_tempo_pace          # in seconds 

# the time he spend running is 38.1 minutes => print(total_time/60) 
# we can use math operation or buildin function 
# buildin function solution 
import datetime
a= datetime.datetime(2020,1,1,6, 52, 0)
b= a + datetime.timedelta(0,total_time)
print("He will get home at", b.time())   # use time() to remove date and keep only time 

# math operation solution 
#start_time= (6*60+52)*60   # convert the time he left home in seconds 
#total_time_easy_pace= number_mile_easy_pace* time_easy_pace     # in seconds 
#total_time_tempo_pace= number_mile_tempo_pace* time_tempo_pace  # in seconds
# finish_hour = (start_time + total_time_easy_pace + total_time_tempo_pace)/(60*60.0)
#finish_floored = (start_time + total_time_easy_pace + total_time_tempo_pace)//(60*60) # or just type int(finish_floored)
#finish_minute  = (finish_hour - finish_floored)*60
#print (f"He will get home at {finish_hour}: {finish_minute}"") 
#------------------------------------------------
