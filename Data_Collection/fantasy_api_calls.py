'''
@gausian
this file is central to making the API calls to the Fantasy servers and get the related data.
Please make sure to add the key in line 11. 
The key can be created by creating a free account on https://fantasydata.com/
'''

import http.client
import sys
base_folder = 'data/'

key_list = ['a316467dc81c45058e9be558798765e2']

count = 0

class FantasyData:

    @staticmethod
    def parse_create(call_path, counter = 0):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': key_list[counter],
        }
        global count
        count+=1
        
        try:
            conn = http.client.HTTPSConnection('api.fantasydata.net')
            conn.request("GET", call_path, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()

        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            input('Error. Continuing can have adverse effects. Enter to quit....')
            sys.exit(-1)
        return data

    @staticmethod
    def save_file(file_name, data):
        print('writing file - ',file_name)
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
