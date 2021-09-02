import requests
from datetime import datetime
from airflow.models import Variable

today = datetime.today()
today = today.strftime("%Y-%m-%d")


def get_articles(ti):

    api_key = Variable.get("news_api_key")
    url = "https://newsapi.org/v2/everything"
    params = {"qInTitle": '(f1 OR "formula 1" OR "formula one")', "language": "en",
              "from": today, "apiKey": api_key}

    response = requests.get(url, params=params)
    articles = response.json()["articles"]

    ti.xcom_push(key="articles", value=articles)


def send_teams_alert(ti):

    webhook_url = Variable.get("teams_webhook_url")
    articles = ti.xcom_pull(key="articles", task_ids=["get_articles"])[0]

    message = ""
    title = f"New F1 Articles for {today}"

    for i in range(len(articles)):
        curr_title = articles[i]["title"]
        curr_url = articles[i]["url"]

        message += f"{i+1}. **Title:** {curr_title} **URL:** {curr_url}\r"

    payload = {
        "title": title,
        "text": message
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
