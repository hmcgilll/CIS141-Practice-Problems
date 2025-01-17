# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
firstnumber=int(input("Please Input your first number"))
secondnumber=int(input("Please Input your second number"))
addition=(firstnumber+secondnumber)
subtraction=(firstnumber-secondnumber)
multiplication=(firstnumber*secondnumber)
division=(firstnumber/secondnumber)
print(addition,subtraction,multiplication,division)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
firstnumber=int(input("Please Input your first number of the side of a triangle"))
secondnumber=int(input("Please Input your second number of the side of a triagnle"))
thirdnumber=int(input("Please input your third number of the side of a triangle"))
s=(firstnumber+secondnumber+thirdnumber)/2
s2= int(s*((s-firstnumber)+(s-secondnumber)+(s-thirdnumber)))
a=math.sqrt(s2)
print(a)
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
numbers= []
for i in range(5):
    num = int(input("Enter a number"))
    numbers.append(num)
total= sum(numbers)
average= total/len(numbers)
minimum= min(numbers)
maximum=max(numbers)
range_value= maximum - minimum
deviation= sum((x - average) ** 2 for x in numbers) / len(numbers)
standard= math.sqrt(deviation)
print(total)
print(average)
print(minimum)
print(maximum)
print(range_value)
print(standard)
