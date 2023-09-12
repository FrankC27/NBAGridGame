# Team Name Mapping

# Dictionary containing keys for every possible team code and their corresponding value 
# as the team code to be normalized too
teamNames = {

    # Atlanta Hawks
    "ATL": "ATL",
    "STL": "ATL",
    "MLH": "ATL",

    # Boston Celtics
    "BOS": "BOS",

    # Brooklyn Nets
    "NJN": "NJN",
    "NYN": "NJN",
    "BRK": "NJN",

    # Charlotte Hornets
    "CHA": "CHA",
    
    # Chicago Bulls
    "CHI": "CHI",

    # Clevland Cavaliers
    "CLE": "CLE",

    # Dallas Mavericks
    "DAL": "DAL",

    # Denver Nuggets
    "DEN": "DEN",

    # Detroit Pistons
    "DET": "DET",

    # Golden State Warriors 
    "GSW": "GSW",
    "SFW": "GSW",

    # Houston Rockets
    "HOU": "HOU",
    "SDR": "HOU",

    # Indiana Pacers
    "IND": "IND",

    # Los Angeles Clippers
    "LAC": "LAC",
    "SDC": "LAC",

    # Los Angeles Lakers
    "LAL": "LAL",

    # Memphis Grizzlies 
    "MEM": "MEM",
    "VAN": "MEM",

    # Miami Heat
    "MIA": "MIA",

    # Milwake Bucks 
    "MIL": "MIL",

    # Mississota Timberwolves 
    "MIN": "MIN",

    # New Orleans Pelicans 
    "NOH": "NOH",
    "NOP": "NOH",

    # New York Knicks 
    "NYK": "NYK",

    # Oklahoma City Thudner 
    "OKC": "OKC",
    "SEA": "OKC",

    # Orlando Magic
    "ORL": "ORL",

    # Philadelphia 76ers
    "PHI": "PHI",

    # Phoenix Suns
    "PHO": "PHO",

    # Portland Trail Blazers
    "POR": "POR",

    # Sacramento Kings 
    "SAC": "SAC",
    "KCK": "SAC",

    # San Antonio Spurs
    "SAS": "SAS",

    # Toronto Raptors
    "TOR": "TOR",

    # Utah Jazz 
    "UTA": "UTA",

    # Washington Wizards 
    "WAS": "WAS",
    "CAP": "WAS",
    "BAL": "BAL"
}

# Used to convert team code to the actual name of the team
teamCodeToFull = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "NJN": "Brooklyn Nets",
    "CHA": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers", 
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOH": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philidelphia 76ers",
    "PHO": "Pheonix Suns",
    "POR": "Portland Trailblazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "TOR": "Toronto Raptors",
    "UTA": "Utah Jazz",
    "WAS": "Washington Wizards"
}

# Used to convert the actual name of the team to the team code
teamFullToCode = {value: key for key, value in teamCodeToFull.items()}

# List of all team codes
teamCodeList = list(teamCodeToFull.keys())