import urllib.parse
from Data_Collection.fantasy_api_calls import FantasyData
import os.path

def main():
    f = open('newdata/team.txt', 'r')
    content = f.readlines()
    count = 0
    for line in content:
        print(line)
        team_id = line.rstrip()
        if os.path.exists('newdata/players' + str(team_id) + '.json'):
            count += 1
            print('skipping - ', 'players' + str(team_id))
            continue

        call_path = get_player_stats_team(team_id)

        data = FantasyData.parse_create(call_path)
        print(data)
        FantasyData.save_file('newdata/players' + str(team_id) + '.json', data)

    print(count)
    f.close()

def get_player_stats_team(team_id):
    params = urllib.parse.urlencode({
        'teamid': team_id
    })
    call_path = "/v3/soccer/stats/json/PlayersByTeam/{}".format(team_id)

    return call_path

if __name__=='__main__':
    main()