import pycrfsuite
from crf_util import sent2features, to_sent
from nltk.metrics.distance import edit_distance
from nltk.tokenize import word_tokenize
import json

def ner_crf(sent, tagger):
    return tagger.tag(sent2features(to_sent(sent)))
    
    
def tag_to_player(sent, tag, player_dic):
    temp = ''
    player_name = []
    for i, tag in enumerate(tag):
        if tag not in ['B-N', 'I-N']:
            if temp != "":
                player_name.append(temp)
                temp = ""
                
        if tag == 'B-N':
            temp = sent[i] + ' '
        elif tag == 'I-N':
            temp += sent[i] + ' '
        
    if temp != "":
        player_name.append(temp)
    res = []
    for this_player in player_name:
        this_player = this_player.strip()
        if len(this_player.split()) > 1:
          
            for player in player_dic:
                if player['CommonName']:
                    if edit_distance(this_player ,player['CommonName']) < 0.02:

                        res.append(player['PlayerId'])

        else:
        
            for player in player_dic:
                if player['CommonName']:
                    if edit_distance(this_player ,player['LastName']) < 0.02: 

                        res.append(player['PlayerId'])

                        
    return res

def tag_to_team(sent, tag, team_dic):
    temp = ''
    team_name = []
    for i, tag in enumerate(tag):
        if tag not in ['B-C', 'I-C']:
            if temp != "":
                team_name.append(temp)
                temp = ""
                
        if tag == 'B-C':
            temp = sent[i] + ' '
        elif tag == 'I-C':
            temp += sent[i] + ' '
        
    if temp != "":
        team_name.append(temp)
    res = []
    for this_team in team_name:
        this_team = this_team.strip()   
        for team in team_dic:
            if team['Name']:
                if this_team in team['Name']: 
                    res.append(team['TeamId'])
    return res
    
    
if "__name__" == "__main__":

    with open('goal_extracted.json', 'r') as f:
        goal_news = json.load(f)
        
    tagger = pycrfsuite.Tagger()
    tagger.open('soccer_ner.crfsuite')

    goal_news_mention = []

    for a_news in goal_news:
        if a_news['title']:
            title = a_news['title']
            tokens = word_tokenize(title)
            tag = ner_crf(title, tagger)
            relate_players = tag_to_player(tokens,tag, players)
            relate_teams = tag_to_team(tokens,tag, teams)
            if relate_players or relate_teams:
                new_a_news = a_news
                if relate_players:
                    new_a_news['relate_players'] = relate_players
                if relate_teams:
                    new_a_news['relate_teams'] = relate_teams
                goal_news_mention.append(new_a_news)

    with codecs.open('goal_news_mention', 'w','utf8') as f:
        json.dump(goal_news_mention, f)
