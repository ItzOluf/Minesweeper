import tkinter as tk
from tkinter import ttk
import random

# Defines the Starting App where you choose difficultys 
class start_App():
    def __init__(self):
        #The window gets defined as root and given a title and size
        self.root = tk.Tk()
        self.root.title="MInesweeper by Oluf"
        self.root.geometry("250x300")
        # a Button to start the game a list that contains the difficultys adn a combo to choose from the list are created
        self.start_button = ttk.Button(self.root,text="start",command=self.start_game)
        self.difficultys = ["difficulty 1", "difficulty 2","difficulty 3","difficulty 4","difficulty 5"]
        self.choose_difficulty = ttk.Combobox(self.root,values=self.difficultys)
        
        # The windows and the button/combobox are placed onto the window which is put in mainloop
        self.choose_difficulty.place(x=65,y=100,width=120)
        self.start_button.place(x=75,y=200,width=100,height=50)
        
        self.root.mainloop()

    # this function will happen after the start button is pressed where it gets the difficultys and starts the new function
    def start_game(self):
        diff = self.choose_difficulty.get()
        


####################################################################################################
####################################################################################################
####################################################################################################

# The main App
class App():
    def __init__(self):
        pass


#checks if we are running this from main so we don't accidentally run this program twice
if __name__ == "__main__":
    start_App()
    App()