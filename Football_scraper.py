import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta

def today_scraper():
    bundesliga_games = bundesliga_scraper()
    premleague_games = premleage_scraper()
    games = [bundesliga_games, premleague_games]
    return games


def bundesliga_scraper():
    URLS = ["https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures"]
    fixtures=['Todays bundesliga games are:']
    for url in URLS:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        today = date.today()

        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            dates = row.find_all('td')
            try:
                if str(today) == dates[1].text:
                    cet_time = datetime.time(datetime.strptime(str(dates[2].text[0:5]), "%H:%M"))
                    fixtures.append(f'{cet_time}---{dates[3].text} {dates[5].text} {dates[7].text}')
            except:
                print('empty')
    return fixtures

def premleage_scraper():
    URLS = ["https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"]
    fixtures=['Todays premier league games are:']
    for url in URLS:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        today = date.today()

        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            dates = row.find_all('td')
            try:
                if str(today) == dates[1].text:
                    cet_time = datetime.time(datetime.strptime(str(dates[2].text[0:5]), "%H:%M") + timedelta(hours=1))
                    fixtures.append(f'{cet_time}---{dates[3].text} {dates[5].text} {dates[7].text}')
            except:
                print('empty')
    return fixtures

def yesterday_scraper():
    URLS = ["https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures","https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"]
    fixtures=['Yesterdays games were:']
    for url in URLS:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            dates = row.find_all('td')
            try:
                if str(yesterday) == dates[1].text:
                    fixtures.append(f'{dates[3].text} {dates[5].text} {dates[7].text}')
            except:
                print('empty')
    return fixtures


today_scraper()


