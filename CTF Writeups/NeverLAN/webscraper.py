import mechanicalsoup
import csv

url = 'http://challenges.neverlanctf.com:1240/'
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
browser.find_link
browser.submit_selected()



