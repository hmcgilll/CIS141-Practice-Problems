#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
# A,B, (A AND B),(NOT B)
# TRUE TRUE    FALSE
# TRUE FALSE   TRUE
# FALSE TRUE   FALSE
# FALSE FALSE  FALSE 
# comment Im not super confident on this so feedback would be nice. this is the only concept this unit that just does not click with me. 
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
headlight= 22
if headlight < 8:
    print("Headlight on")
else:
    print("Headlight off")
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
bank=int(input("What is your Current bank balance? This is to determine if you are below 100 Dollars Currently.  "))
if bank < 100:
    print("True")
else:
    print("False")
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age=int(input("What is your Age? This is to determine What movies you can see.  "))
if age >= 18:
    print("You may see R Rated Movies")
elif age >= 13:
    print("You may see PG-13 Movies")
else:
    print("You may only see G/PG Rated Movies")
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
total=float(input("What is the current total of you order? "))
if total <50:
    shipping=5
else:
    shipping=0
order=total+shipping
print(f"Your total including shipping is {order:.2f}")
