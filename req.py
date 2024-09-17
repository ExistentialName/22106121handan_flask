import requests
from bs4 import BeautifulSoup
import re

def scrap(target, selectors, flag):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }
    r = requests.get(target, headers=headers)

    bs = BeautifulSoup(r.text, 'html.parser')
    res = bs.select(selector=selectors)
    if flag == 0:
        return [re.sub(r'\s+', '', item.get_text(strip=True)) for item in res if item.get_text(strip=True)]
    if flag == 1:
        return [item.get('href') for item in res if item.get('href')]


url = "https://journal.ecust.edu.cn/"
title = scrap(url, "div.article-list-title.clearfix > a", flag=0)
print("文章标题：",title)
title_urls = scrap(url, "div.article-list-title.clearfix > a", flag=1)
print("文章地址：",title_urls)
authors = scrap(url, "div.article-list-author span a", flag=0)
print("文章作者：",authors)
abstracts = []
for url in title_urls:
    urls = "https://journal.ecust.edu.cn" + url
    abstracts.append(scrap(urls, "div.abstract-cn div.article-abstract", flag=0))
print("第一篇文章摘要：",abstracts[0])
