import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import time

class playerDB:
    '''
    Contains all funcitons required for:
        1. Creating the database and table
        2. Scraping the Internet for player info
        3. Populating the table in database with player info
    '''

    def __init__(self):
        self.dbName = 'players/playerDB.db'
        self.connection = None
        self.cursor = None

    def connect(self):
        '''Connect to the database and set the cursor'''
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()

    def createTable(self):
        '''Create the "players" table'''
        self.cursor.execute("""CREATE TABLE players (
                            id INTEGER PRIMARY KEY,
                            playerId TEXT,
                            name TEXT,
                            teams TEXT)""")
        self.connection.commit()
        print("The 'players' table has been created...")

    def insertPlayer(self, playerId, name, teams):
        '''
        Insert the player info in the "players" table. Requires:
            1. playerId -> a alphanumerical code unique to each player
            2. name -> the full name of the player
            3. teams -> a list of all the teams the player has played for as a comma separated string
        '''
        self.cursor.execute(f"""INSERT INTO players (playerId, name, teams) VALUES ("{playerId}","{name}", "{teams}")""")
        self.connection.commit()
        print(f"Player {name} was added to 'players' database...")

    def scrapeAllPlayers(self):
        '''
        Scrape all players and their corresponding information required to populate the database. 
        Then insert the player and their info into the "players" table. 
        '''
        url1 = 'https://www.basketball-reference.com/players/' # website used to scrape data
        abc = 'abcdefghijklmnopqrstuvwyz' # all possible last name letters of current and past basketball players who have played in the NBA

        for letter in abc:
            tempUrl = url1 + letter + '/' # create the url for the page based on first initial of last name
            pageHtml = requests.get(tempUrl)
            soup = BeautifulSoup(pageHtml.text.encode(), 'html.parser')

            # Navigate to the desired table/information in the page
            table = soup.find('div', id='div_players')

            for player in table.find_all('tr'):
                playerID = re.sub('<a href="/players/./', "", str(player.a)) # clean playerID string
                playerID = re.sub('.html.*', "", playerID) 
                time.sleep(3.1) # as instructed by the websites admins, cannot send more then 20 requests a minute without getting IP banned. 
                if playerID != 'None':
                    print(f"Scraping for {playerID}...")  # if a player was found, scrape all the information for that player...
                    teamListStr, playerName = self.scrapePlayer(playerID)
                    print("...complete")
                    self.insertPlayer(playerID, playerName, teamListStr) # then add the information to the database table

        
            

    def scrapePlayer(self, playerId):
        """
        Given a specific players "playerId", navigate to the webpage containing thier information and 
        scrape all the teams that they have played for. Return the comma separated string of all the 
        teams they have played for as well as their full name.
        """
        letter = playerId[0] 
        teamList = []
        playerUrl = 'https://www.basketball-reference.com/players/' + letter + '/' + playerId + '.html'
        print(playerUrl)
        playerHtml = requests.get(playerUrl)
        soup = BeautifulSoup(playerHtml.text.encode(), 'html.parser')

        teamTable = soup.find('table', id='per_game')
        teamTable = teamTable.find('tbody')

        for row in teamTable.find_all('tr'):
            for i in row.find_all('td', class_='left'):
                if i.text not in teamList and i.text != 'NBA':
                    teamList.append(i.text) # if the team does not already exist in the list of teams, add it to the list

        playerName = soup.find('div', id='meta')
        playerName = playerName.h1.text # scrape the players full name
        print(f"{playerName} played for:\n{teamList}")

        teamListStr = ','.join(teamList) # change the list to a string

        print(teamListStr)


        return teamListStr, playerName


if __name__ == "__main__":     
    database = playerDB()
    database.connect()
    database.createTable()
    print(database.dbName)
    database.scrapeAllPlayers()
