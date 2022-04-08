#!/bin/bash
docker run --name airflow \
       -v $(pwd)/dags:/app/airflow/dags \
       -v $(pwd)/plugins/:/usr/local/airflow/plugins \
-p 8080:8080 -d airflow:latest
