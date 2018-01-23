import urllib.request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = 'https://snowe.sookmyung.ac.kr/bbs5/boards/notice'
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
browser.get(url)

titles = browser.find_elements_by_css_selector("td.title")


for title in titles:
    try:
        a = title.find_element_by_css_selector("a")
        print ("-",a.get_attribute("href"))
        print(title.text)
    except NoSuchElementException:
        print(title.text)

browser.quit()
