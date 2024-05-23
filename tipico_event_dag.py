from datetime import datetime, timedelta
import requests
import json
import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 21),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the API endpoint URL
api_url = "https://trading-api.tipico.us/v1/pds/lbc/events/live?licenseId=US-NJ&lang=en&limit=18"


# Define the function to call the API and store the data
def call_and_store_api_data(**context):
    # Call the API and get the response
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        data = json.loads(response.content)

        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Store the data (e.g., to a local file or database)
        df.to_csv('api_data.csv', index=False)

        # Log a message
        print(f"API data stored successfully at {datetime.now()}")
    else:
        # Log an error message
        print(f"Failed to call the API. Status code: {response.status_code}")


# Create the DAG
with DAG('tipico_api_dag', default_args=default_args, schedule_interval=timedelta(minutes=10)) as dag:
    # Define the task to call the API and store the data
    call_and_store_task = PythonOperator(
        task_id='call_and_store_api_data',
        python_callable=call_and_store_api_data,
        dag=dag
    )