# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word=input("Give me a word!")
repeat=int(input("How many times do you want it to repeat?"))
finalresult=(word * repeat)
print(finalresult)
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name=input("Give me Your Name!")
age=int(input("How Old are you?"))
age2= (age + 1 )
print(f"Hello, {name}! You are {age} years old. Next year, you will be {age2} years old.")
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence=input("Give me a Sentence!")
wordy=input("Give me a word to find in this sentence! ")
print(sentence != wordy)
# Comment note. This is my best attempt im very lost on this one 
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
text=input("Write out word to slice ")
input1=int(input("Starting at 0 give me a starting point "))
input2=int(input("Give me an end point from your word"))
splice=text[input1:input2]
print(splice)
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("Hello | I | Am | Iron Man")
