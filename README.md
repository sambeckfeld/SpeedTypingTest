# SpeedTypingTest
A speed typing test for my final project

This is a speed typing test to check for accuracy and the time it took to finish typing

I have decided to use tkinter to build the bulk of my project

I created 3 buttons that all serve different functions. One to reset the word, one to submit the word, and one to reset the game

So far what I have done is...

The interface of the project including an image background using PIL from Pillow,
A function to get a new random word,
and a function that checks the word the user typed in,

What I don't have done is...

A function to check the spelling of the word typed in and seeing if it matches the word from my list,
A time function to give a clock,
And a function to reset the game,

I've started on the check_word function to check the spelling of the words but had trouble with running a few different things into the parameters.

Sources used so far to help create this project

https://www.youtube.com/watch?v=YXPyB4XeYLA

https://www.youtube.com/watch?v=ybpxJ_0B_Ms

# SpeedTypingTest Finished

I created a much simpler speed typing test using the destroy method to reset and start my game combined with my orignal project

I started by creating a screen called root
Inserting a background image using PIL
Creating a start button that calls on a function called begin
and a simple instruction label

I have 2 functions, one called begin and tthe other called results

Right away in the begin function I create an if statement that checks a global variable and if it is equal to 0, it destroys the original screen
This is a cheap way of making it possible to reset the game as many times as I want, if I dont include this if statement, It cannot destroy the original screen twice as it was already destroyed

I then create the second function called results
This function uses an if statement to check if the user entered the correct sentence presented to them.
If they are correct it prints a statement and ends a timer that tells you how fast you finished

Below this function I begin to create the second screen but before that I start a timer and create a list of sentences that will be randomly selected from using randint

I then create a new screen to replace "root" simply called "root2"
I re-add the backround image and create a label that pulls a random sentence from the list I created earlier

I then create an Entry for the user to type in the sentence, this will be used with .get in the results function

I then create 2 buttons that use the command feature to link them to the functions, One button that submits the sentence using the results as a command
and another button that uses the begin function to bring up another screen with a new sentence

The result and print statements are put into the console which is something I wish I could've got working into a label but could not figure out how to replace labels rather then destroy
