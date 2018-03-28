import ijson
import urllib.parse
from fantasy_api_calls import FantasyData
import os.path

def main():
    parse_create()


def parse_create():
    count = 0
    with open('data/team.json', 'r') as f:
        for each_team in ijson.items(f, "item"):
            team_id = (each_team['TeamId'])
            if count == 15  :
                break
            count += 1

            # if the file exists I donno want waste an API call

            if os.path.exists('data/players'+str(team_id)+'.json'):
                print('skipping - ','players'+str(team_id))
                continue

            call_path = get_player_stats_team(team_id)

            data = FantasyData.parse_create(call_path)
            print(data)
            FantasyData.save_file('data/players'+str(team_id)+'.json', data)





def get_player_stats_team(team_id):
    params = urllib.parse.urlencode({
        'teamid': team_id
    })
    call_path = "/v3/soccer/stats/json/PlayersByTeam/{}".format(team_id)

    return call_path

if __name__=='__main__':
    main()