score = 0
# Question 1
answer1 = input("How do you say Battery in Maori \n a. Puhiko \n b. Takiputa \n c. Patuhi \n d. Tiriata \n Answer: ")

if answer1 == "a" or answer1 == "Puhiko":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 2
answer2 = input("How do you say Wifi in Te Reo? \n a. Waea Atamai \n b. Kupuhana \n c. Tuafafine \n d. Ahokore \n Answer: ")

if answer2 == "d" or answer2 == "Ahokore":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 3
answer3 = input("How do you say Podcast in Te Reo? \n a. Pawhiri \n b. Pahorangi \n c. Nga Tautuhinga \n d. Kiriahua \n Answer: ")

if answer3 == "b" or answer3 == "Pahorangi":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 4 
answer4 = input("How do you say Folder in Te Reo? \n a. Paeahua \n b. Kopaki \n c. Rakau Pumahara \n d. Rorohiko \n Answer: ")

if answer4 == "b" or answer4 == "Kopaki":
  score += 5
  print("Correct!")
  print("Score: ", score)
  print("\n")
else:
  print("Incorrect! Maybe next time!")
  print("Score: ", score)
  print("\n")

# Question 5
answer5 = input("How do you say Text in Te Reo? \n a. Patuhi \n b. Kupuhana \n c. Tikiake \n d. Tiaki \n Answer: ")

if answer5 == "a" or answer5 == "Patuhi":
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
