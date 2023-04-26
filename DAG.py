

from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from extract_transform.app import extract_and_transform
from load.load_csv import load_data_to_csv 

#defining DAG arguments
default_args = {
    'owner': 'Samy',
    'start_date': days_ago(0),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_TWITTER',
    default_args=default_args,
    description='Extract, Transform and Load Twitter data',
    schedule_interval=timedelta(days=20),
)


# define the task extract and transform
extract_transform_data = PythonOperator(
    task_id='extract-transform',
    python_callable=extract_and_transform,
    dag=dag
)


# define the task laod
load = PythonOperator(
    task_id='load',
    python_callable=load_data_to_csv,
    dag=dag
)

# task pipeline
extract_transform_data >> load