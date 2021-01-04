from tkinter import *
from PIL import ImageTk,Image
from timeit import default_timer as timer
import random

#setting a variable for restarting the test
x=0

#creating the main screen for starting the game
root = Tk()
root.title("A Writing Test")
root.geometry("500x200")

#function for beginning the test

def begin():

#using the variable to make it possible to destroy the original screen and root2 screens(the second screen created when the start button is clickeed)
    global x
    if x==0:
        root.destroy()
        x=x+1

#checking the results using .get to get what the user entered and to check it across the word selected randomly and ending the timer
    def results():
        if entry.get()==words[word]:
            end=timer()
            
            print("You finished in " + str(end-start) + " seconds!")
        else:
            print("Wrong Answer Try again, check your spelling")

#creating a list of sentences and randomly selecting from it
    words = ["typing starts here for always", "terrible is the man who falls", "dunking is for the best of the players", "tugging is used in tug of war", "hippo's seem to love the water"]
    word=random.randint(0,(len(words)-1))

#starting the timer
    start=timer()

#creating a new screen to replace the main when start button is clicked and root.destroy is called on
    root2 = Tk()
    root2.title("A Writing Test")
    root2.geometry("500x200")

#adding a background image
    my_img = ImageTk.PhotoImage(Image.open("bimg.jpg"))
    my_Label = Label(image=my_img)
    my_Label.pack()

#adding a label that shows the word randomly selected
    wordLabel = Label(root2, text=words[word], bg="yellow")
    wordLabel.place(x=275, y=45)

#creating an instruction label
    label1 = Label(root2, text="How fast can you type this word?")
    label1.place(x=50, y = 40)

#creating an entry for the user to type in
    entry=Entry(root2)
    entry.place(x=225, y=80)

#creating 2 buttons with commands attached to the functions above
    chButton = Button(root2, text="Submit", command=results)
    chButton.place(x=225, y=120)

    reButton = Button(root2, text="Restart?", command=begin)
    reButton.place(x=150, y=120)

    root.mainloop()

#adding an image to use as a background using ImageTk from Pillow which used PIL
my_img = ImageTk.PhotoImage(Image.open("bimg.jpg"))
my_Label = Label(image=my_img)
my_Label.pack()

#adding a starting label requesting the user to click a button to begin
stLabel = Label(root, text="Click Start to Begin the Test", bg="yellow", width=20, height=3)
stLabel.place(x=170, y=25)

#adding a starting button
stButton = Button(root, text="Start", command=begin, width=14, bg='grey')
stButton.place(x=185, y=85)



root.mainloop()
