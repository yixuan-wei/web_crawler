"""
sentiment analysis based on ibm tone analyzer, and english lyrics in QQ music
Utilizing PyQt4
"""

import sys
import time
from selenium import webdriver
from urllib import request
from lxml import etree

class PhantomSpider:
    def getContent(self, url):
        browser = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
        browser.get(url)
        time.sleep(3)
        html = browser.execute_script("return document.documentElement.outerHTML")
        output = etree.HTML(html)
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath, 'w', encoding='UTF-8')
        file_obj.write(content)
        file_obj.close()



'''xslt_root = driver.get("https://y.qq.com/n/yqq/toplist/3.html#stat=y_new.toplist.menu.3")
time.sleep(3)

transform = etree.XSLT(xslt_root)
#fo = open("aaaa1.txt", "wb")
html = driver.execute_script("return document.documentElement.outerHTML")
doc = etree.HTML(html)
result_tree = transform(doc)
#fo.write(driver.page_source.encode())
#fo.close()
print(result_tree)
driver.quit()'''