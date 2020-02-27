#!/usr/bin/env python3

#from sportsreference.nba.teams import Teams
from sportsreference.nba.roster import Roster
#from pprint import pprint
#import csv
#import os

#2013-2016
def get_rosters(years):
    #years is a list of years to pull the rosters from
    with open("hinkie_roster.txt", "w") as f:
    #    hinkie_roster = {}
        for year in years:
            #Gets roster for a given year
            roster = Roster(team="PHI", year=str(year), slim=True).players
            #incrementing through the player info and print playerID and name
            for playerID, name in roster.items():
                f.write("{}: PlayerID: {}\n".format(name, playerID))
    f.close()


get_rosters(["2018"])
