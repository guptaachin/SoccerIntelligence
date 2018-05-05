import os
import json
from pprint import pprint

path_valid_stats_folder = os.getcwd() + '/newdata/validstat/'


def main():
    from_valid_folder()


def from_valid_folder():
    cumulative_json = open(path_valid_stats_folder+'a_json.json', 'w')

    # master_dict  = {}
    # master_dict['@context'] = {"schema":"http://schema.org/"}
    # master_dict['@graph'] = []
    # rootnode_dict = {}
    # rootnode_dict['@id'] = "http://example.org/stats"
    # rootnode_dict['schema:players'] = []
    # master_dict['@graph'].append(rootnode_dict)
    # count = 0
    list_json = []
    for e_file in os.listdir(path_valid_stats_folder):
        if(e_file == 'a_json.json'):
            continue
        file_instance = json.load(open(path_valid_stats_folder + e_file, 'r'))
        # # player_dict = {}
        # split_file = e_file.split("_")
        # playerid = split_file[2].split(".")[0]
        # roundid = split_file[0]
        # player_dict['@id'] = "http://example.org/playerid#"+playerid

        # rootnode_dict['schema:players'].append({'@id':"http://example.org/playerid#"+playerid})

        # player_dict['schema:stats_'+roundid] = []

        # for k,v in file_instance[0].items():
        list_json.append(file_instance[0])

        # new_dict = {}
        # for k_, v_ in player_dict.items():
        #     newk = 'schema:' + k_
        #     new_dict[newk] = player_dict[k_]
        #
        # new_dict['@id'] = "http://example.org/playerid#" + playerid
        # master_dict['@graph'].append(player_dict)
        # count += 1
        # if(count == 1):
        #     break


    json.dump(list_json, cumulative_json)
    cumulative_json.close()

if __name__ == "__main__":
    main()