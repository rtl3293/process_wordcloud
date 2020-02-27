from sportsreference.nba.teams import Teams
from sportsreference.nba.rosters import Rosters
from pprint import pprint
import csv
import os

#2013-2016
def get_rosters(years):
    #years is a list of years to pull the rosters from
    for year in years:
        
