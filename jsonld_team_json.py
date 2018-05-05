import os
import ijson
import json

data_folder = os.path.join(os.getcwd(), 'newdata')


def main():
    current_file = open(data_folder + '/team.json' , 'r+')
    jsonld_file = open(data_folder + '/team_ld_karma.json', 'w')

    play_dict = {}
    play_dict['@context'] = dict({"schema": "http://schema.org/"})
    play_dict['@graph'] = []

    graph_dict = {}
    graph_dict['@id'] = 'http://example.org/teams'
    graph_dict['schema:team'] = []
    play_dict['@graph'].append(graph_dict)

    teams_set = set()
    f = open(data_folder +'/team.txt', 'r')
    content = f.readlines()
    count = 0
    for line in content:
        team_id = line.rstrip()
        teams_set.add(team_id)

    for item in ijson.items(current_file, "item"):
        new_dict = {}

        if str(item["TeamId"]) not in teams_set:
            continue

        link = 'http://example.org/team#'+str(item["TeamId"])

        graph_dict['schema:team'].append({'@id':link})
        for k, v in item.items():
            mod_k = get_real_key(k)

            if (mod_k is not ""):
                newk = 'schema:' + mod_k
                new_dict[newk] = item[k]

        new_dict['@id'] = 'http://example.org/team#'+str(item['TeamId'])
        play_dict['@graph'].append(new_dict)


    json.dump(play_dict, jsonld_file)
    jsonld_file.close()
    current_file.close()


def get_real_key(key):
    # if(key == "TeamId"):
    #     key = '@id'
    # elif key == "FirstName":
    #     key = 'givenName'
    # elif key == "LastName":
    #     key = 'familyName'
    # elif key == "CommonName":
    #     key = "name"
    # elif key == "Position":
    #     key = "Role"
    # elif key == "PositionCategory":
    #     key = ""
    # elif key == "Jersey":
    #     key = "Number"
    # elif key == "Foot":
    #     key = ""
    # elif key == "Height":
    #     key = "height"
    # elif key == "Weight":
    #     key = "weight"
    # elif key == "Gender":
    #     key = "gender"
    # elif key == "BirthDate":
    #     key = "birthDate"
    # elif key == "BirthCity":
    #     key = ""
    # elif key == "BirthCountry":
    #     key = "birthPlace"
    # elif key == "Nationality":
    #     key = "nationality"
    # elif key == "InjuryStatus":
    #     key = ""
    # elif key == "InjuryBodyPart":
    #     key = ""
    # elif key == "InjuryStartDate":
    #     key = ""
    # elif key == "InjuryNotes":
    #     key = ""
    # elif key == "Updated":
    #     key = "UpdateAction"
    # elif key == "url":
    #     key = ""
    # elif key == "RotoWirePlayerID":
    #     key = ""
    # elif key == "DraftKingsPosition":
    #     key = ""

    return key


if __name__ == '__main__':
    main()