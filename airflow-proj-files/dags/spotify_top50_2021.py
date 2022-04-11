from datetime import datetime, timedelta
from random import randint

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.papermill_operator import PapermillOperator
from airflow.operators.python import BranchPythonOperator


## from airflow.utils.dates import days_ago

## import pandas as pd
## import matplotlib
## matplotlib.use("Agg")
def _spotify_top50_2021():
    return randint(1, 10)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}
with DAG(
        dag_id='example_papermill_operator',
        default_args=default_args,
        start_date=datetime(2022, 4, 10),
        schedule_interval='@daily',
        template_searchpath='/Users/madhavirockandla/AirflowWeekend/airflow-proj-files/',
        catchup=False) as dag:
    run_this = PapermillOperator(
        task_id="run_spotify_top50_2021",
        input_nb="/airflow-proj-files/spotify_top50_2021.ipynb",
        output_nb="/airflow-proj-files/out-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
    )

with DAG(
        dag_id="spotify_top50_2021",
        default_args=default_args,
        start_date=datetime(2022, 4, 10),
        schedule_interval='0 0 * * *',
        template_searchpath='/Users/madhavirockandla/AirflowWeekend/airflow-proj-files/',
        catchup=False) as dag:
    spotify_top50_2021 = PythonOperator(
        task_id="spotify_top50_2021",
        python_callable=_spotify_top50_2021
    )
    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_spotify_top50_2021
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )

# def import_raw_data():
#   # Imports raw data and returns a DataFrame
#   raw_data = pd.read_csv(
#      '/Users/madhavirockandla/AirflowWeekend/airflow-proj-files/data/spotify_top50_2021.csv')
#  pd.DataFrame(raw_data)
