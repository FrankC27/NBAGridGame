import sqlite3
import random
import game.constants as constants
import game.inputNormalization as norm

class Game():
    def __init__(self):
        super().__init__()
        self.teamsList = list(constants.teamCodeToFull.keys())

        self.rows, self.cols = self.gameStart()   
        self.dbName = 'players/playerDB.db'
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor() 
        
        self.player_names = self.fetchAllNames()


    def fetchAllNames(self):
         '''
         Get all the players names from the database
         '''
         self.cursor.execute('''Select * FROM players''')
         respone = self.cursor.fetchall()

         return [row[2].strip() for row in respone]
    
    def autocomplete(self, userInput):
        '''
        Given a string, return all the names that match the input
        '''
        matchingNames = [name for name in self.player_names if name.lower().startswith(userInput.lower())]
        return matchingNames
    
    def gameStart(self):
        '''
        Start a new game, randomly select the teams to populate the rows and columns of the game
        '''

        rows = []
        cols = [] 

        rows = random.sample(self.teamsList, 3) # Get 3 teams to populate the rows
        # print(rows)
        
        remainingTeams = [team for team in self.teamsList if team not in rows] # Determine which teams were not chosen
        cols = random.sample(remainingTeams, 3) # Get 3 teams to populate the columns that have not already been chosen for the rows

        print(f"Rows: {rows}")
        print(f"Columns: {cols}")

        # return the col and row teams
        return rows, cols
    

    def choiceMade(self, player, team1, team2):
        '''
        Given a player name and two teams, determine if the player has played for both of the teams,
        if so, return True, if not, return False
        '''

        # Check to see if the player exists in the player database
        print(f"Searching Database for {player}")
        self.cursor.execute('''SELECT * FROM players WHERE name LIKE ?''', ('\n' + player + '\n',))
        response = self.cursor.fetchall()
        # if not found in the database, return a message saying that the player name was spelt wrong
        if not response or len(response) == 0:
                return False, "Player name was spelt wrong"

        # if found in the database, check to see how many there were
        else: 
            print("Players found: ",len(response))
            # for each player in the player database that matches the player choice made, check to see if the player played on both team1 and team2
            for p in response:
                teams = p[3].split(',')
                count = 0
                for t in teams:
                    teams[count] = norm.normalizeTeamCode(t) # Ensure that any team name for one franchise is treated as the same
                    count +=1
                    
                print(teams)

                # if there is a player who played on both teams that matches the name, then return True 
                if team1 in teams and team2 in teams:
                    return True, "Correct"

                # otherwise, return false
                return False, "Incorrect"
            
if __name__ == '__main__':
    game = Game()
    user_input = input("Enter a player name: ")
    matching_names = game.autocomplete(user_input)
