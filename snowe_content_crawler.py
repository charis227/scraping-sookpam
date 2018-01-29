from bs4 import BeautifulSoup
import urllib.request as request


def print_page(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'lxml')
    article = soup.select_one('div.article')
    #//*[@id="_ckeditorContents"]
    p_list = article.find_all('p')

    content = ""
    for p in p_list:
        if p.text:
             content = content + p.text + '\n'
    print(content)
    return;

