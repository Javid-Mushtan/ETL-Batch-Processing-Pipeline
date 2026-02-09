from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

LOCATION = 'us-central1'
PIPELINE_NAME = 'ETL_Pipeline'
INSTANCE_NAME = 'datafusion-dev'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['javidmushtan@gmail.com'],
    'email_on_failure': False,  # Disabled email due to SMTP config issue
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    'employee_data',
    default_args=default_args,
    description='Extract employee data',
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    extract_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py',
    )

    start_datafusion_pipeline = CloudDataFusionStartPipelineOperator(
        task_id="start_datafusion_pipeline",
        location=LOCATION,
        pipeline_name=PIPELINE_NAME,
        instance_name=INSTANCE_NAME,
        asynchronous=True,
    )

    extract_task >> start_datafusion_pipeline