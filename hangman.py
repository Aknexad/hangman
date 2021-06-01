import random

# list and random choice
# world_list = ["ardvark","baboon","camel"]
 
from list import world_list
chosen_word = random.choice(world_list)

print(chosen_word)

lives = 6

# crate blank 
display = []
for _ in range(len(chosen_word)):
    display.append("_")
# print(display)


end_of_game = False

while not end_of_game:
    gauss = input("guess a letter").lower()

    if gauss in display:
        print(f"you gave alerady guessed {gauss}")

    # chaking a geuss macing letter and rplice blank
    for postion in range(len(chosen_word)):
        letter = chosen_word[postion]
        if letter == gauss :
            display[postion] = letter 

    if gauss not in chosen_word:
        print(f"you guessed {gauss}thats not in the word")
        lives -=1
        if lives == 0 :
            end_of_game = True
            print("you lose")        

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you wine")

    from habgnab_art import stage
    print(stage[lives])    
