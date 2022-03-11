from itertools import count
import datetime
import feedparser
import asyncio
from RSSfeed import url_link

rssfeeds = list()

async def start():
    print("Process has been started!")
    await rss()
    await rss2()

async def rss():
    d = feedparser.parse(url_link)
    storage = d["entries"][0]
    rssfeeds.append(storage)

async def update_rss():
    d = feedparser.parse(url_link)
    storages = d["entries"][0]
    return storages


async def rss2():
    while True:
        data = await update_rss()
        if rssfeeds[0] == data:
            print("Nothing new in the feed!\nWaiting for 5 seconds...")
            await asyncio.sleep(5)
        elif rssfeeds[0] != data:
            d = feedparser.parse(url_link)
            title = d["entries"][0]["title"]
            titledetail = d["entries"][0]["id"]
            rssfeeds.clear()
            rssfeeds.append(data)
            print(f"{title} and its link:{titledetail}\nwere detected in the stream!")
            await asyncio.sleep(5)

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(start())
    loop.run_forever()
except KeyboardInterrupt:
    loop.close()
else:
    print("Program has ended by an unknown reason.")