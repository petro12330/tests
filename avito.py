import http.client
from bs4 import BeautifulSoup
pairs = {}
class Register:
    def __init__(self,region, category):
        self.region = region
        self.category = category

    def get_id(self):
        id =len(pairs) + 1
        pairs[id] = [self.region, self.category]
        return id

class Bot:
    def get_html(self, region, category):
        conn = http.client.HTTPSConnection("www.avito.ru")
        payload = ''
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'u=2kfmrcai.1cy6s0w.wt2thhj49000; v=1607543266; buyer_location_id=638920; luri=mytischi; '
                      'buyer_selected_search_radius4=0_general; dfp_group=47; '
                      'sessid=d266404b7239d11e79264b45a466dd79.1607543267; '
                      'sx=H4sIAAAAAAACAwXBwQqAIAwA0H%2FZucOWw8TPaQyJTINhO4j%2F3nsTktZBGPV0FjHDxMXE0A3yhA8y6LW'
                      '%2FT21hNPMuhVnKbdyxixV3hA0UMkU8YkCisNYP4bcWO1QAAAA%3D '
        }
        try:

            conn.request("GET", "/{}?q={}".format(region, category), payload, headers)  # path - путь или категория
            response = conn.getresponse()
            response_body = response.read()
        finally:
            conn.close()

        return response_body

    def parse_html(self, html):
        urls = []
        user_database = []
        soup = BeautifulSoup(html, 'lxml')
        container = soup.select_one('span.page-title-count-1oJOc')
        # container = soup.select('span.tooltip-target-wrapper-XcPdv')
        return container.string




def main(region, category):
    # region = 'mytischi'
    # category = 'lada'
    pairs = {}
    bot = Bot()
    html = bot.get_html(region,category)
    result = bot.parse_html(html)

    return result
    # print(result)
    # bot.save_csv(result)
    # print("OK")
#
#
# if __name__ == '__main__':
#     main()
