import random

# Functions go here
def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()
    
    if response == "yes" or response =="y":
      response = "yes"
      return response
      
    elif response == "no" or response == "n":
      response = "no"
      return response
    
    else:
      print("Please answer yes / no")

def instructions():
  print("**** How to Play ****")
  print()
  print("The rules of the game go here")
  print()
  return""

 
# Main Routine goes here
def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10\n"
  
  valid = False
  while not valid:
    try:
      # ask the question 
      response = int(input(question))
      # if the amount is too low / too high give
      if  low < response <= high:
        return response
      
      # output an error
      else:
        print(error)
  
    except ValueError:
      print(error)

# Main routine goes here
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
  instructions()
  
instructions()

# ask user how much they want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = 5 

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

  # increase # of rounds played
  rounds_played += 1

  # print round number
  print()
