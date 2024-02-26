from datetime import datetime, timedelta
from airflow.models import Variable
from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
import requests
import json
# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="cronTrigger",  start_date=datetime.now(),  schedule=timedelta(days=1)) as dag:
    # Tasks are represented as operators
    selectOperator = PostgresOperator(task_id="select_priority", sql="sql/selectPriorityOne.sql", postgres_conn_id = "postgres_local")

    @task()
    def airflow(**selectOperator):
        val = selectOperator['ti'].xcom_pull(key='return_value',task_ids="select_priority")

        url = "http://172.20.240.1:8000/cron/"

        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
        }
        result = []
        for priority in val:
            response = requests.request("POST", url, headers=headers, data=json.dumps(priority))

            result.push(response.text)
        return result

    selectOperator >>airflow()

 