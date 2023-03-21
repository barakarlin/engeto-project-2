"""
project_2.py: druhý projekt do Engeto Online Python Akademie
author: Bara Karlinova
email: bara.karlinova@kiwi.com
discord: BaraKar#6094
"""

import random

separator = '-' * 47

# Program pozdraví užitele a vypíše úvodní text
print("Hi there!",
      separator,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.",
      separator, sep = '\n')

# Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
def num_generator():
      first_value = random.randint(1, 9)
      digits = [digit for digit in range(10) if digit not in [first_value]]
      last_3_values = random.sample(digits, 3)
      rand_num = [first_value] + last_3_values
      return rand_num

def bulls_cows():
      random_number = num_generator()
      game_on = True
      runs = 0
      while game_on:
            guessed_number = input('Enter a number: ')
            # Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
            # pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
            if guessed_number.isdigit():
                  if len(str(guessed_number)) != 4:
                        print('Given number does not have four digits.')
                  else:
                        if (str(guessed_number).startswith('0')) & (len(set(guessed_number)) == 4):
                              print('Given number starts with 0.')
                        elif (not str(guessed_number).startswith('0')) & (len(set(guessed_number)) < 4):
                              print('Given number contains duplicate digits.')
                        elif (str(guessed_number).startswith('0')) & (len(set(guessed_number)) < 4):
                              print('Given number starts with 0 and contains duplicate digits.')
                        else:
                              guessed_number_list = []
                              [guessed_number_list.append(int(i)) for i in guessed_number]
                              print(guessed_number_list)

                              bulls = 0
                              cows = 0

                              # Program vyhodnotí tip uživatele
                              for i in range(4):
                                    if guessed_number_list[i] == random_number[i]:
                                          bulls += 1
                                    else:
                                          if guessed_number_list[i] in [j for j in random_number if j not in [random_number[i]]]:
                                                cows += 1

                              runs += 1

                              # Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows
                              # (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a
                              # množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
                              if bulls < 4:
                                    if (bulls == 1) & (cows == 1):
                                          print(f"{bulls} bull, {cows} cow")
                                    elif (bulls != 1) & (cows == 1):
                                          print(f"{bulls} bulls, {cows} cow")
                                    elif (bulls == 1) & (cows != 1):
                                          print(f"{bulls} bull, {cows} cows")
                                    else:
                                          print(f"{bulls} bulls, {cows} cows")
                              else:
                                    game_on = False
                                    print(f"Correct, you've guessed the right number in {runs} guesses!")
            else:
                  print('Given input is not a number')

      print(separator)

      if runs < 11:
            print("That's amazing!")
      elif runs < 21:
            print("That's average.")
      else:
            print("That's not so good.")


if __name__ == "__main__":
    bulls_cows()

