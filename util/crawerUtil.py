# import requests
# import urllib.parse
# import re
# class crawler():
#     def __init__(self, search):
#         base_url = 'https://t.me/s/zh_groups?q='
#         #search = '手机卡'
#         self.url = base_url + urllib.parse.quote(search)
#
#     def gettext(self):
#         r = requests.get(self.url)
#         splitlines = r.text.split('\n')
#         result = []
#         pattern = '<div class="tgme_widget_message_text js-message_text'
#         for i in splitlines:
#             if i.startswith(pattern):
#                 result.append(i)
#         return result
#
#     def get_name(self):
#         result = []
#         pattern = '_blank">@'
#         pattern_end = '</a>'
#         text = self.gettext()
#         for i in text:
#             left = i[i.find(pattern)+len(pattern):]
#             left = left[:left.find(pattern_end)]
#             result.append(left)
#         return result
#
#     def get_id(self):
#         result = []
#         text = self.gettext()
#         pattern = '<mark class="highlight"></mark></div>'
#         for i in text:
#             assert(i.endswith(pattern))
#             tmp = '-'+re.findall(r'\d+', i)[-1]
#             result.append(tmp)
#         return result
#
#     def getInfo(self):
#         name = self.get_name()
#         id = self.get_id()
#         print("name,id",name,id)
#
# a = crawler('手机卡')
# a.getInfo()
