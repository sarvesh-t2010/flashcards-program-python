import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time

final_flashcards = []
repeat_flashcards = []
repeat_count = 1
start_time = 0
end_time = 0
total_time = []
session_start_time = 0
session_end_time = 0
saved_flashcards = []
unique_list = []
repeat_list = []


"""
To do:
Linear regression prediction model of how much more time you'd have to spend
timer module and estimated time to memorise
Graph
documentation
comments
formatting
"""


def model(x, y):
    x_coord = np.array(x).reshape(-1, 1)
    y_coord = np.array(y)

    model = LinearRegression()
    model.fit(x_coord, y_coord)

    y_pred = model.predict(x_coord)

    plt.scatter(x_coord, y_coord, label = "real data", marker = 'o')
    plt.plot(x_coord, y_pred, color = 'red', label = "Predicted time to memorise")
    plt.title("Predicted time to study")
    plt.xlabel("Times flashcards were repeated")
    plt.ylabel("Time taken to complete")
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5)
    plt.clf()



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
session_start_time = time.time()
while True:
    start_time = time.time()
    for j in range(2):
        for i in range(len(final_flashcards)):
            print("")
            print(final_flashcards[i][0])
            while True:
                known_var = str(input("Do you know the answer to this? (Yes or No): "))
                known_var = known_var.strip()
                known_var = known_var.lower()
                if known_var == "yes":
                    print("Great work!")
                    break
                elif known_var == "no":
                    repeat_flashcards.append(final_flashcards[i])
                    print("That's okay! Practice makes perfect!")
                    break
                else:
                    print("Thats an invalid input! Say Yes or No!")
        
            print("\nHere is the answer to '" + final_flashcards[i][0] + "':")
            print(final_flashcards[i][1])
        
        random.shuffle(final_flashcards)
        
    
    final_flashcards = []
    final_flashcards = repeat_flashcards
    repeat_flashcards = []
    unique_list = []
    for i in final_flashcards:
        if i not in unique_list:
            unique_list.append(i)
    
    final_flashcards = unique_list

    if len(final_flashcards) < 1:
        print("Nice work! You memorised all your flashcards!")
        break
    else:
        print("\nYou have " + str(len(final_flashcards))+ " more flashcards left to memorise! Repeating cards left to memorise...")
        
        repeat_count = repeat_count + 1
        repeat_list.append(repeat_count)
        end_time = time.time()
        total_time.append(round(end_time-start_time, 2))
        if repeat_count > 2:
            model(repeat_list, total_time)
        continue

session_end_time = time.time()

session_total_time = session_end_time - session_start_time
print("\nYou spent " + str(round(session_total_time/60, 2)) + " minutes studying!")

