# F1 News Microsoft Teams Alert using Airflow and MS Teams Webhooks

This is a simple workflow that extracts Formula 1 (I like F1) news articles using the News API and sends an alert to a Microsoft Teams channel. Hence, this is a test implementation of using the Microsoft Teams webhooks in Airflow. By using Airflow, this process can be scheduled to occur, for example, daily to get new articles for the day.

![image](https://user-images.githubusercontent.com/63803360/131786818-9a75bf1c-56b5-4cf3-aad2-e300bc0ee28d.png)

## References

1. NewsAPI Docs

   - https://newsapi.org/docs

2. Working with Airflow XComs

   - https://www.youtube.com/watch?v=8veO7-SN5ZY

3. Working with Airflow Variables
   - https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html
