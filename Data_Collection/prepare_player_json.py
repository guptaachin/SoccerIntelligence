import ijson
import json
import bs4 as bs
import os
from pprint import pprint

path = '/home/achin/Downloads/espn.json'
keys_ = {'url':'url', 'rc':'raw_content','id':'doc_id', 't_c':'timestamp_crawl'}
base_folder = 'data/'

def main():
    player_json, player_hash_file = load_player_hash()
    master_player_dict = parse(player_json, player_hash_file)
    write_player_data(master_player_dict)
    release_resources(player_hash_file)

def load_player_hash():
    player_hash = set()
    f = open(base_folder+'player_data.json', 'r+')

    is_empty = os.path.getsize(base_folder+'player_data.json') == 0
    if(not is_empty):
        player_hash = json.load(f)

    return player_hash, f


def parse(player_hash, player_hash_file):
    master_player_dict = {}

    br = 0

    with open(path, 'r') as f:
        for item in ijson.items(f, "item"):
            print(item[keys_['url']])
            soup = bs.BeautifulSoup(item[keys_['rc']], 'html.parser')
            players_bio = soup.find_all('div', {"class": "player-spec"})

            print('players_bio length - ',len(players_bio))

            if(len(players_bio) == 1):
                player_dict = load_player_bio_dict(players_bio, player_hash)

            entry_file = player_dict['name'].strip() + ' ' + player_dict['dob'].strip() #+ '\t' + player_dict['pob'].strip()
            # if the player is not in the index file refresh
            # if _hash(entry_file) not in player_hash:
            #     print('writing - ',entry_file)
            #     # player_hash_file.write(entry_file+'\n')
            #     player_hash.add(_hash(entry_file))

            # for now this will overwrite stuff
            master_player_dict[str(_hash(entry_file))] = player_dict
            print(len(player_hash))
            br+=1
            if br == 10:
                break

    return master_player_dict

def load_player_bio_dict(players_bio, player_dict):

    player_name = players_bio[0].h1.text
    player_dict['name'] = player_name

    player_det = players_bio[0].find_all('dl')

    for index, element in enumerate(player_det):
        player_l = ['' for _ in range(3)]
        player_details = element.find_all('dd')

        for i_, e_ in enumerate(player_details):
            player_l[i_] = e_.text

        if(index == 0):
            player_dict['position'] = player_l[0].strip()
            player_dict['height'] = player_l[1].strip()
            player_dict['weight'] = player_l[2].strip()
        else:
            player_dict['age'] = player_l[0].strip()
            player_dict['dob'] = player_l[1].strip()
            player_dict['pob'] = player_l[2].strip()

    return player_dict


def release_resources(player_hash_file):
    player_hash_file.close()


def write_player_data(master_player_dict):
    with open(base_folder+'player_data.json', 'w') as outfile:
        json.dump(master_player_dict, outfile)

def _hash(n):
  return (n)

if __name__ == '__main__':
    main()

