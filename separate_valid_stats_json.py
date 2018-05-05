import os
import json
from fantasy_api_calls import FantasyData


path_data_folder = os.getcwd() + '/newdata/stat/'
path_valid_stats_folder = os.getcwd() + '/newdata/validstat/'


def main():
    get_wrong_status_files()


def get_wrong_status_files():
    count = 0
    for each_folder in os.listdir(path_data_folder):
        current_path = path_data_folder + '' + each_folder

        for each_file in os.listdir(current_path):
            current_json = json.load(open(current_path + '/' + each_file, 'r'))
            file_nme_split = each_file.split('_')
            roundid = file_nme_split[3][5:]
            team_id = file_nme_split[4]
            playerid = file_nme_split[5].split('.')[0]
            if(len(current_json) > 0):
                count += 1
                # new_file_name = path_valid_stats_folder+roundid+'_'+team_id+'_'+playerid+'.json'
                # new_file = open(new_file_name, 'w')
                # json.dump(current_json, new_file)
                # new_file.close()
    print(count)

def get_wrong_files():
    file_wrong_status = open('wrong_status_files.txt', 'r')

    all_lines = file_wrong_status.readlines()
    for line in all_lines:
        line = line.rstrip().split('_')
        roundid = line[0]
        teamid = line[1]
        playerid = line[2]

        call_path = get_call_path(roundid, playerid)
        new_file_path = 'newdata/statwrong/' +'round_team_player_stats' + str(roundid) + "_" + str(teamid) + "_" + str(playerid) + '.json'
        data = FantasyData.parse_create(call_path, 10)
        FantasyData.save_file(new_file_path, data)


def get_call_path(roundid, playerid):
    call_path = "/v3/soccer/stats/json/PlayerSeasonStatsByPlayer/{0}/{1}".format(roundid, playerid)
    return call_path


if __name__ ==  "__main__":
    main()