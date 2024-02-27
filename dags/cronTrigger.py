from datetime import datetime, timedelta, date
from airflow.models import Variable
from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
import requests
import json

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="cronTriggerP1",  start_date=datetime.now(),  schedule=timedelta(days=1)) as dag:
    # Tasks are represented as operators
    selectOperator = PostgresOperator(task_id="select_priority", sql="sql/selectPriorityOne.sql", postgres_conn_id = "postgres_local")

    @task()
    def airflow(**selectOperator):
        val = selectOperator['ti'].xcom_pull(key='return_value',task_ids="select_priority")

        url = Variable.get ("url") #"http://192.168.0.19:8000/cron/"

        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
        }
        result = []
        for priority in val:
            payload_priority = dict(zip(['id', 'priority', 'is_active', 'created_at', 'updated_at'],priority))
            response = requests.request("POST", url, headers=headers, data=json.dumps(payload_priority, default=json_serial))

            result.append(response.text)
        return result

    selectOperator >>airflow()

 