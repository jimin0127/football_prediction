from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from pandas import Series


premier_team_score = DataFrame()
index_list = ["team_1", "score_1", "team_2", "score_2"]

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # webdriver 설치 경로를 입력해주세요
driver = webdriver.Chrome(path, chrome_options=options)
driver.implicitly_wait(3)  # seconds

# 2019년 8월부터 2020념 7월까지 프리미어 리그 경기 일정
naver_wfootball = ["https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2019&month=8&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2019&month=09&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2019&month=10&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2019&month=11&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2019&month=12&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=01&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=02&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=03&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=06&category=premier",
                   "https://sports.news.naver.com/wfootball/schedule/index.nhn?year=2020&month=07&category=premier"]

for football in naver_wfootball:
    driver.get(football)

    page = driver.page_source
    premi_team_score_list = BeautifulSoup(page, "html.parser")
    team_rank_list = premi_team_score_list.select('.schedule_month_area> .schedule_month_table >table>tbody>tr')

    for team in team_rank_list:
        try:
            left_team = team.select('.team_left > .name')[0].text
            #print(team.select('team_left>.name'))
            left_score = team.select('.team_left > .score')[0].text
            right_team = team.select('.team_right>.name')[0].text
            right_score = team.select('.team_right>.score')[0].text
            series = Series([left_team, left_score, right_team, right_score], index= index_list)
            premier_team_score = premier_team_score.append(series, ignore_index=True)
            #print(ranking+1, left_team, left_score, ':', right_score, right_team)
        except:
            continue

print(premier_team_score)

premier_csv = premier_team_score.to_csv('premier_csv.csv', header=True, index=False)

