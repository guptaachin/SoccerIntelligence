'''
@gauscian
This file is responsible for getting the player data by the team id.
The data is saved at this path data/players_data
'''


import urllib.parse
from fantasy_api_calls import FantasyData
import os.path

data_folder = os.path.join(os.getcwd(), 'data/team_data')


def main():
    create_folder_if_need(data_folder)
    f = open('Data_Collection/team.txt', 'r')
    content = f.readlines()
    count = 0
    for line in content:
        print(line)
        team_id = line.rstrip()
        if os.path.exists(data_folder+'/players' + str(team_id) + '.json'):
            count += 1
            print('skipping - ', 'players' + str(team_id))
            continue

        call_path = get_player_stats_team(team_id)
        data = FantasyData.parse_create(call_path)
        FantasyData.save_file(data_folder+'/players' + str(team_id) + '.json', data)
        input('wait')
    f.close()


def get_player_stats_team(team_id):
    params = urllib.parse.urlencode({
        'teamid': team_id
    })
    call_path = "/v3/soccer/stats/json/PlayersByTeam/{}".format(team_id)

    return call_path


def create_folder_if_need(directorys):
    import os
    if not os.path.exists(directorys):
        os.makedirs(directorys)


if __name__=='__main__':
    main()
