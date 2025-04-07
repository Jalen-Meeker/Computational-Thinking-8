#Beginning: crete variables
introvert_points=0
extrovert_points=0

#Middle: Ask questions
answer=input("On a weekend would you rather A) stay home all day, or B) go out with friends?")
if answer == "A":
   introvert_points += 1
elif answer == "B":
   extrovert_points += 1


answer=input("Do you like A) Reading a book, or B) Calling a friend?")
if answer == "A":
   introvert_points += 1
elif answer == "B":
   extrovert_points += 1


answer=input("Do you have A) Less than 4 friends, or B) More than 4 friends")
if answer == "A":
   introvert_points += 1
elif answer == "B":
   extrovert_points += 1


answer=input("Do you like to A) Write, or B) Make new friends")
if answer == "A":
   introvert_points += 1
elif answer == "B":
   extrovert_points += 1


answer=input("Do you like to A) Read, or B) Be in a leadership role?")
if answer == "A":
   introvert_points += 1
elif answer == "B":
   extrovert_points += 1



#End: determine results
if introvert_points > extrovert_points:
    print("You are an introvert")
elif extrovert_points > introvert_points:
   print("You are an extrovert")
elif introvert_points == extrovert_points:
   print ("You are an ambivert")