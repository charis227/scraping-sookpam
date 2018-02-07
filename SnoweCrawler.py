from selenium import webdriver
from Record import Record
from DBManager import DBManager
import time


class SnoweCrawler:
    browser = None
    url = 'https://snowe.sookmyung.ac.kr/bbs5/boards/notice'

    def __init__(self):
        SnoweCrawler.browser = webdriver.Chrome()
        SnoweCrawler.browser.implicitly_wait(3)
        SnoweCrawler.browser.get(SnoweCrawler.url)
        time.sleep(5)
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        SnoweCrawler.browser.quit()
        return

    @classmethod
    def check_out_process(cls):
        SnoweCrawler.set_page_crawling()
        SnoweCrawler.crawl_pages()
        return

    @classmethod
    def check_out_finished(cls):
        SnoweCrawler.browser.find_element_by_id('fnshVDT').click()
        SnoweCrawler.browser.implicitly_wait(3)
        time.sleep(2)
        SnoweCrawler.set_page_crawling()
        SnoweCrawler.crawl_pages()
        return

    @classmethod
    def set_page_crawling(cls):
        global page_max
        page_end = SnoweCrawler.browser.find_element_by_css_selector('a.next_end')
        page_max = page_end.get_attribute('href')[len(SnoweCrawler.url) + 1:]
        page_max = int(page_max)
        return

    @classmethod
    def crawl_pages(cls):
        for count in range(1, page_max):
            print('page: ',str(count))
            cls.browser.implicitly_wait(3)
            cls.browser.get(SnoweCrawler.url+'#'+str(count))
            time.sleep(5)
            SnoweCrawler.call_list()
        return

    @classmethod
    def call_list(cls):
        element_list = cls.broswer.find_elements_by_css_selector('#messageListBody > tr')
        for tr in element_list:
            if tr.get_attribute('class')!='notice':
                num = tr.find_element_by_css_selector('td.num')
                category = tr.find_element_by_css_selector('td.title_head')
                a = tr.find_element_by_css_selector('a')
                href = a.get_attribute('href')
                title = tr.find_element_by_css_selector('span')

                record = Record()
                record.view = SnoweCrawler.browser.find_element_by_css_selector('li.pageview').text[4:]
                record.date = SnoweCrawler.browser.find_element_by_css_selector('li.date').text[:10]
                content = SnoweCrawler.browser.find_element_by_css_selector('#_ckeditorContents').text
                record.content = ' '.join(content.split())
                record.id = int(num.text)
                record.category = "공지"
                record.division = category.text
                record.title = title.text
                DBManager.insert(record)
        return

