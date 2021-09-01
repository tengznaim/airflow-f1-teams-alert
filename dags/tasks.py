import requests
from datetime import datetime


def get_articles(ti):

    today = datetime.today()
    today = today.strftime("%Y-%m-%d")

    api_key = "4e54122ff1604ae1acb69c54be1a0b3c"
    url = "https://newsapi.org/v2/everything"
    params = {"q": "(formula 1 OR f1)", "language": "en",
              "from_data": today, "apiKey": api_key}

    response = requests.get(url, params=params)
    articles = response.json()["articles"]

    ti.xcom_push(key="articles", value=articles)


def send_teams_alert(ti):
    message = ""

    webhook_url = "https://365umedumy.webhook.office.com/webhookb2/a0ccfe7b-48a4-46f7-8746-54143a9409b2@a63bb1a9-48c2-448b-8693-3317b00ca7fb/IncomingWebhook/7e8a547d572848d79a4125ce0bcbeaac/c44ebda5-7a13-4a73-8d4d-17d3f644e7be"

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
