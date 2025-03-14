# Day 8
# Used it to make a daily affirmation generator. I had fun with the if statements.
print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")



if name =="Ambika" or name == "ambika":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("Happy first day of the week", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("It's only the second day of the week", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("Almost half way through the week", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"your week is almost over!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "It's FRIDAY!")

elif name == "Sam" or name== "sam":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look happier today", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "it's FRIDAY!")
else:
 print("I do not know your name, but I hope you are having a great day!")
