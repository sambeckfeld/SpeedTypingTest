from tkinter import *
from PIL import ImageTk,Image
import random


def reset_word():
    
    word=random.randint(0,(len(words)-1))
    
    
    wordLabel = Label(text=words[word] + str("     "))
    wordLabel.place(x=225, y=70)  

def submit_word():
    typedWord = sent.get()
    

    #check_word(typedWord)
    print(typedWord)
    
"""def check_word(typedWord):

    word = word.split()
    count = len(word)
    
    typedWord = typedWord.split()
    for letter in typedWord:
        if(typedWord[0] != word[0]):
            count -= 1
        word.pop(0)
        typedWord.pop(0)

    print(count)"""
            
    
#creating the screen using tkinter
#setting the size with geometry
root = Tk()
root.title("A Writing Test")
root.geometry("500x200")

#adding an image to use as a background using ImageTk from Pillow which used PIL
my_img = ImageTk.PhotoImage(Image.open("bimg.jpg"))
my_Label = Label(image=my_img)
my_Label.pack()

#creating a label to tell the user what to do
#placing all label's and buttons with "place"
label = Label(root, text="Type the Sentence Below!")
label.place(x=170, y=25)

#creating an text input box using Entry
sent = Entry(root, width=40, borderwidth=5)
sent.place(x=130, y=100)

#creating a button to enter in the sentence typed
but1 = Button(root, text="Submit!", command= submit_word)
but1.place(x=245, y=150)

#creating a new sentence button
but2 = Button(root, text="Reset Game")
but2.place(x=120, y=150)

#creating a button for reseting the sentence
but3 = Button(root, text="New Word", command = reset_word)
but3.place(x=350, y=150)


#creating a list of words called "words"
#creating a new variable named word that is randomly selecting from the list
words = ["typing", "terrible", "dunking", "tugging", "hippo"]



word=random.randint(0,(len(words)-1))

wordLabel = Label(text=words[word])
wordLabel.place(x=225, y=70)


  






#runnning root in a loop
root.mainloop()



