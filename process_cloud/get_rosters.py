#!/usr/bin/env python3

#from sportsreference.nba.teams import Teams
from sportsreference.nba.roster import Roster
#import numpy as np
#from pprint import pprint
#import csv
#import os
import pandas as pd
#2013-2016
def get_rosters(years):
    #years is a list of years to pull the rosters from
    hinkie_roster = {}
#    with open("hinkie_roster.txt", "w") as f:
    for year in years:
        #Gets roster for a given year
        season = "20" + year +"-{}".format(str(int(year) + 1))
        for player in Roster(team="PHI", year="20" + year).players:
        #incrementing through the player info and formatting data
        #for wordcloud.generate_from_frequencies(hinkie_roster)
            try:
                games_played = player.dataframe.loc[season].games_played[0]
                if player.name not in hinkie_roster and games_played > 0:
                    hinkie_roster[player.name] = games_played
                elif games_played > 0:
                    hinkie_roster[player.name] += games_played
            except KeyError:
                continue
#        for name, gp in hinkie_roster.items():
#                f.write("{}: Games Played: {}\n".format(name, gp))
#    f.close()
    return hinkie_roster

#get_rosters()
#, 2015, 2016]
