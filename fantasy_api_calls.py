import http.client

base_folder = 'data/'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f382ebfbd5604136ac03cf4cec6e3fa7',
}

class FantasyData:

    @staticmethod
    def parse_create(call_path):
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
        f = open(file_name, 'wb')
        f.write(data)
        f.close()
