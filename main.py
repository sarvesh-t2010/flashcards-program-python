import random
final_flashcards = []
repeat_flashcards = []
repeat_count = 0
saved_flashcards = []

"""
To do:
Linear regression prediction model of how much more time you'd have to spend
timer module and estimated time to memorise
Graph
documentation
comments
formatting
"""

while True:
    try:
        file_path = str(input("Enter the path of your .txt file of your flashcards: "))
        with open(file_path, "r", encoding="utf-8") as f:
            flashcard_data = f.read()
        break
    except:
        print("That is not a valid path!")
        continue


seperated_flashcards = flashcard_data.split('\n')
while True:
    print("1) Bar spacing (question|answer)\n2) semicolon spacing (question;answer)\n3) tab spacing (question   answer)")
    spacing_type = input("What spacing type does your flashcards use? (enter the corresponding number):")
    if spacing_type == "1":
        spacing_type = "|"
        break
    elif spacing_type == "2":
        spacing_type = ";"
        break
    elif spacing_type == "3":
        spacing_type = "    "
        break
    else:
        print("Thats not a valid answer! Type 1, 2, or 3!")
        continue

for i in range(len(seperated_flashcards)):
    final_flashcards.append(seperated_flashcards[i].split(spacing_type))



random.shuffle(final_flashcards)

while True:
    for j in range(2):
        for i in range(len(final_flashcards)):
            print("")
            print(final_flashcards[i][0])
            while True:
                known_var = str(input("Do you know the answer to this? (Yes or No): "))
                known_var = known_var.strip()
                if known_var == "yes" or known_var == "Yes":
                    print("Great work!")
                    break
                elif known_var == "no" or known_var == "No":
                    repeat_flashcards.append(final_flashcards[i])
                    print("That's okay! Practice makes perfect!")
                    break
                else:
                    print("Thats an invalid input! Say Yes or No!")
        
        print("\nHere is the answer to '" + final_flashcards[i][0] + "':")
        print(final_flashcards[i][1])

    final_flashcards = []
    final_flashcards = repeat_flashcards
    repeat_flashcards = []
    if len(final_flashcards) < 1:
        print("Nice work! You memorised all your flashcards!")
        break
    else:
        print("\nYou have a few more flashcards left to memorise! Repeating cards left to memorise...")
        continue

