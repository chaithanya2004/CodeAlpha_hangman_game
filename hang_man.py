import random
print("Let's play  the game by gussing the letter ,Hangman")
print("Get ready to guess")

###accepting the name of player
def welcometogame():
  name=input("we welcome you to the game! Please Enter your goodname:\n")
  print("Hii",name,"enjoy the game")

book_of_word = ["fungame", "name", "diamond", "memory","happy","hello", "tour", "wish", "school","football"]
welcometogame()  

### Choose a random word
randomchoice= random.choice(book_of_word)
for i in  randomchoice:
  print("_",end="")

def print_hangman(wrong):
  if(wrong == 0):
    print("\n*---*")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n*---*")
    print("*   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n*---*")
    print("*   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n*---*")
    print(" *  |")
    print(" |\ |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n*---*")
    print(" *  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n*---*")
    print(" *  |")
    print("/|\ |")
    print("  \ |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" *  |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")    

def printWord(letterguessed):
  correctletters=0
  wordcount=0
  for char in randomchoice:
    if(char in letterguessed):
      print(randomchoice[wordcount], end=" ")
      correctletters+=1 
    else:
      print(" ",end=" ")
    wordcount+=1
  return correctletters

def printLines():
  print("\r")
  for char in randomchoice:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomchoice)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 7 and current_letters_right != length_of_word_to_guess):
    print("\nyou guessed letters: ")
    for letter in current_letters_guessed:
      print(letter, end=" ")
      #user input
    you_guessed_letter= input("\nJust drop the letter: ")
    if(randomchoice[current_guess_index] ==you_guessed_letter ):
      print_hangman(amount_of_times_wrong)
      current_guess_index+=1
      current_letters_guessed.append(you_guessed_letter)
      current_letters_right = printWord(current_letters_guessed)
      printLines()
    else:
      amount_of_times_wrong+=1
      current_letters_guessed.append(you_guessed_letter)
      print_hangman(amount_of_times_wrong)
      current_letters_right = printWord(current_letters_guessed)
      printLines()

print("\n**you done with your game: Thank you for playing **")
print("The word is:")
print(randomchoice)    
       

    
