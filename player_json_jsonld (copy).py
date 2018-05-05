import ijson
import os
import re
import json


data_folder = os.path.join(os.getcwd(), 'newdata')

def main():
    jsonld_file = open(data_folder + '/each_file_karma.json', 'w')
    lis_json = []
    for each_file in os.listdir(data_folder):
        m = re.match('(players)(\d*)', each_file)

        if m:
            team_no = (m.group(2))
            current_file = open(data_folder+'/'+each_file, 'r+')

            play_dict = {}
            # play_dict['@context'] = dict({"schema": "http://schema.org/"})
            play_dict['@graph'] = []

            graph_dict={}

            # graph_dict['@id'] = 'http://example.org/team#'+str(team_no)
            # graph_dict['schema:play_2018'] = []
            # play_dict['@graph'].append(graph_dict)

            for item in ijson.items(current_file, "item"):

                # graph_dict['schema:play_2018'].append({'@id': "http://example.org/playerid#"+ str(item['PlayerId'])})
                new_dict = {}
                for k, v in item.items():
                    mod_k = get_real_key(k)
                    # if mod_k == 'del':
                    #     del item[k]
                    if(mod_k is not "del" and mod_k is not ""):
                        newk = mod_k
                        new_dict[newk] = item[k]

                new_dict['team_id'] = 'http://example.org/team#'+str(team_no)
                play_dict['@graph'].append(new_dict)

            lis_json.append(play_dict)

            current_file.close()

    json.dump(lis_json, jsonld_file)
    jsonld_file.close()



def get_real_key(key):
    if(key == "PlayerId"):
        key = 'del'
    elif key == "FirstName":
        key = 'givenName'
    elif key == "LastName":
        key = 'familyName'
    elif key == "CommonName":
        key = "del"
    elif key == "Position":
        key = "del"
    elif key == "PositionCategory":
        key = "del"
    elif key == "Jersey":
        key = "del"
    elif key == "Foot":
        key = ""
    elif key == "Height":
        key = "del"
    elif key == "Weight":
        key = "del"
    elif key == "Gender":
        key = "del"
    elif key == "BirthDate":
        key = "birthDate"
    elif key == "BirthCity":
        key = "birthCity"
    elif key == "BirthCountry":
        key = "birthPlace"
    elif key == "Nationality":
        key = "del"
    elif key == "InjuryStatus":
        key = "del"
    elif key == "InjuryBodyPart":
        key = "del"
    elif key == "InjuryStartDate":
        key = "del"
    elif key == "InjuryNotes":
        key = "del"
    elif key == "Updated":
        key = "del"
    elif key == "url":
        key = "del"
    elif key == "RotoWirePlayerID":
        key = "del"
    elif key == "DraftKingsPosition":
        key = "del"
    elif key == 'PhotoUrl':
        key = "del"

    return key

if __name__ == "__main__":
    main()

