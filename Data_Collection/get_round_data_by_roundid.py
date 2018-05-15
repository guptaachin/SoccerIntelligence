'''
@gauscian
This file is responsible for getting the round data. 
The rounds is gets the data for are enumerated in the round.txt
The out put of this file is saved to data folder in form of json files.
'''

import os
import sys
from fantasy_api_calls import FantasyData

data_folder = os.path.join(os.getcwd(), 'data/round_data')

def main():
    f = open('Data_Collection/round.txt', 'r')
    round_content = f.readlines()
    for e_round in round_content:
        roundid = e_round.rstrip()
        call_path = get_call_path(roundid)
        new_file_path = data_folder+'/round_' + roundid + '.json'
        data = FantasyData.parse_create(call_path)
        FantasyData.save_file(new_file_path, data)
    f.close()

def get_call_path(roundid):
    call_path = "/v3/soccer/stats/json/TeamSeasonStats/{0}".format(roundid)
    return call_path

if __name__ == "__main__":
    print('main')
    main()
