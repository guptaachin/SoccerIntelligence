'''
@gauscian
this script gets the players stats data and save it in the data/player_data
'''

import ijson
import os
from fantasy_api_calls import FantasyData

player_data_folder = os.path.join(os.getcwd(), 'data/player_data/')
team_data_folder = os.path.join(os.getcwd(), 'data/team_data/')

def main():
    f = open('Data_Collection/round.txt', 'r')
    round_content = f.readlines()
    count = 0
    for e_round in round_content:
        roundid = e_round.rstrip()
        teams_file = open('Data_Collection/team.txt', 'r')
        team_content = teams_file.readlines()

        create_folder_if_need(player_data_folder+roundid)

        for each_team in team_content:
            teamid = each_team.rstrip()
            team_file_name = 'players'+teamid+'.json'
            each_team_file = open(team_data_folder+team_file_name, 'r')
            for item in ijson.items(each_team_file, "item"):
                playerid = item['PlayerId']
                call_path = get_call_path(roundid, playerid)
                new_file_path = player_data_folder+roundid+'/' + str(roundid) + "_" + str(teamid) + "_" + str(playerid) +'.json'
                if os.path.exists(new_file_path):
                    continue
                data = FantasyData.parse_create(call_path, count)
                FantasyData.save_file(new_file_path, data)
                input('wait. line 36. remove to see all works well')

    f.close()


def get_call_path(roundid, playerid):
    call_path = "/v3/soccer/stats/json/PlayerSeasonStatsByPlayer/{0}/{1}".format(roundid, playerid)
    return call_path

def create_folder_if_need(directorys):
    import os
    if not os.path.exists(directorys):
        os.makedirs(directorys)

if __name__ == "__main__":
    main()
