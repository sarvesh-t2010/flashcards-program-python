Welcome to Sarvesh's awesome flashcard program


**install dependencies**
- Install the following dependencies by running this command in your console: `pip install numpy matplotlib scikit-learn`

**How to input flashcards**
- First, put "main.py" in a folder
- Then go onto quizlet and choose one of your own flashcards (for testing purposes, I have provided an example flashcard deck)
- click export flashcard by clicking the 3 dots and selecting export
- set the "Between term and definition" to "custom" and type "|"
- Set the between rows option to new line
- Now copy the text it gave you
- Create a .txt file, name it whatever you want and make sure its in the same folder as main.py
- paste the test quizlet gave you into this txt and save

**Important details**
- Make sure that the flashcard doesnt have any lines with nothing on it and stay consistent with the question and answer spacing type
- run the code with python main.py in the console
- use a windows pc as otherwise the linear regression graph wont be displayed

**General information**
- This program repeats cards you didn't know and will repeat the entire deck twice before only repeating the cards you got wrong
- After 2 repitions, the linear regression model will be created for you to see how well you are getting your cards right and what the prediction of cards is going to be next.
