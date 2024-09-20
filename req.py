import requests
from bs4 import BeautifulSoup
import re
from db import DBTool


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


# url = "https://journal.ecust.edu.cn/"
# title = scrap(url, "div.article-list-title.clearfix > a", flag=0)
# print(len(title))
# title_urls = scrap(url, "div.article-list-title.clearfix > a", flag=1)
# # print(title_urls.length)
# authors = scrap(url, "div.article-list-author", flag=0)
# print(len(authors))
# # print("文章作者：",authors)
# abstracts = []
# for url in title_urls:
#     urls = "https://journal.ecust.edu.cn" + url
#     abstracts.append(scrap(urls, "div.abstract-cn div.article-abstract", flag=0))
# print(len(abstracts))

if __name__ == '__main__':
    #开始调用函数进行爬取
    url="https://journal.ecust.edu.cn/"
    db = DBTool()
    #首先要爬取到内容，再写入数据库
    title = scrap(url, "div.article-list-title.clearfix > a", flag=0)
    title_urls = scrap(url, "div.article-list-title.clearfix > a", flag=1)
    author = scrap(url, "div.article-list-author", flag=0)
    abstract = []
    for url in title_urls:
        urls = "https://journal.ecust.edu.cn" + url
        abstract.append(scrap(urls, "div.abstract-cn div.article-abstract", flag=0))

    if len(title) == len(author) == len(abstract):
        for i in range(len(title)):
            # 调用insert函数，这里假设已经根据需求调整了该函数以接受单个元素
            if db.insert(title[i], author[i], abstract[i]):
                print(f"Inserted: {title[i]}, {author[i]}, {abstract[i]}")
                # 可以选择性地查询并打印所有数据，但可能不需要每次插入都查询
                # print(db.queryAll())
    else:
        print("Error: The lists do not have the same length.")