## End to End Datascience project

import dagshub
dagshub.init(repo_owner='lenkabineet02', repo_name='ml-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)