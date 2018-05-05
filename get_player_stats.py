import http.client, urllib.request, urllib.parse, urllib.error, base64
import ijson
import os
import re
import json
from fantasy_api_calls import FantasyData


data_folder = os.path.join(os.getcwd(), 'newdata')

def main():
    f = open('newdata/round.txt', 'r')
    round_content = f.readlines()
    count = 0
    for e_round in round_content:
        roundid = e_round.rstrip()
        teams_file = open('newdata/team.txt', 'r')
        team_content = teams_file.readlines()

        create_folder_if_need('newdata/stat/'+roundid)

        for each_team in team_content:
            teamid = each_team.rstrip()
            team_file_name = 'players'+teamid+'.json'
            each_team_file = open('newdata/'+team_file_name, 'r')
            for item in ijson.items(each_team_file, "item"):
                playerid = item['PlayerId']
                call_path = get_call_path(roundid, playerid)
                new_file_path = 'newdata/stat/'+roundid+'/round_team_player_stats' + str(roundid) + "_" + str(teamid) + "_" + str(playerid) +'.json'

                if os.path.exists(new_file_path):
                    continue


                data = FantasyData.parse_create(call_path, count)
                if ': 403' in str(data)[1:-1]:
                    print('count = ',count)
                    count += 1
                    data = FantasyData.parse_create(call_path, count)


                if ': 403' not in str(data)[1:-1]:
                    FantasyData.save_file(new_file_path, data)
                else:
                    print('not writing')

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
