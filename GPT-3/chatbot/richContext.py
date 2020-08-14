import json
import requests
import config
import random

def fetchContent(country="us", city="Madison",articles=5):
    context =[]
    cityName = f"{city},{country}" #used by weather api
    weatherKey = config.weatherApiKey
    newsKey = config.newsApiKey
    #fetch weather context
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/weather?q={cityName}&appid={weatherKey}")
    if response.status_code == 200:
        data = response.json()
        context.append(f"Weather info|{data['main']['temp']}, humidity is {data['main']['humidity']} and the general weather is {data['weather'][0]['description']}.\n")
    #fetch news context
    url = (f"http://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}")
    response = requests.get(url)
    articleList = [a['title'] for a in response.json()['articles']]
    randomNews = "News info|" + " ".join(random.sample(articleList, articles)) + ".\n"
    context.append(randomNews)
    return " ".join(context)

if __name__ == "__main__":
    pass


