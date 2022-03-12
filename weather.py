#

import feedparser
import requests
from bs4 import BeautifulSoup
import re

TEST_FLAG = True #Manual flag for local testing of file

class scrapeAlerts:
    def __init__(self):
        self.w = weatherRSS()

    def _isAlert(self):
        return True if (self.w.getNumberEntries() > 1) else False

    def getAlert(self):
        if self._isAlert():
            url = self.w.getLink(1)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            result = soup.find("div", {"class": "col-xs-12"})
            alert = re.sub('<[^>]+>',"",result.text)
            alertLink = self.w.getLink(1)
            alertReport = alert.replace(".",". ") + alertLink
            return alertReport
        else:
            return "No Current Alerts!\n"

class weatherRSS:
    def __init__(self):
        self.Feed = feedparser.parse("https://weather.gc.ca/rss/battleboard/nl21_e.xml")

    def getNumberEntries(self):
        return len(self.Feed.entries)

    def getTitle(self,i):
        return self.Feed.entries[i].title

    def getDate(self,i):
        return self.Feed.entries[i].summary

    def getLink(self,i):
        return self.Feed.entries[i].link        

if __name__ == "__main__":
    if TEST_FLAG:
        plsWork = scrapeAlerts()
        print(plsWork.getAlert())
        with open("testFile.txt",'w') as fp:
            fp.write(plsWork.getAlert())
            print("Write Successful!\n")
     

