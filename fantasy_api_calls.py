import http.client

base_folder = 'data/'


key_list = ['f382ebfbd5604136ac03cf4cec6e3fa7', '63e5d289c1f74a41a697f71b16b1f846', '496b899d42ec441796433d65b5ddad37', '44f3b7c2ac8542b4b89db734b71464e0', '63faeb95cc12454c95800729ff862b11',
            '4206171330e242228eb5f5b816a5e11c','83d592386dc94c53bfb976ae5e9d4c25','91a7c9cf625249beab80d162d15098a9','6fae3feea25a4f2c9c98e98bc01a4c2e',
            '3f8bcf331c3b406787e984dada85ca60']
class FantasyData:

    @staticmethod
    def parse_create(call_path, counter):

        if(counter == len(key_list)):
            input("Keys exhausted")

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': key_list[counter],
        }

        try:
            conn = http.client.HTTPSConnection('api.fantasydata.net')
            conn.request("GET", call_path, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return data

    @staticmethod
    def save_file(file_name, data):
        print('writing file - ',file_name)
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
