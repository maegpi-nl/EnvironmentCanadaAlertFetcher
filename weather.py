# https://github.com/maegpi-nl/EnvironmentCanadaAlertFetcher
# @author Maegpi
# @Date Modified 2022-03-22
# @Description: A small program that scrapes the Environment Canada's Weather Warning page and
# returns the current warning as a string object


import feedparser
import requests
from bs4 import BeautifulSoup
import re

TEST_FLAG = True #Manual flag for local testing of file

class scrape_alerts:
    def __init__(self):
        self.w = weather_rss()

    def _is_alert(self):
        return self.w.get_number_entries() > 1

    def get_alert(self):
        if self._is_alert():
            url = self.w.get_link(1)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            result = soup.find("div", {"class": "col-xs-12"})
            alert = re.sub('<[^>]+>',"",result.text)
            alert_link = self.w.get_link(1)
            alert_report = alert.replace(".",". ") + alert_link
            return alert_report
        else:
            return None

class weather_rss:
    def __init__(self):
        self.Feed = feedparser.parse("https://weather.gc.ca/rss/battleboard/nl21_e.xml")

    def get_number_entries(self):
        return len(self.Feed.entries)

    def get_title(self,i):
        return self.Feed.entries[i].title

    def get_date(self,i):
        return self.Feed.entries[i].summary

    def get_link(self,i):
        return self.Feed.entries[i].link        

if __name__ == "__main__":
    if TEST_FLAG:
        pls_work = scrape_alerts()
        print(pls_work.get_alert())
        with open("test_file.txt",'w') as fp:
            fp.write(pls_work.get_alert())
            print("Write Successful!\n")
     

