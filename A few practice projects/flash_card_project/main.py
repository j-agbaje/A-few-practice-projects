from tkinter import *
import pandas
import random

# Background color for the application
BACKGROUND_COLOR = "#B1DDC6"

# Try to load the words to learn from a CSV file,
# if not found, load from the original French words file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    # Load default words if 'words_to_learn.csv' is not found
    data = pandas.read_csv("./data/french_words.csv")
    word_list = data.to_dict(orient="records")  # Convert to list of dictionaries
    index = random.choice(range(len(word_list)))  # Randomly select an index
else:
    word_list = data.to_dict(orient="records")
    # Check if the word list is empty, if so, load from the default file
    if word_list:
        index = random.choice(range(len(word_list)))
    else:
        data = pandas.read_csv("./data/french_words.csv")
        word_list = data.to_dict(orient="records")
        index = random.choice(range(len(word_list)))


# Function to change the current word on the flashcard
def change_word():
    global word
    global index
    global word_list

    # Remove the current word from the list
    word_list.remove(word_list[index])
    index = random.choice(range(len(word_list)))  # Choose a new random index

    # Get the new French word
    new_french_word = word_list[index]['French']
    canvas.itemconfig(language, text='French', fill='black')  # Set language text
    canvas.itemconfig(word, text=new_french_word, fill='black')  # Set the new word

    # Update the flashcard background to French side
    canvas.itemconfig(create_card_background, image=french_word_image)

    # Schedule the change to the English word after 5 seconds
    window.after(5000, lambda: change_card(index))

    # Save the updated word list to 'words_to_learn.csv'
    new_data = pandas.DataFrame(word_list, columns=('French', 'English'))
    new_data.to_csv('words_to_learn.csv', index=False)


# Function to flip the card and show the English translation
def change_card(index_no):
    # Change the flashcard background to English side
    canvas.itemconfig(create_card_background, image=english_word_image)

    # Get the English word corresponding to the current French word
    new_eng_word = word_list[index_no]['English']
    canvas.itemconfig(word, text=new_eng_word, fill="white")  # Set the English word
    canvas.itemconfig(language, text='English', fill="white")  # Set language text


# Initialize the main window
window = Tk()
window.title("French Flashcards")
window.config(bg=BACKGROUND_COLOR, width=1000, height=1000, padx=200, pady=200)

# Create the canvas for displaying the flashcards
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Load images for the front and back of the flashcards
french_word_image = PhotoImage(file='./images/card_front.png')
english_word_image = PhotoImage(file='./images/card_back.png')

# Add the initial card background (French side)
create_card_background = canvas.create_image(400, 263, image=french_word_image)

# Add text elements for the language and word
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
new_word = word_list[index]['French']  # Get the initial French word
word = canvas.create_text(400, 263, text=new_word, font=('Ariel', 60, 'bold'))

# Place the canvas on the window grid
canvas.grid(row=0, column=0, columnspan=2)

# Schedule the first card flip after 3 seconds
window.after(3000, lambda: change_card(index))

# Load images for the "wrong" and "right" buttons
button_wrong_image = PhotoImage(file='./images/wrong.png')
button_right_image = PhotoImage(file='./images/right.png')

# Create and place the "wrong" button
wrong_button = Button(image=button_wrong_image, highlightthickness=0, command=change_word)
wrong_button.config(width=100, height=100, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0, padx=50, pady=50)

# Create and place the "right" button
right_button = Button(image=button_right_image, highlightthickness=0, command=change_word)
right_button.config(width=100, height=100, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1, padx=50, pady=50)

# Start the Tkinter event loop
window.mainloop()
