import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time
#make sure to install all the modules


#Variable to change how many times the flashcards repeat before collecting missed cards and making the user repeat again
repeat_card = 2

#Lists and variable definition
final_flashcards = []
repeat_flashcards = []
repeat_count = 1
session_start_time = 0
session_end_time = 0
saved_flashcards = []
unique_list = []
repeat_list = []
original_cards = []
correct_answers = []

#Function for linear regression model and graphing it
def model(x, y):
    x_coord = np.array(x).reshape(-1, 1) #get function values then reshape them into something linear regression can understand
    y_coord = np.array(y)

    model = LinearRegression() #do the linear regression model
    model.fit(x_coord, y_coord) #do linear regression model on list of coords

    y_pred = model.predict(x_coord) #find like the middle between all the points for the regression graph to go through

    next_x = np.array([[x[-1] + 1]]) #x value plus 1 basically
    next_y = round(model.predict(next_x)[0]) #prediction of next point
    if next_y > len(final_flashcards):
        next_y = len(final_flashcards)
    plt.scatter(x_coord, y_coord, label="Real data") #graph points of real data
    plt.plot(x_coord, y_pred, color='red', label="Regression line") #graph linear regression line

    plt.scatter(next_x, next_y, color='green', label='Next prediction') #graph the prediction for the amount of cards user might get right

    textstr = f"Next Predicted correct answer count = {next_y:.2f}" #display predicted answer amount
    plt.gca().text( #formatting
        0.05, 0.95, textstr,
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',

    )

#plot graph
    plt.title("Predicted Time to Study")
    plt.xlabel("Times flashcards were repeated (seconds)")
    plt.ylabel("Times Answer was known")
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(5)
    plt.clf()



#Introduction/watermark
print("⣿⣿⣿⣿⣿⠟⠁⣠⣶⣦⣤⣶⣶⣶⣶⣤⣀⣀⣀⣈⠉⠁⣤⣤⣄")
print("⣿⣿⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢀⣼⣿⠿")
print("⣿⣿⣿⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠐⠈⢁⣀")
print("⣿⣿⠇⢀⣿⡿⠿⠛⠋⠉⠉⠉⢀⢀⣀⣀⣠⣤⣼⣷⣾⣿⣿⡿")
print("⠿⠏⢀⡾⢀⢀⣀⣀⣠⣤⣶⡶⠞⣿⣿⣉⡟⣬⢙⠿⣿⣿⠏⠁⣰")
print("⣤⣤⡴⣷⠛⣿⣿⣿⣿⣿⣿⠇⢀⠙⠻⢿⣿⣧⡾⠶⢻⠛⢀⣼⣿")
print("⠘⠻⢶⣯⡝⢠⣍⣻⣿⣿⠋⢀⢀⢀⢀⢀⢀⢀⢀⢀⡿⢀⣼⣿⣿")
print("⢀⢀⢀⠙⣟⠋⠉⠉⢀⢀⠠⠴⠖⠛⠉⢀⢀⢀⢀⣼⠁⣰⣿⣿⣿")
print("⢀⢀⢀⢀⠈⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⠞⠁⣠⣿⣿⣿⣿")
print("⢀⢀⢀⢀⣠⣀⠈⠓⠦⣄⣀⣀⣀⣀⣤⣴⣾⠁⢠⣾⣿⣿⣿⣿⣿")
print("⢀⢀⢀⣸⣿⣿⣿⣦⣄⢀⢹⣿⣿⣿⣿⣿⣿⡆⠈⣿⣿⣿⣿⣿⣿")
print("⢀⢀⣼⣿⣿⣿⣿⣿⡏⢀⢸⣿⣿⣿⣿⣿⣿⣷⢀⢻⣿⣿⣿⣿⡟")
print("⢀⠘⠛⠛⠛⠛⠛⠛⢀⢀⠘⠛⠛⠛⠛⠛⠛⠛⠃⢀⠛⠛⠛⠛")
print("𝑺𝒂𝒓𝒗𝒆𝒔𝒉 𝑻𝒉𝒊𝒂𝒈𝒂𝒓𝒂𝒋𝒂𝒏 𝑷𝒓𝒆𝒔𝒆𝒏𝒕𝒔")
print("Awesome flashcard app 5000")
print("------------------------------------------")
print("Remember, make sure to run this on your computer's console so that the linear regression graph shows up and please make sure you read the readme.md for help!")
while True: 
    try:
        file_path = str(input("------------------------------------------\nEnter the path of your .txt file of your flashcards: ")) #find and read path
        with open(file_path, "r", encoding="utf-8") as f:
            flashcard_data = f.read()
        break
    except:
        print("Error! That is not a valid path or your file type isn't a .txt!")
        continue

seperated_flashcards = flashcard_data.split('\n') 

# Ask user for seperation type and seperate cards accordingly
while True:    
    while True:
        print("------------------------------------------\n1) Bar spacing (question|answer)\n2) semicolon spacing (question;answer)\n3) dash spacing (question-answer) \n4) tab spacing (question \t answer)")
        spacing_type = input("What spacing type does your flashcards use? (enter the corresponding number):")
        if spacing_type == "1":
            spacing_type = "|"
            break
        elif spacing_type == "2":
            spacing_type = ";"
            break
        elif spacing_type == "3":
            spacing_type = "-"
            break
        elif spacing_type == "4":
            spacing_type = "\t"
        else:
            print("Thats not a valid answer! Type 1, 2, 3 or 4!")
            continue

    for i in range(len(seperated_flashcards)):
        final_flashcards.append(seperated_flashcards[i].split(spacing_type))
    try:
        for i in range(len(final_flashcards)):
            test = final_flashcards[i][1]
        break
    except:
        print("\nError! Your flashcards are formatted incorrectly, make sure you chose the correct spacing type and refer back to the readme.md explaining how to properly put files in here!")
        continue

print("------------------------------------------\nOpening flashcards...\n------------------------------------------")

original_cards = final_flashcards

#card shuffle and display script
random.shuffle(final_flashcards)
session_start_time = time.time()
while True:
    for j in range(repeat_card):
        for i in range(len(final_flashcards)):
            print("")
            print(final_flashcards[i][0])
            while True:
                known_var = str(input("\n\n\n\n------------------------------------------\nDo you know the answer to this? (Yes or No): "))
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
        
            print("------------------------------------------\n\nHere is the answer to '" + final_flashcards[i][0] + "':")
            print(final_flashcards[i][1])
            print("\n\n\n\n------------------------------------------")
        
        random.shuffle(final_flashcards)
    #reset flashcards with new deck with cards user had trouble with    
    
    final_flashcards = []
    final_flashcards = repeat_flashcards
    repeat_flashcards = []
    unique_list = []
    for i in final_flashcards:
        if i not in unique_list:
            unique_list.append(i)
    
    final_flashcards = unique_list

    if len(final_flashcards) < 1:
        print("Nice work! You memorised all your flashcards!\n------------------------------------------")
        break
    else:
        print("You have " + str(len(final_flashcards))+ " more flashcards left to memorise! Repeating cards left to memorise...\n------------------------------------------")
        
        #display regression model after 2 repitions
        repeat_count = repeat_count + 1
        repeat_list.append(repeat_count)
        correct_answers.append((len(original_cards))-(len(final_flashcards)))
        if repeat_count > 1:
            print("Creating linear regression graph of predicted your correct answers!\n------------------------------------------")
            model(repeat_list, correct_answers)
         
        continue

session_end_time = time.time()

session_total_time = session_end_time - session_start_time
print("\nYou spent " + str(round(session_total_time/60, 2)) + " minutes studying!")
print("Good luck on whatever you are studying for!")

