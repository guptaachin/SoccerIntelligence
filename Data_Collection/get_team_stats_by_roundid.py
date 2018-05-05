import os
from Data_Collection.fantasy_api_calls import FantasyData

data_folder = os.path.join(os.getcwd(), 'newdata')

def main():
    f = open('round.txt', 'r')
    round_content = f.readlines()
    for e_round in round_content:
        roundid = e_round.rstrip()
        call_path = get_call_path(roundid)
        new_file_path = 'newdata/z_' + roundid + '.json'
        data = FantasyData.parse_create(call_path, 10)
        FantasyData.save_file(new_file_path, data)

    f.close()

def get_call_path(roundid):
    call_path = "/v3/soccer/stats/json/TeamSeasonStats/{0}".format(roundid)
    return call_path

if __name__ == "__main__":
    print('main')
    main()
