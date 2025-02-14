#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
number=[1,3,4,2,6]
e=0
for i in number:
    if i % 2 == 0:
        e += i
print(e)
print(" ")
#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
words=["Olympic","Word","Olympic","Eggbert","Olympic","Sans"]
print(words.count("Olympic"))
print(" ")
#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
string=["test","egg","to","a","Hello"]
filt_string=[word for word in string if len(word) >=3]
print(filt_string)
print(" ")
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
num=[1,-2,4,-6,3,5,-7]
pos_num=[x for x in num if x > 0]
neg_num=[x for x in num if x < 0]
print(pos_num)
print(neg_num)
print(" ")
#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
square=[2,4,6]
new_square=[]
for num in square:
    new_square.append(num ** 2)
print(new_square)
