import tkinter as tk
from tkinter import messagebox
import game.gameLogic as gameLogic
import game.inputNormalization as norm

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create the tkinter window
        self.title("NBA Grid Game Guesser")
        self.buttons = []
        self.geometry('750x400')

        # Used to keep track of the row and column that the user has chosen
        self.chosenRow = None
        self.chosenCol = None

        # Initialize the autocomplete search box
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.autocomplete)

        self.entry = tk.Entry(self, state=tk.DISABLED,textvariable=self.search_var)
        self.entry.grid(row=1, column=4, padx=5, pady=5)

        # Initialize the enter button, should be disabled until a user choses a box (row/column pair)
        self.enterButton = tk.Button(self, text="Enter", command=self.makeGuess, state=tk.DISABLED)
        self.enterButton.grid(row=1, column=5, padx=5, pady=5)

        # Create and configure autocomplete listbox
        self.autocompleteListbox = tk.Listbox(self, width=25, height=10)
        self.autocompleteListbox.grid(row=2, column=4, padx=5, pady=5, rowspan=3)
        self.autocompleteListbox.bind("<<ListboxSelect>>", self.onAutocompleteSelect)
        self.autocompleteListbox.grid_forget()  # Initially hide the listbox

        # Create instance of the game logic
        self.game = gameLogic.Game()

        # Generate the teams that will be on the rows and columns of the game
        self.teamRowList , self.teamColList = self.game.gameStart()

        # Initialize the window based on the teams that have been randomly selected
        self.setupGameWindow()

        # Set the players lives and score
        self.lives = 3
        self.score = 0



    def setupGameWindow(self):
        '''
        Create buttons and configure the game window
        '''

        for col in range(3): # Populate the columns with the teams
            label = tk.Label(self, text=norm.convertCodeToFull(self.teamColList[col]))
            label.grid(row=1, column=col+1, padx=5, pady=5)

        for row in range(3): # Populate the rows with the teams
            label = tk.Label(self, text=norm.convertCodeToFull(self.teamRowList[row]))
            label.grid(row=row+2, column=0, padx=5, pady=5)

            rowButtons = []
            # Create and place all the player buttons on the window
            for col in range(3):
                button = tk.Button(self, text=" ", width=10, height=5,
                                   command=lambda r=row, c=col: self.buttonClick(r, c))
                button.grid(row=row+2, column=col+1, padx=5, pady=5)
                rowButtons.append(button)
            self.buttons.append(rowButtons)
        

    def buttonClick(self, row, col):
        '''
        Handle the button click event.
        '''
        self.entry.config(state=tk.NORMAL)  # Enable the entry box
        self.entry.delete(0, tk.END)  # Clear any previous text
        self.entry.focus()  # Set focus to the entry box
        self.chosenRow = row # Update the row and column of the chosen button
        self.chosenCol = col
        # print(self.chosenRow)
        # print(self.chosenCol)
        
        self.enterButton.config(state=tk.NORMAL)  # Enable the enter button
        self.autocompleteListbox.grid(row=2, column=4, padx=5, pady=5, rowspan=3)
        self.autocompleteListbox.delete(0,tk.END) # Clear the autocomplete suggestions


    def makeGuess(self):
        playerName = self.entry.get()
        if playerName:
            print(f"Player name: {playerName}")
            result, output = self.game.choiceMade(playerName, self.teamRowList[self.chosenRow], self.teamColList[self.chosenCol])
            print(output)
            if result == True:
                self.score +=1
                self.buttons[int(self.chosenRow)][int(self.chosenCol)].config(state=tk.DISABLED, bg='green')
                if self.score == 9:
                    messagebox.showinfo('WOW!', 'You won the game with a perfect score, AMAZING!')
                    self.destroy()
            else:
                self.buttons[int(self.chosenRow)][int(self.chosenCol)].config(state=tk.DISABLED, bg='red')
                self.lives -= 1
                if self.lives == 0:
                    messagebox.showinfo('Game Over, you lost', f"Your score was: {self.score}")
                    self.destroy()

        self.entry.delete(0, tk.END)  # Clear the entry box
        self.entry.config(state=tk.DISABLED)  # Disable the entry box
        self.enterButton.config(state=tk.DISABLED)  # Disable the enter button
        self.autocompleteListbox.grid_forget()


    
    def autocomplete(self, *args):
        
        userInput = self.search_var.get()
        matchingNames = self.game.autocomplete(userInput)

        self.autocompleteListbox.delete(0, tk.END)
        for name in matchingNames[:5]:
            self.autocompleteListbox.insert(tk.END, name)

        if matchingNames:
            self.autocompleteListbox.grid(row=2, column=4, padx=5, pady=5)
        else:
            self.autocompleteListbox.grid_forget()



    def onAutocompleteSelect(self, event):
        selectedIndex = self.autocompleteListbox.curselection()
        if selectedIndex:
            selectedName = self.autocompleteListbox.get(selectedIndex[0])
            self.search_var.set(selectedName)
            self.autocompleteListbox.grid_forget()
        

if __name__ == '__main__':
    gameWindow = GameWindow()
    gameWindow.mainloop()


