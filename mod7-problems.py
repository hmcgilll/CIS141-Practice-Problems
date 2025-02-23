'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(word):
    vowel="aeiouAEIOU"
    count=0
    for char in word:
        if char in vowel:
            count += 1
    return count
print(count_vowels("euouae"))
print(" ")
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    smallcase=(s.lower())
    reverse_s = smallcase[::-1]
    return smallcase == reverse_s
print(is_palindrome("Rotor"))
print(is_palindrome("Oryx"))
print(is_palindrome("rotor"))
print(' ')
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attack, defence):
    effectiveness = {
        ("Water", "Fire"): "Super Effective",
        ("Fire", "Water"): "Not Very Effective",
        ("Electric", "Grass"): "Neutral"}
    if (attack, defence) in effectiveness:
        return effectiveness[(attack, defence)]
    else:
        return "Not Valid"
print (type_advantage("Water" ,"Fire"))
print (type_advantage("Electric", "Grass"))
print (type_advantage("Fire", "Water"))
print(' ')
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age,vehicle):
    total = 0 
    if age <= 18:
        return "Free"
    elif age <=64 and vehicle =="yes":
        total += 20
        return total
    elif age <=64 and vehicle == "no":
        total += 10
        return total
    elif age >=65 and vehicle == "yes":
        total += 15
        return total
    elif age >= 65 and vehicle == "no":
        total += 5
        return total
    else:
        return "Invalid Responce"
print(ferry_fare(16, "no"))
print(ferry_fare(22,"no"))
print(ferry_fare(22,"yes"))
print(ferry_fare(66,"no"))
print(ferry_fare(66,"yes"))
print(ferry_fare(16,"yes"))
print(' ')
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):
    if experience <= 99:
        return "Level 1"
    elif experience <=199:
        return "Level 2"
    elif experience >= 200:
        return "Level 3"
    else:
        return "Not Valid"
print(level_up(80))
print(level_up(120))
print(level_up(240))
