from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from tasks import get_articles, send_teams_alert


with DAG("f1_alert_dag",
         schedule_interval="@once",
         start_date=datetime.now(),
         description="A DAG that gets daily news articles relating to F1 and sends an alert to a Microsoft Teams channel.",
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="get_articles",
        python_callable=get_articles
    )

    task_2 = PythonOperator(
        task_id="send_teams_alert",
        python_callable=send_teams_alert
    )

    task_1 >> task_2
