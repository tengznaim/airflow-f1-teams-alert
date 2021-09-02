# F1 News Microsoft Teams Alert using Airflow and MS Teams Webhooks

This is a simple workflow that extracts Formula 1 (I like F1) news articles using the News API and sends an alert to a Microsoft Teams channel. There are various ways to do this, for example, a Discord bot without the need of Airflow. However, this is a test of using the Microsoft Teams webhook in Airflow. A major advantage of using Airflow, although may not be intended for this use case is the ability to schedule this process, for example, daily to get new articles for the day.

![image](https://user-images.githubusercontent.com/63803360/131786818-9a75bf1c-56b5-4cf3-aad2-e300bc0ee28d.png)

## Getting Articles using the News API

The News API has a Python client. However, this somehow didn't work in Airflow (the module was unrecognised when importing the DAG). Hence, for this implementation, I made manual requests using the requests module to the everything endpoint.

After getting the articles, I used XComs in Airflow to transfer data between the tasks. However, this may not be the recommended use of XComs due to larger nature of the response. One improvement would probably be to simplify the response before transferring.

## Working with the MS Teams Webhook

MS Teams enables creating an incoming webhook for MS Teams channels to do things like sending messages. In order to apply this in an Airflow DAG, I also used manual requests for this due to the same reason of not being able to import the DAG if the wrapper module is included.

## References

1. NewsAPI Docs

   - https://newsapi.org/docs

2. Working with Airflow XComs

   - https://www.youtube.com/watch?v=8veO7-SN5ZY

3. Working with Airflow Variables

   - https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html

4. Sending Messages to Teams Channels using Python

   - https://stackoverflow.com/questions/59371631/send-automated-messages-to-microsoft-teams-using-python

5. pymsteams Docs and Github Repo
   - https://pypi.org/project/pymsteams/
   - https://github.com/rveachkc/pymsteams
