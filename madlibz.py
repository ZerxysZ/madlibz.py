import random

def madlib_story_1():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    part_of_body = input("Enter a part of body: ")
    number = input("Enter a number: ")
    place = input("Enter a place: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    
    madlib = f"{noun} is a {adjective} {plural_noun} that grows on your {part_of_body}. If you don't remove it in {number} days, it will spread to your {place}, making it difficult to {verb_ing}."
    print(madlib)

def madlib_story_2():
    adjective = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    part_of_body = input("Enter a part of body: ")
    number = input("Enter a number: ")
    place = input("Enter a place: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    
    madlib = f"If you ever find yourself in {place}, beware of the {adjective} {plural_noun} that lurk in the shadows. They are known to attack your {part_of_body} and drain your energy in just {number} seconds, leaving you {verb_ing} in pain."
    print(madlib)

def madlib_story_3():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    part_of_body = input("Enter a part of body: ")
    number = input("Enter a number: ")
    place = input("Enter a place: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    
    madlib = f"Legend has it that if you find the {noun} in the {place}, you will be granted {adjective} {plural_noun} that give you the power to control the {part_of_body} of others. But be warned, if you use these powers for {verb_ing}, they will only last for {number} minutes before they disappear forever."
    print(madlib)

def madlib_story_4():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    part_of_body = input("Enter a part of body: ")
    number = input("Enter a number: ")
    place = input("Enter a place: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    
    madlib = f"In a {place} far, far away, there once lived a {adjective} {noun} who had {number} {plural_noun} growing out of their {part_of_body}. Despite the constant {verb_ing}, the {noun} refused to seek medical attention, leading to their eventual demise."
    print(madlib)

def madlib_story_5():
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    part_of_body = input("Enter a part of body: ")
    number = input("Enter a number: ")
    place = input("Enter a place: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    
    madlib = f"In the {place} of {noun}, there is a {adjective} {noun} that has {number} {plural_noun} for {part_of_body}. Legend has it that if you touch one of these {plural_noun} while {verb_ing}, you will be granted {adjective} powers that will last for {number} years. But be warned, the {plural_noun} are guarded by a {adjective} {noun} who will stop at nothing to protect them."
    print(madlib)

import random

def choose_story():
    title_options = [
        "Welcome to Madlibs Mania - Where imagination and humor collide!",
        "Get ready for a wild ride as you fill in the blanks to create hilarious stories.",
        "Choose your adventure! Enter the number of the story you want to play (1-5), or q to quit:"
    ]
    
    story_options = [
        "Get ready to create a laugh-out-loud joke!",
        "Love is in the air in this heartwarming tale!",
        "Unleash your inner superhero in this epic adventure!",
        "Get ready for a spine-tingling horror story!",
        "Step into a world of fantasy and wonder!"
    ]
    
    print(title_options[0])
    print(title_options[1])

    while True:
        print("\n" + title_options[2])
        print("1. " + story_options[0])
        print("2. " + story_options[1])
        print("3. " + story_options[2])
        print("4. " + story_options[3])
        print("5. " + story_options[4])
        print("q. Quit")

        choice = input().lower()

        if choice == 'q':
            print("\nThanks for playing! Goodbye.")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("\nInvalid input. Please enter a number from 1 to 5 or 'q'.")
            continue
        else:
            choice = int(choice)
            if choice == 1:
                print("\n" + story_options[0])
                madlib_story_1()
            elif choice == 2:
                print("\n" + story_options[1])
                madlib_story_2()
            elif choice == 3:
                print("\n" + story_options[2])
                madlib_story_3()
            elif choice == 4:
                print("\n" + story_options[3])
                madlib_story_4()
            elif choice == 5:
                print("\n" + story_options[4])
                madlib_story_5()
            else:
                print("\nInvalid input. Please enter a number from 1 to 5 or 'q'.")

    print("\nThanks for playing Madlibs Mania - Come back soon for more wacky stories!")

    
choose_story()