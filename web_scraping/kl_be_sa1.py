from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")

url = "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kliniken-herzogin-elisabeth-braunschweig"
driver.get(url)

content = driver.page_source
beautisoup = BeautifulSoup(content, 'html.parser')

names=[]
ratings=[]
reviews=[]
departments=[]
dates=[]
titles=[]

for ele in beautisoup.find_all("article", attrs={"class":"bewertung"}):
    title = ele.find("h2")
    titles.append(title.text)
    date = ele.find("time")
    dates.append(date.text)
    department = ele.find("a", href=True)
    departments.append(department.text)
    review = ele.find("p")
    reviews.append(review.text)
    
for ele in beautisoup.find_all("section", attrs={"class":"rating"}):
    rating = ele.find("img")
    ratings.append(rating["class"])

df = pd.DataFrame({'Department':departments, 'Date':dates, 'Title':titles, 'Review':reviews}) 
df.to_csv('D:/refugeeks_project/selenium_py/p1/klinik1_liste.csv', index=False, encoding='utf-8')

