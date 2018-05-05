import http.client, urllib.request, urllib.parse, urllib.error, base64
import ijson
import os
import re
import json

data_folder = os.path.join(os.getcwd(), 'newdata')

def main():
    f = open('newdata/round.txt', 'r')
    round_content = f.readlines()
    # count = 0
    master_list = []
    for e_round in round_content:
        roundid = e_round.rstrip()
        # call_path = get_call_path(roundid)
        # new_file_path = 'newdata/z_' + roundid + '.json'
        #
        # data = FantasyData.parse_create(call_path, 10)
        #
        # pprint(data)
        #
        # input("waiting")
        #
        # FantasyData.save_file(new_file_path, data)
        print('working for = ',roundid)
        current_file = open(data_folder+"/z_"+roundid+".json", 'r')

        current_json = json.load(current_file)
        # print(type(current_json))
        for each_element in current_json:
            master_list.append(each_element)
        current_file.close()

    current_file_master = open(data_folder + "/z_team_stats.json", 'w')
    json.dump(master_list, current_file_master)
    current_file_master.close()
    f.close()



# def get_call_path(roundid):
#     call_path = "/v3/soccer/stats/json/TeamSeasonStats/{0}".format(roundid)
#     return call_path
#
# def create_folder_if_need(directorys):
#     import os
#     if not os.path.exists(directorys):
#         os.makedirs(directorys)

if __name__ == "__main__":
    print('main')
    main()
