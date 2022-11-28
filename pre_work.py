#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")
hello_name("username") 

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
def first_odds():
    for value in range(1, 101):
        if (value % 2) == 1:
            print(value)
first_odds()

def first_odds_other():
    for v in range(1,101,2):
        print(v)
first_odds_other()


#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 
def max_num_in_list(a_list):
    x = (a_list[0])
    for value in (a_list):
        if (value > x):
            x = value
    return x

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
#but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). 
def is_leap_year(a_year):
    if (a_year % 4) == 0:
        if (a_year % 100) > 0:
            if (a_year % 400) == 0:
                return True 
            else:
                return False
        else:
            return True 
    else:
        return False

answer = is_leap_year(2000)
print(answer)

print(is_leap_year(2001))

#Question 5: Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. 

def is_consecutive(li):
    for i in range(0,len(li)):
        if i == len(li) - 1:
            return True
        if li[i] + 1 != li[i+1]:
            return False
        else:
            return False


