'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
file = open("D:\CIS141\SkillsDemo\gardening_tips.txt.txt", "r")
content = file.read()
print(content)
file.close()
print(" ")
'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
files = open("D:\CIS141\SkillsDemo\hiking_log.txt", "a")
while True:
    hike= input("What was the Name of your Hike? (0 to exit): ")
    if hike == "0":
        break
    distance= input("How far did you go in miles? (0 to exit): ")
    if distance == "0":
        break
    files.write(hike + "\t" + distance + "\n")
files.close()
files= open("D:\CIS141\SkillsDemo\hiking_log.txt", "r")
log = {}
for line in files:
    stripped_line = line.strip()
    key_val_list = stripped_line.split("\t")
    key = key_val_list[0]
    val = key_val_list[1]
    log[key] = val
files.close()
print(log)
print(" ")
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
with open("D:\CIS141\SkillsDemo\song_lyricks.txt","r") as filea:
    lyrics = filea.read()
word_counts = {}
for i in range(5):
    wordy= input(f"Enter what word {i+1} you want to search :")
    word_counts[wordy] = lyrics.split().count(wordy)
print("\n Word Count: ")
print(word_counts)
print(" ")
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
with open("D:\CIS141\SkillsDemo\poll.txt", "r") as fileb:
    votes = fileb.read().strip().split(",")
vote_count = {"yea": votes.count("yea"), "nah": votes.count("nah")}
print("\nVote Count:")
print(vote_count)
# I wrote nah on accident hope thats fine vs nay let me know if i need to redo it with nay instead. 
# Coding note: dont know why my VSCode wont read from the directory so direct paths are used. uploading text documents to github also for review. 