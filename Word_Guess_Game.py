word_list = ["aardvark", "baboon", "Camel"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
placeholder = ""
for blank in range(word_length):
    placeholder += "_"
print(placeholder)  


game_over = False
correct_letters =[]

while not game_over:
    guess = input("Enter your first Guess:").lower()
    print(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
                display += letter
                correct_letters.append(guess)
        elif letter in correct_letters:
             display+= letter
        else:
            display += "_"    
    print (display)

    if "_" not in display:
         game_over=True
         print ("You win")
         print ("add")