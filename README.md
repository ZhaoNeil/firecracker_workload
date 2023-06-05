# firecracker_workloads adapted from [serverless-faas-workbench](https://github.com/ddps-lab/serverless-faas-workbench)
## How to run:
python:
`python3 lambda_function.py [arguments]`

java Fibonacci:
```
javac Fibonacci/Fibonacci.java
java Fibonacci/Fibonacci 100
```
java [Tomcat](https://devcenter.heroku.com/articles/create-a-java-web-application-using-embedded-tomcat):
```
cd Tomcat
mvn package
sh target/bin/webapp   
```
## Not included workloads:
### cpu-memory:
feature_generation, mapreduce, model_serving
### network:
s3_download_upload
