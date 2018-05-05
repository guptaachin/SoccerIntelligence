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
        return self.response


# def main():
#     d = Data()
#     # response = d.make_a_request(COMPETITIONS)
#     # print(response)
#     # input('waiting')
#
#
#     # for competition in response:
#     teams_response = d.make_a_request(TEAM % 444)
#
#     teams_json = teams_response['teams']
#
#
#     print(teams_json)
#     input('waiting')
#
#     # for team in teams_json:
#         team_id = team['id']
#         # print(team['id'])
#         # print(team['name'])
#         # player_response = d.make_a_request(PLAYER % team_id)
#         #
#         #
#         #
#         # print(player_response)
#         # input('waiting')
#         # break
#
#
# if __name__ == '__main__':
#     main()