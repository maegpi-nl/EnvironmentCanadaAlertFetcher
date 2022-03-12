import feedparser
import requests
from bs4 import BeautifulSoup

class weatherAPI:
    def __init__(self, entry):
        self.Feed = feedparser.parse("https://weather.gc.ca/rss/battleboard/nl21_e.xml")
        self.entry = entry
        
    def getNumberEntries():
        return len(self.Feed.entries)

    def getTitle():
        return self.entry.title

    def getDate(entry):
        return entry.summary

    def getLink(entry):
        return entry.link

NewsFeed = feedparser.parse("https://weather.gc.ca/rss/battleboard/nl21_e.xml")
print("Number of RSS entries:" ,len(NewsFeed.entries))

entry = NewsFeed.entries[1]
for key in entry.keys():
    print(key)#,": ", NewsFeed.entries.key)
print()

for warning in NewsFeed.entries:
    print(warning.summary)
    print(warning.title)
    print(warning.link)
    print(warning.id)
    print()
#summary is the date and time the warning was posted

numberOfEntries = len(NewsFeed.entries)

if numberOfEntries > 1:
    url = NewsFeed.entries[1].link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", {"class" : "col-xs-12"})
    weatherWarning = result.find("p")
    print(result)
#    print(result.prettify())
   # print(page.text)


