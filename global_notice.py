from selenium import webdriver
from DBManager import DBManager
from Record import Record

DBManager()
record = Record()

browser = webdriver.Chrome()
browser.get('http://cms.sookmyung.ac.kr/wiz5/contents/board/board_action.php?home_id=exchange&handle=7&page=1&scale=15&categoryId=1&categoryDepth=&parent=')

last_page_num = len(browser.find_elements_by_tag_name('li'))
browser.get('http://cms.sookmyung.ac.kr/wiz5/contents/board/board_action.php?home_id=exchange&handle=7&page='+str(last_page_num)+'&scale=15&categoryId=1&categoryDepth=&parent=')

notice_list = browser.find_elements_by_css_selector('#board-container > div.list > form > table > tbody > tr > td > img')
notice_len = len(notice_list)

num = 0
for i in range(0, last_page_num):
    next_list_page = browser.find_element_by_css_selector('#board-container > div.list > div.leftBtn > div > a').get_attribute('href')
    element_list = browser.find_elements_by_css_selector('#board-container > div.list > form > table > tbody > tr > td.title > a')
    url_list = [element_list[i].get_attribute("href") for i in range(len(element_list)-1, notice_len-1, -1)]

    for url in url_list:
        browser.implicitly_wait(3)
        browser.get(url)
        title = browser.find_element_by_class_name('tit').text
        content = browser.find_element_by_id('contentsDiv').text
        num = num+1
        DBManager.insert(num, 'global', 'global', title, content)
#        print(title)
#        print(content)

    browser.get(next_list_page)

browser.quit()