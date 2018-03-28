import http.client
import json

API_TOKEN = 'a5b08602d1f543a39f0abb46b8812539'
TEAM = '/v1/competitions/%d/teams'
PLAYER = '/v1/teams/%d/players'
COMPETITIONS = '/v1/competitions'

class Data:

    def __init__(self):
        self.connection = None
        self.header = None
        self.response = None

    def make_a_request(self, extension):
        '''
        :return: response
        '''
        self.connection = http.client.HTTPConnection('api.football-data.org')
        self.headers = {'X-Auth-Token': API_TOKEN, 'X-Response-Control': 'minified'}
        self.connection.request('GET', extension, None, self.headers)
        self.response = json.loads(self.connection.getresponse().read().decode())
        print(extension)
        return self.response


def main():
    d = Data()
    response = d.make_a_request(COMPETITIONS)

    for competition in response:
        teams_response = d.make_a_request(TEAM % competition['id'])
        teams_json = teams_response['teams']
        for team in teams_json:
            team_id = team['id']
            print(team_id)
            player_response = d.make_a_request(PLAYER % team_id)
            print(player_response)
        break


if __name__ == '__main__':
    main()