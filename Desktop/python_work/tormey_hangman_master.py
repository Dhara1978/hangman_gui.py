###imports###
from tkinter import *
import tkinter.messagebox
import random

class mainWindow(object):
    def __init__(self,master):
        with open('hangman_words.txt', 'r') as f:
                self.words = f.readlines()
        
        #choose random word to guess in game
        self.guess_word = random.choice(self.words)
        self.words.remove(self.guess_word)
        
        #get rid of space at the end of the word
        self.guess_word = self.guess_word.strip()
        print(self.guess_word)

        #guess list
        self.guess_list = []
        self.no_lives = 7
        self.master=master
        self.master.wm_title("Hangman")
        Label(master, text = '   Hangman', font = ('Arial', 30)).grid(row = 0, column = 0, columnspan = 10)
        Label(master, text = ' ', font = ('Arial', 16)).grid(row = 1, column = 0, columnspan = 3)
        Label(master, text = 'Guess the word: ', font = ('Arial', 16)).grid(row = 2, column = 0, columnspan = 3, sticky = W)
        Label(master, text = 'Letters guessed: ', font = ('Arial', 16)).grid(row = 3, column = 0, columnspan = 3, sticky = W)
        Label(master, text = 'Lives remaining: ', font = ('Arial', 16)).grid(row = 4, column = 0, columnspan = 3, sticky = W)
        Label(master, text = str(self.no_lives), font = ('Arial', 16)).grid(row = 4, column = 3, sticky = W)
        Label(master, text = ' ', font = ('Arial', 16)).grid(row = 5, column = 0, columnspan = 3)
        Label(master, text = 'Enter guess: ', font = ('Arial', 16)).grid(row = 6, column = 0, columnspan = 3, sticky = W)
        self.display_guesses()
        self.display_word()
        self.guess_letter_input()

    #declaration of functions
    def letter_guess(self,letter):
        self.data = self.e.get()
        self.guess_list += self.data
        if self.data not in self.guess_word:
                        self.no_lives -= 1
                        if self.no_lives == 0:
                                        tkinter.messagebox.showinfo('tormey-hangman', 'you have lost')
                                        self.clear_data()                  
        Label(self.master, text = str(self.no_lives), font = ('Arial', 16)).grid(row = 4, column = 3, sticky = W)
        self.e.delete(0, 'end')
        self.display_word()
        self.display_guesses()

    def display_word(self):
        self.display_word_user = ''
        for i in self.guess_word.lower():
                        if i == ' ':
                                        self.display_word_user += ' '
                        elif i in self.guess_list:
                                        self.display_word_user += i
                        elif i not in self.guess_list:
                                        self.display_word_user += '*'

        Label(self.master, text = self.display_word_user, font = ('Arial', 16)).grid(row = 2, column = 3, columnspan = 7, sticky = W)

        if '*' not in self.display_word_user:
                        tkinter.messagebox.showinfo('tormey-hangman', 'Well done!\nYou have guessed correctly\nit was ' + self.guess_word)
                        self.clear_data()

    def display_guesses(self):
        self.wrong_guess = []
        for i in self.guess_list:
                        if i not in self.guess_word.lower():
                                        self.wrong_guess += i
        Label(self.master, text = self.wrong_guess, font = ('Arial', 16)).grid(row = 3, column = 3, columnspan = 7, sticky = W)

 

    def guess_letter_input(self):
        self.v = StringVar()
        self.e = Entry(self.master, textvariable = self.v)
        self.e.bind('<Return>', self.letter_guess)
        self.e.grid(row = 6, column = 3)

    def clear_data(self):
        tkinter.messagebox.showinfo('tormey-hangman', 'A new word will now be selected.')
        self.guess_word = random.choice(self.words)
        self.words.remove(self.guess_word)
        self.guess_word = self.guess_word.strip()
        self.letter_guess("")
        self.no_lives = 7
        self.guess_list = []
        self.wrong_guess = []
        self.display_word_user = ''
        Label(self.master, text = "                                          ", font = ('Arial', 16)).grid(row = 2, column = 3, columnspan = 7, sticky = W)
        Label(self.master, text = "                                          ", font = ('Arial', 16)).grid(row = 3, column = 3, columnspan = 7, sticky = W)
        Label(self.master, text = "                                          ", font = ('Arial', 16)).grid(row = 4, column = 3, sticky = W)

        for i in self.guess_word.lower():
                        if i == ' ':
                                        self.display_word_user += ' '
                        elif i in self.guess_list:
                                        self.display_word_user += i
                        elif i not in self.guess_list:
                                        self.display_word_user += '*'

        Label(self.master, text = self.display_word_user, font = ('Arial', 16)).grid(row = 2, column = 3, columnspan = 7, sticky = W)
        Label(self.master, text = self.wrong_guess, font = ('Arial', 16)).grid(row = 3, column = 3, columnspan = 7, sticky = W)
        Label(self.master, text = str(self.no_lives), font = ('Arial', 16)).grid(row = 4, column = 3, sticky = W)

       

if __name__ == "__main__":

    Hangman=Tk()
    Hangman_TOOL=mainWindow(Hangman)
    Hangman.mainloop() 
