import tkinter as tk
from tkinter import ttk
import random
import math
# Defines the Starting App where you choose difficultys 
class start_App():
    def __init__(self):
        #The window gets defined as root and given a title and size
        self.root = tk.Tk()
        self.root.title("Minesweeper by Oluf")

        self.root.geometry("250x300")
        # a Button to start the game a list that contains the difficultys adn a combo to choose from the list are created
        self.start_button = ttk.Button(self.root,text="start",command=self.start_game)
        self.difficultys = ["difficulty 1", "difficulty 2","difficulty 3","difficulty 4"]
        self.choose_difficulty = ttk.Combobox(self.root,values=self.difficultys)
        
        # The windows and the button/combobox are placed onto the window which is put in mainloop
        self.choose_difficulty.place(x=65,y=100,width=120)
        self.start_button.place(x=75,y=200,width=100,height=50)
        
        self.root.mainloop()

    # this function will happen after the start button is pressed where it gets the difficultys and starts the new function
    def start_game(self):
        global diff
        diff = self.difficultys.index(self.choose_difficulty.get())
        self.root.quit()
        
        
        


####################################################################################################
####################################################################################################
####################################################################################################

# The main App
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper by Oluf")
        self.pressed = []
        self.root.geometry("700x700")
        print(diff+1)
        mines = {
            1: (9 * 9, 10),
            2: (16 * 16, 40),
            3: (30 * 16, 99),
            4: (50 * 50, 500)
        }
        self.ratio = mines[diff+1]
        self.genreate_mines()
        self.generate_minefield()
        
        
        
        self.root.mainloop()
    
    def genreate_mines(self):
        all_positions = [(x, y) for x in range(int(math.sqrt(self.ratio[0]))) for y in range(int(math.sqrt(self.ratio[0])))]
        self.mine_pos = set(random.sample(all_positions, self.ratio[1]))  # Store as a set for fast lookup
        print(self.mine_pos)
        
    def check_mine(self, x, y, button):
        # If the button was not pressed already, change the button color
        if (x, y) not in self.pressed:
            button.config(fg="red", bg="red")  # Change button color to red
            self.pressed.append((x, y))
        elif (x, y) in self.mine_pos:
            print("You pressed a mine!")
        else:
            # Call check_surroundings to check for neighboring mines
            mines = self.check_surroundings(x, y)
            if mines == 0:
                button.destroy()  # Remove button if no surrounding mines
                del self.buttons[(x, y)]  # Remove the button from the dictionary
                for ax in range(-1, 2):  # Loop through neighboring coordinates
                    for ay in range(-1, 2):
                        if ax == 0 and ay == 0:  # Skip the current button
                            continue
                        # Check if the neighboring coordinates are in the button dictionary
                        if (x + ax, y + ay) in self.buttons:
                            self.pressed.append((x + ax, y + ay))
                            # Get the neighboring button and pass it to the check_mine function
                            self.check_mine(x + ax, y + ay, self.buttons[(x + ax, y + ay)])
            else:
                # If there are surrounding mines, show the count on the button
                button.config(fg="black", bg="white", text=f"{mines}")

    def check_surroundings(self, x, y):
        minecounter = 0
        for ax in range(-1, 2):  # Loop through surrounding coordinates
            for ay in range(-1, 2):  # Loop through surrounding coordinates
                 if (x + ax, y + ay) in self.mine_pos:  # Check if there's a mine in the neighboring cell
                    print(f"Mine at ({x + ax}, {y + ay})")
                    minecounter += 1
        return minecounter
    
    
    def generate_minefield(self):
        print(self.ratio[0])
        self.buttons = {}
        size = int(math.sqrt(self.ratio[0]))
        btn_size = 700 / size
        ax = 0
        ay = 0
        for x in range(0, 700, int(btn_size)):
            for y in range(0, 700, int(btn_size)):

                btn = tk.Button(self.root)
                self.buttons.update({(ax, ay): btn})

                # Use default arguments in lambda to capture ax, ay, and btn
                btn.config(command=lambda x=ax, y=ay, b=btn: self.check_mine(x, y, b))
                btn.place(x=x, y=y, width=btn_size, height=btn_size)
                ay += 1
            ax += 1
            ay = 0
#checks if we are running this from main so we don't accidentally run this program twice
if __name__ == "__main__":
    start_App()
    App()