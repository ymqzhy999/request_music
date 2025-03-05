import requests
import os,sys,json
from lxml import etree
from jsonpath import jsonpath
import re
from bs4 import BeautifulSoup
url ='https://dygod.org/index.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer':'https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html',
    'Host':'www.ygdy8.net',
    'Sec-Ch-Ua':'"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'richviews_9192=k6vKZw1c2P75PpdA3lSkDuygVjBDDfG2pBymb4p6XxZQ3NcgQdXIh%252FiypqZWG9KGpUaQORYffbFJBHhWxvFcpbAsmQ2qYEs74ptO6dvBVzneizMaIJ%252FbQe3X3cspuGueGcFnXijv9oxByY61HqWOPuvxDmfg8UjC4xP0lYpg1%252FgheI811dlz222UichsgfS%252FxQHuJzozJT4E%252BXH%252FwM9TKy1fDLxw98bI5xm%252Fd1MJ5K7nGGzl9FdpQrB2h75qN1dTSQk23TYpgE%252Fg7GE4J1VhTQmGwBfDWgsDRVmfvlRN5PkMZCPKifM4SAFr%252FTFlk5enwxu%252FA45jNVzce8Hm%252BrT%252BpA%253D%253D; 9192_3632_39.144.159.201=1; 919278691=%7B%225882%22%3A1%2C%225931%22%3A1%7D; beitouviews_9191=UnXvy4S5cESx9Aos9A%252B5Ytby%252Feks25N%252BTAHtqpsrDXaEr%252FzvgdBLCrcyDHsTJIw4deUhPQQPPx0fMCJD8gFYMp9%252BJT3Von2GJa7ug2t0sxvxPl23jtwDsSl8Qr%252FwTogseba4Qdb8FhDhKnIDo4E73luQcvFhr3dDJY7Jy9k%252FLkB%252Fk%252B%252BE0dfm2M%252B8l2WW1WUqvoPEuSaBjHP2MH2y3ZewHHAKVV9i8z4LsQBN9M3ZrZBnEFbYG8fg%252Fs3QY%252BvW0eyJADTM5eg3Fqca%252BaZJtGcPO6ZTCIiI1ATJRKIKSc67cbGNjfG0i7r%252BhmhNkYvVysHVQf9W%252BcUg9NbyRfMOepQ9Og%253D%253D; 9191_3666_39.144.159.201=1; track_info=1717153071698'
}

response = requests.get(url , headers = headers, )
"""
方法一:
response.encoding = 'gb2312'---->响应网页中的charset值  

方法二:
response.encoding = response.apparent.encoding
"""
response.encoding = response.apparent_encoding  #不用提前去网页看charset值
result = response.text
xml_doc = etree.HTML(result)#转为xml文档
movie_title = xml_doc.xpath('//ul/a')
for title in movie_title:
    print(title.text)