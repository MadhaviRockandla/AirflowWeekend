## Using Docker to handle Airflow

for running
```
docker run --name airflow -p 8080:8080 -d airflow:latest
```

for building
```
time docker build --tag airflow:latest .
```

This is SOOO much better than trying to onstall it on your machine. Use Docker to handle all the isolation aspects of running airflow.

