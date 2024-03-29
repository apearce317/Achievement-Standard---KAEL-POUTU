# Sequence 1 Kael Poutu 27/06/22 Base Quiz v2

# importing the random library
import random 

#globals and question lists
score = 0
english = ["battery","wifi","podcast","folder","text"]
right_answer = ["puhiko", "ahokore","pahorangi","kopaki","patuhi"]
option_1 = ["tihau","motoka", "kai","hikoi","haka"]
option_2 = ["manuhiri", "whenua", "tane","tuatara","pounamu"]

# Sequence 2 Kael Poutu 29/06/22 v2

#define a function to generate a question
def generate_question(english, right_answer, option_1, option_2):
  global score
  print("what is the correct word for", english, "in maori")
  # Generate a random number to determine the sequence of answers
  # if random_sequence = 0 the right answer would be c
  random_sequence = random.randint(0,2)
  #seperate print statements for readability
  if (random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      print("correct.")
      score += 1
    else:
      print("incorrect.")
  # if random_sequence = 1 the right answer would be a
  if (random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      print("correct.")
      score += 1
    else:
      print("incorrect.")
  # if random_sequence = the right answer would be b
  if (random_sequence == 2):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      print("correct.")
      score += 1
    else:
      print("incorrect.")


# Sequence 3 Kael Poutu 29/06/22 v2

# generate 5 questions pulling possible answers from lists.
for i in range (0,5):
  generate_question(english[i], right_answer[i], option_1[i], option_2[i])

  #print the score at the end of the quiz
if score > 2:
  print("Yay your", score, "was Great")
else:
  print("You have failed your score was",score)

