# import http.client
# from bs4 import BeautifulSoup
# pairs = {}
# class Register:
#     def __init__(self,region, category):
#         self.region = region
#         self.category = category
#
#     def get_id(self):
#         id =len(pairs) + 1
#         pairs[id] = [self.region, self.category]
#         return id
#
# class Bot:
#     def get_html(self, region, category):
#         conn = http.client.HTTPSConnection("www.avito.ru")
#         payload = ''
#         headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
#                       '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'Cookie': 'u=2kfmrcai.1cy6s0w.wt2thhj49000; v=1607543266; buyer_location_id=638920; luri=mytischi; '
#                       'buyer_selected_search_radius4=0_general; dfp_group=47; '
#                       'sessid=d266404b7239d11e79264b45a466dd79.1607543267; '
#                       'sx=H4sIAAAAAAACAwXBwQqAIAwA0H%2FZucOWw8TPaQyJTINhO4j%2F3nsTktZBGPV0FjHDxMXE0A3yhA8y6LW'
#                       '%2FT21hNPMuhVnKbdyxixV3hA0UMkU8YkCisNYP4bcWO1QAAAA%3D '
#         }
#         try:
#
#             conn.request("GET", "/{}?q={}".format(region, category), payload, headers)  # path - путь или категория
#             response = conn.getresponse()
#             response_body = response.read()
#         finally:
#             conn.close()
#
#         return response_body
#
#     def parse_html(self, html):
#         urls = []
#         user_database = []
#         soup = BeautifulSoup(html, 'lxml')
#         container = soup.select_one('span.page-title-count-1oJOc')
#         # container = soup.select('span.tooltip-target-wrapper-XcPdv')
#         return container.string
#
#
#
#
# def main(region, category):
#     # region = 'mytischi'
#     # category = 'lada'
#     pairs = {}
#     bot = Bot()
#     html = bot.get_html(region,category)
#     result = bot.parse_html(html)
#
#     return result
#     # print(result)
#     # bot.save_csv(result)
#     # print("OK")
#
#
# if __name__ == '__main__':
#     main()






# import http.client
# import urllib.parse
# import json
# import base
# import
# def find_count(locationId, time = 1607888783, page = 1, count = 0):
#     global conn
#     try:
#             category = 'iphone'
#             key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
#             conn = http.client.HTTPSConnection("m.avito.ru")
#             payload = ''
#             headers = {
#                 'Cookie': 'u=2kcjfwr5.1cy6s1f.67doh7wk5r40; _ym_d=1603406419; _ym_uid=1603406419323895036; _ga=GA1.2.140767030.1603406419; __gads=ID=694c7279f39a88c8:T=1603406420:S=ALNI_MZ_CEyN1ziI3EDW_yERf41kLsxGbw; _fbp=fb.1.1603406420487.1683305975; buyer_local_priority_v2=0; __cfduid=d113cd3f0d80dca326b04e737fc600ce61606430007; buyer_selected_search_radius2=0_job; _gcl_au=1.1.212409338.1607504004; sessid=50dbeeca533d556cf718ea4786013db4.1607943825; _ym_isad=1; _gid=GA1.2.1928443520.1607943829; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d40477fde300814b1e85546b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264ed3de19da9ed218fe246b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0abc91376f4301c077f2985db2d99140e2d3741983000e5586b3cba93bd9ad85a712af9e5c04fd1603fb4f900cf54c471c22da10fb74cac1eab0df103df0c26013a0df103df0c26013aafbc9dcfc006bed9083348feb1118ec1fdd7f8be323879c63de19da9ed218fe23de19da9ed218fe2d6fdecb021a45a31b3d22f8710f7c4ed78a492ecab7d2b7f; toggleOnAFB=1; toggleValueAFB=100; lastViewingTime=1607944040443; showedStoryIds=51-49-48-47-42-32; _mlocation=638920; _mlocation_mode=laas; viewedStories=40; viewedAFB=40; abp=2; buyer_location_id=624430; luri=gus-hrustalnyy; buyer_selected_search_radius0=0; v=1607975776; _ym_visorc_34241905=b; buyer_laas_location=624430; _ym_visorc_419506=w; _ym_visorc_188382=w; dfp_group=35; buyer_selected_search_radius4=0_general; so=1607977709; sx=H4sIAAAAAAACA52V0ZKqTAyE38XrcxEgA8O%2BjUQMGnXAEUY9te9%2BeqzSWvbu%2F%2FfKqoXPpLvT%2Ft34%2FjQXVPddYpEYybNGiZTi5uvvZtl8bU7PB%2B9b3k6TF46qRhqSMqtQCt42fzb95quoyZNj1%2FD3n81O23Q8La4%2B4%2F8GVkhA%2BkhvZDnO%2Btj2GvtHCJ6Tek8%2Bf7Lo2YcfyKppqQSyvBSy3HonAxlZZGOKSTDFGznuSl8%2B69F5CuaxSAycIqeUKAaiNbIogOwnSWM87InxOEhCWM%2BU6L8jXeFbArJryzQeC9cUMWaJEiUvmnz6H1N6avOU0um1DvG27CFMMpHk8Rf0Y892X4%2FBX8rWNCYKrJA7pECMZ8NKS1e5tgWSw3OazlPduS1GgIscYorZyjeyf1yma9eV7JOpD1GYKGigEL3JyvGqpux4b2FZpmXQ0YQxYUxBImOIN7J1KteZbvNDk6bkCSHKRDOO0ftViKitgazocNpNw57S7CWxpaSKJ%2FmjZbjOoeKdLRgO8ilJSAK4sgWLskb6jKyPfLo4rWibGEvjYW8KkfSNrDtr9%2FfnQYdkiIIFioZcREycNPIKWbwWrwczavyux2QMV1S8YDGRN%2FJYNrSd%2B%2F6wjyJqwGAX9cqikUJaI90L%2Bbyc65FDfRWsZfk0kHd8%2BExpVTcHGcsJJ4uzguWiSJnlU%2Fq1uGuy4%2F1OJh4mcV0SFtyNIUt49eO46PnU1v3iOGDT5AP0DsiZGKYNv5AvLbfaPp3EKhSRcIuInGAdyPpGpuF%2BIHWPbR0yhlAegQS%2Bm1f9Gcu6rHzeu%2FNx0XlXDUc8GSLinhNP8kl61buTUGenJhjOBwHCZUFxRRlA0BWy8Pkem0dze1ZD08%2B5X3A2kAc1pB8pT%2F21Pcbzcr1jA9yCEWvuF4OVPq2mZCpfUo6uWXhHcDuIvoKHMsIlv5FxKzK2z3g1QqGweUIcIXZ%2Bg%2FxPw%2BuKmiylHLr78S6pipqn8OY5oF7p445rpEtdPI4TvMhA09zRWFyRuV9TulyXdZRyOIyazmggFCUMUDH7kaHz4K5OygIZkwRgjhkqGM9C8xWyattsTxHktH%2Fu7yM7vKP88ls9f5Je3Hia%2BLJrn%2BAZGsALkpvwzbgH9NVqyheycQHjPr2OqBn8%2BOAHCG2Dynwjd8d%2BSLdhrC8Cv3OIUFWachEF45XjuMdsjwtT3NYynTADG0EjOP7zHuO87I%2FLPmyPLB6eaIxGglR4JF5tjWyK7%2B9%2F%2F0ffiSIHAAA%3D',
#                 'user - agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
#             }
#             url = '/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=624430&page='+ str(page) +'&query=iphone'
#             conn.request("GET",url , payload, headers)
#             res = conn.getresponse()
#             data = res.read().decode("utf-8")
#             dicr = json.loads(data)['result']['items']
#             positiv = 0
#             for i in range(len(dicr)):
#                 item = dicr[i]['value']
#                 if item['time'] >= time:
#                     positiv += 1
#                     print(item)
#             if positiv > 0:
#                 conn.close()
#                 find_count(locationId, time= time, page= page+1, count = count + positiv)
#             else:
#                 return count
#     finally:
#         conn.close()


# find_count(locationId = 624430, time =1576266383)
