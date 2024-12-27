from bs4 import BeautifulSoup 
import requests 
import csv 
import pandas as pd

url = "https://editorial.rottentomatoes.com/guide/best-new-movies/"

website = requests.get(url).text

mywebsite = BeautifulSoup(website, "lxml")

films = mywebsite.find_all("div", class_="row countdown-item")

with open("Data_of_filmes.csv", "w", encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['film name', 'film year', 'film rate', 'director name'])

    for filme in films:
        filme_name = filme.find("h2").text.strip().split("(")[0].strip()
        filme_year = filme.find("h2").text.strip().split("(")[1].split(")")[0]
        filme_rate = filme.find("h2").text.strip().split()[-1]
        director = filme.find("div", class_="info director")
        director_names = [a.text for a in director.find_all("a")]
        writer.writerow([filme_name, filme_year, filme_rate, director_names])

df = pd.read_csv("Data_of_filmes.csv", encoding='utf-8')

print(df)

for filme in films:
    img_tag = filme.find("img")
    
    if img_tag:
        img_src = img_tag.get("src")
        print(img_src)
        response = requests.get(img_src)
        path = f"E:/AI/Ai course instance/taskes/web_scraping/images/{films.index(filme)}.jpg"
        with open(path, "wb") as image:
            image.write(response.content)
