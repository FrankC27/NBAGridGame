import game.constants as c

def normalizeTeamCode(input):
    '''
    Given a team code string, normalize the code to allow different teams from the same 
    franchise to be treated as the same, return the normalized team code
    '''
    if input in c.teamNames:
        normalizedInput = c.teamNames[input]
    else:
        normalizedInput = input
    return normalizedInput

def convertCodeToFull(code):
    '''
    Given team code string, return the full team name
    '''
    if code in c.teamCodeToFull:
        fullTeamName = c.teamCodeToFull[code]
    else:
        fullTeamName = code
    return fullTeamName

def convertFullToCode(fullName):
    '''
    Given the full team name string, return the team code
    '''
    if fullName in c.teamFullToCode:
        teamCode = c.teamFullToCode[fullName]
    else: 
        teamCode = fullName
    return teamCode

