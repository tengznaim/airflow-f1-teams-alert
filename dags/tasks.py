import requests
from datetime import datetime
from airflow.models import Variable


def get_articles(ti):

    today = datetime.today()
    today = today.strftime("%Y-%m-%d")

    api_key = Variable.get("news_api_key")
    url = "https://newsapi.org/v2/everything"
    params = {"q": "(formula 1 OR f1)", "language": "en",
              "from_data": today, "apiKey": api_key}

    response = requests.get(url, params=params)
    articles = response.json()["articles"]

    ti.xcom_push(key="articles", value=articles)


def send_teams_alert(ti):
    message = ""

    webhook_url = Variable.get("teams_webhook_url")

    articles = ti.xcom_pull(key="articles", task_ids=["get_articles"])[0]

    for article in articles:
        title = article["title"]
        article_url = article["url"]
        message += f"Title: {title} \n URL: {article_url} \n"

    payload = {
        "text": message
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
