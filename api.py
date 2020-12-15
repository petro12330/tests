import http.client
import urllib.parse
import json
import base
from fake_useragent import UserAgent


class Bot:
    def __init__(self, pair):
        self.region = pair[1]
        self.category = pair[0]
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.conn = http.client.HTTPSConnection("m.avito.ru", timeout=10)
        self.ua = UserAgent()
        self.count = None

    def get_id_location(self):
        payload = ''
        headers = {
            'Cookie': 'u=2kfmrcai.1cy6s0w.wt2thhj49000; buyer_selected_search_radius4=0_general; '
                      'buyer_local_priority_v2=0; buyer_selected_search_radius0=200; buyer_location_id=638920; '
                      'sx=H4sIAAAAAAACAw3JwQqAIAwA0H%2FZucPMZcu%2FkZBFCyQsR0j%2FXu%2F6Osx8P0eSLV'
                      '%2B1MpmZFissbBA7NIiQ93CmNoVxMWVSWpEI%2F6ciJkVhgAzRBWT06L173w9VOrM1VAAAAA%3D%3D; '
                      'sessid=8bc4e5dea8b325ce05e21935d12b0464.1608066636; _mlocation=638920; v=1608070541; '
                      'dfp_group=87',
            'user-agent': str(self.ua)
        }
        self.ua.update()
        self.conn.request("GET", "/api/1/slocations?key=" + self.key + "&q=" + urllib.parse.quote_plus(self.region),
                          payload, headers)
        res = self.conn.getresponse()

        data = res.read().decode("utf-8")
        id = json.loads(data)
        return id["result"]["locations"][0]['id']

    def get_count(self, id_location, time, page=1, count=0):
        payload = ''
        headers = {
            'Cookie': 'u=2kfmrcai.1cy6s0w.wt2thhj49000; buyer_selected_search_radius4=0_general; '
                      'buyer_local_priority_v2=0; buyer_selected_search_radius0=200; buyer_location_id=638920; '
                      'sx=H4sIAAAAAAACAw3JwQqAIAwA0H%2FZucPMZcu%2FkZBFCyQsR0j%2FXu%2F6Osx8P0eSLV'
                      '%2B1MpmZFissbBA7NIiQ93CmNoVxMWVSWpEI%2F6ciJkVhgAzRBWT06L173w9VOrM1VAAAAA%3D%3D; '
                      'sessid=8bc4e5dea8b325ce05e21935d12b0464.1608066636; _mlocation=638920; v=1608070541; '
                      'dfp_group=87',
            'user-agent': str(self.ua)
        }
        url = ("/api/10/items?key=" + self.key + "&locationId=" +
               str(id_location) + '&page=' + str(page) + "&query=" + urllib.parse.quote_plus(
                    self.category) + '&sort=date')
        self.conn.request("GET", url, payload, headers)
        res = self.conn.getresponse()
        data = res.read().decode("utf-8")
        items = json.loads(data)['result']["items"]
        self.count = count
        print(self.count)
        if len(items) > 0:
            positiv = 0
            for i in range(len(items)):
                item = items[i]['value']
                if item['time'] >= time:
                    positiv += 1
            if positiv != 0:
                self.get_count(id_location, time=time, page=page + 1, count=self.count + positiv)
            else:

                return self.count
        else:
            return self.count


def main(id, time):
    pair = base.get_pair(id)
    item = Bot(pair)
    id_location = item.get_id_location()
    count = item.get_count(id_location=id_location, time=time)
    print(count)


if __name__ == '__main__':
    print(main(1, 1576266383))
