########
#Quiz 1
########
#Part3: Write a program that asks the user to enter their age in years as input
#assume that the user enters a positive integer) and calculates and prints how old the user is in terms of days.
#Assume that there are 365 days in a year. For example: if the user enters

#Answer:
# Type your code here
x = input('Enter your age: ')
print("You are",int(x)*365,"days old")

#Part 4: Write a program that asks the user for an integer 'x' and prints the value of y after evaluating the following expression:
#y=x2−12x+11

# Type your code here
x = input('Enter your number: ')
y= int(x)*int(x)-12*int(x)+11
print(y)

#Part5:
#Write a program that asks the user for a positive integer between 1 and 7 (Assume that the user may enter any
#number from 1 to 7 both inclusive) and prints the day of week corresponding to that number in all capital
#letters. Assume that the day of the week starts from MONDAY. For example: if the user enters:

# Type your code here
x = input('Enter a positive integer between 1 and 7: ')
y=['','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(y[int(x)])

#Part6:
#Complete the following program such that it calculates and prints the average of the elements of the given list.
# Type your code here
sample_list = [2, 10, 3, 5]
def avg(list):
    sum = 0
    for elm in list:
        sum += elm
    return sum/(len(list)*1.0)
    
print(avg(sample_list))


########
#Quiz2
########

