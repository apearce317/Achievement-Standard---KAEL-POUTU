score = 0
# Question 1
question1 = input("How do you say Battery in Maori \n a. Puhiko \n b. Takiputa \n c. Patuhi \n d. Tiriata \n Answer: ").lower()

if question1 == "a" or question1 == "puhiko":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 2
question2 = input("How do you say Wifi in Te Reo? \n a. Waea Atamai \n b. Kupuhana \n c. Tuafafine \n d. Ahokore \n Answer: ").lower()

if question2 == "d" or question2 == "ahokore":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 3
question3 = input("How do you say Podcast in Te Reo? \n a. Pawhiri \n b. Pahorangi \n c. Nga Tautuhinga \n d. Kiriahua \n Answer: ").lower()

if question3 == "b" or question3 == "pahorangi":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 4 
question4 = input("How do you say Folder in Te Reo? \n a. Paeahua \n b. Kopaki \n c. Rakau Pumahara \n d. Rorohiko \n Answer: ").lower()

if question4 == "b" or question4 == "kopaki":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 5
question5 = input("How do you say Text in Te Reo? \n a. Patuhi \n b. Kupuhana \n c. Tikiake \n d. Tiaki \n Answer: ").lower()

if question5 == "a" or question5 == "patuhi":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")


# final message/overall score
if score <= 10:
  print("Your total score is: ", score, "- oof... better luck next time. Try again?")
elif score <= 20:
  print("Your total score is: ", score, "- Nice! You could have done better though! Try again?")
else:
  print("Your total score is: ", score, "- You are a superstar! You got all of the questions correct!")
