#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n= int(input("Please enter a Positive Integer! "))
c=0
while c <= n:
    c+= n 
    p=c
print("You have reached your integer! ", p)
#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
s= "Olympic College"
for char in s:
    print(char.upper())
#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
for i in range(21):
    if i % 2 == 0:
        print(i)
#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:(See Mod5 Practice Page)
print("5 X 5 Multiplication Table")
for row in range(1,5+1):
    for col in range(1,5+1):
        print(row*col, end="\t")
    print()
#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:(See mod5 practice page)
num=int(input("Enter a number that is not 0 to have it printed :) "))
while num > 0:
    print("Your number is ",num)
    num=int(input("Enter another number! 0 will end the program :) "))
if num <= 0:
    print("End of program")
