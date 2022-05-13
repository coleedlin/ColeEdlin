from random import *

from math import *

class Team:

    def __init__(self, name, war):

        self.name = name

        self.war = war

        self.wins=0

        self.losses = 0
        
    def winToLoss(self):

        self.winProb = (self.war * 1.0265 + 46.067)*0.9504/162
        self.lossProb = 1 - self.winProb
        self.pointVal = self.winProb/self.lossProb

        return self.pointVal


def sim1Game(team1, team2):

    team1pt = team1.winToLoss()

    team2pt = team2.winToLoss()

    team1WtoL = team1pt / (team2pt*1.174)

    team1prob = team1WtoL/(1+team1WtoL)

    if team1prob >= random():

        team1.wins+=1
        team2.losses+=1

    else:

        team2.wins+=1
        team1.losses+=1



def main():

    import csv
    file = open("schedule.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()

    orioles = Team('Baltimore Orioles', 26.8)
    redSox = Team('Boston Red Sox', 42.5)
    yankees = Team('New York Yankees', 48.1)
    blueJays = Team('Toronto Blue Jays', 49.2)
    rays = Team('Tampa Bay Rays', 43.2)
    tigers = Team('Detroit Tigers', 33.1)
    guardians = Team('Cleveland Guardians', 38)
    twins = Team('Minnesota Twins', 38.5)
    whiteSox = Team('Chicago White Sox', 45.7)
    royals = Team('Kansas City Royals', 33.7)
    rangers = Team('Texas Rangers', 32.9)
    athletics = Team('Oakland Athletics', 26.7)
    astros = Team('Houston Astros', 48.9)
    mariners = Team('Seattle Mariners', 39.9)
    angels = Team('Los Angeles Angels', 39.8)
    nationals = Team('Washington Nationals', 27)
    mets = Team('New York Mets', 49.1)
    phillies = Team('Philadelphia Phillies', 46.1)
    braves = Team('Atlanta Braves', 45.9)
    marlins = Team('Miami Marlins', 32.8)
    cardinals = Team('St. Louis Cardinals', 39.6)
    reds = Team('Cincinnati Reds', 29.6)
    brewers = Team('Milwaukee Brewers', 42)
    pirates = Team('Pittsburgh Pirates', 21.8)
    cubs = Team('Chicago Cubs', 32.3)
    giants = Team('San Francisco Giants', 40.1)
    diamondbacks = Team('Arizona Diamondbacks', 26.9)
    dodgers = Team('Los Angeles Dodgers', 54.5)
    rockies = Team('Colorado Rockies', 24.8)
    padres = Team('San Diego Padres', 45)

    teams = [dodgers, giants, rockies, padres, diamondbacks, reds, cardinals, cubs, pirates, brewers, nationals, mets, braves, marlins, phillies, rangers, astros, athletics, angels, mariners, tigers, guardians, twins, whiteSox, royals, orioles, redSox, blueJays, rays, yankees] 

    length = len(rows)
    for i in range(length):
        for j in range(2):
            for team in teams:
                if rows[i][j] == team.name:
                    rows[i][j] = team

    for z in range(10000):
        for row in rows:
            sim1Game(row[0], row[1])
                    
                    
                    
        

    print('Red Sox',redSox.wins,redSox.losses)
    print('Blue Jays',blueJays.wins,blueJays.losses)
    print('Orioles',orioles.wins,orioles.losses)
    print('Yankees',yankees.wins, yankees.losses)
    print('Rays',rays.wins,rays.losses)
    print()
    print('Guardians',guardians.wins,guardians.losses)
    print('Tigers',tigers.wins,tigers.losses)
    print('Royals',royals.wins,royals.losses)
    print('White Sox',whiteSox.wins,whiteSox.losses)
    print('Twins',twins.wins,twins.losses)
    print()
    print('Rangers',rangers.wins,rangers.losses)
    print('Mariners',mariners.wins,mariners.losses)
    print('Astros',astros.wins,astros.losses)
    print('Angels',angels.wins,angels.losses)
    print("A's",athletics.wins,athletics.losses)
    print()
    print('Nationals',nationals.wins,nationals.losses)
    print('Mets',mets.wins,mets.losses)
    print('Marlins',marlins.wins,marlins.losses)
    print('Phillies',phillies.wins,phillies.losses)
    print('Braves',braves.wins,braves.losses)
    print()
    print('Cubs',cubs.wins,cubs.losses)
    print('Cardinals',cardinals.wins,cardinals.losses)
    print('Pirates',pirates.wins,pirates.losses)
    print('Brewers',brewers.wins,brewers.losses)
    print('Reds',reds.wins,reds.losses)
    print()
    print('Dodgers',dodgers.wins,dodgers.losses)
    print('Giants',giants.wins,giants.losses)
    print('Rockies',rockies.wins,rockies.losses)
    print('Diamondbakcs',diamondbacks.wins,diamondbacks.losses)
    print('Padres',padres.wins,padres.losses)

if __name__ == '__main__':

    main()
