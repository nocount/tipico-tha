import json
from datetime import datetime, timedelta

import pandas as pd
import pandas_redshift as pr
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'wburchenal',
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
        # Rename group column to groups as group is a reserved word in Redshift
        df = df.rename(columns={"group": "groups"})

        # Establish Redshift connection
        pr.connect_to_redshift(
            'dev',
            host='<host>',
            port='5439',
            user='<user>',
            password='<password>'
        )

        # Connect to S3
        pr.connect_to_s3(
            aws_access_key_id='<S3 access key>',
            aws_secret_access_key='<S3 secret>',
            bucket='tipico-events-raw',
            subdirectory='raw_data'
        )

        # Write the DataFrame to S3 and then to redshift
        pr.pandas_to_redshift(data_frame=df, redshift_table_name='dbt_wburchenal.tipico_events_raw', index=False,
                              append=True)

        print(f"API data stored in Redshift successfully at {datetime.now()}")
    else:
        print(f"Failed to call the API. Status code: {response.status_code}")


# Create the DAG
with DAG('tipico_event_dag', default_args=default_args, schedule_interval=timedelta(minutes=10)) as dag:
    # Define the task to call the API and store the data
    call_and_store_task = PythonOperator(
        task_id='call_and_store_api_data',
        python_callable=call_and_store_api_data,
        dag=dag
    )
