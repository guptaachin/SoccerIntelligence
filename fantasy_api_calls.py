import http.client

base_folder = 'data/'


# key_list = ['63e5d289c1f74a41a697f71b16b1f846', '496b899d42ec441796433d65b5ddad37', '44f3b7c2ac8542b4b89db734b71464e0', '63faeb95cc12454c95800729ff862b11',
#             '4206171330e242228eb5f5b816a5e11c','83d592386dc94c53bfb976ae5e9d4c25','91a7c9cf625249beab80d162d15098a9','6fae3feea25a4f2c9c98e98bc01a4c2e','1506551484024b95883a58f28bc20f1d', 'f382ebfbd5604136ac03cf4cec6e3fa7']


key_list = ['21bf3652ec5748a2958b8ed42665109c',
            'd05a2d433fe640169b1c81b7d27d9850',
            'dde7375d613b4c73ba878d325d2fb8da',
            '5b4d2eb71bc7423897eda59f8b663681',
            '9cd46e02b7a449a69c8e33e77ae7de4f',
            'e59fda32c7ff480d901793f4338ab9a6',
            'db1c288399aa412fa0a7d968867ab799',
            '0090b5374a874e008f832b85fd256e3c',
            '342bd128907340a087d577a79c5e3315',
            '11c0612982e04420b2734f535e818689',
            '82a88a31de514689b7a1cbb95faf0031']

count = 0

class FantasyData:

    @staticmethod
    def parse_create(call_path, counter):
        if(counter == len(key_list)):
            input("Keys exhausted")
            import sys
            sys.exit(1)


        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': key_list[counter],
        }
        global count
        count+=1
        print('calls made -**************************************************** ',count)
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
