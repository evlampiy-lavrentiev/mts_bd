from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator


default_args = {
            'owner': 'airflow',
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'start_date': '2023-12-05',
            'retries': 1,
            'retry_delay': timedelta(minutes=49),
            'catchup': False
}

dag = DAG(dag_id='testing_stuff',
          default_args=default_args,
          schedule_interval='50 * * * *',
          dagrun_timeout=timedelta(seconds=1200),
          concurrency=1,
          max_active_runs=1,
    )

t1_bash = """
curl -L -o out_file.zip 'https://drive.google.com/uc?export=download&id=1vv959xARGmlzKsaFmZe-Z9DG2NKeUzOX'
"""
t2_bash = "unzip -o out_file.zip"

t3_bash = """/usr/local/hadoop/bin/hdfs dfs -put Netflix%20TV%20Shows%20and%20Movies.csv /netflix_$(date +"%d-%m-%Y_%H-%M-%S")"""

t4_bash = "echo 'Hello world!'"

t5_bash = "rm out_file.zip"
t6_bash = "rm 'Netflix TV Shows and Movies.csv'"

t7_bash = "python3 convert.py"

t1 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='get_dataset_from_web',
                 command=t1_bash,
                 dag=dag)

t2 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='unpack_archive',
                 command=t2_bash,
                 cmd_timeout=300,
                 dag=dag)

t3 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='load_to_hdfs',
                 command=t3_bash,
                 cmd_timeout=300,
                 dag=dag)

t4 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='run_MR_job',
                 command=t4_bash,
                 dag=dag)

t5 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='delete_archive',
                 command=t5_bash,
                 dag=dag)


t6 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='delete_csv',
                 command=t6_bash,
                 dag=dag)

t7 = SSHOperator(ssh_conn_id='ssh_default',
                 task_id='convert',
                 command=t7_bash,
                 dag=dag)

t1 >> t2 >> t3 >> t4 >> t7 >> t5 >> t6
