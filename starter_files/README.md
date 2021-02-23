# Operationalizing Machine Learning

## Overview
This project is part of the Udacity Azure ML Nanodegree.

In this project, we use Azure to **configure a cloud-based machine learning production model, deploy it, and consume it**.
We will also create, publish, and consume a pipeline.

## Architectural Diagram

In this project, we explain briefly how to publish your best AutoML model and deploy it as a Web API.

- **Experiment Run**: Using MLStudio we manually upload data, select the compute 
  target and the task we want to accomplish
- **Best Model Selection**: Comparing all the models, finally we choose the one with better primary metric, in this case, weighted AUC, according to the target unbalance.
- **Model Deployment**: The best model is deployed as an endpoint.
- **Application Insights Activation**: We enable this logs monitoring tool.
- **Display Swagger Documentation**: We make use of the *swagger.json* file
 given by Azure to visualize documentation in a more clear and professional way.
- **Consume Endpoint**: We do a test and a benchmark to check out that the 
endpoint works and to better know latency times.
- **Create, Publish and Consume a Pipeline using Python SDK**: In the top of 
Automation we have the pipelines. Processing data and retraining only with an
HTTP request is possible.

![architecture](img/architecture.png)

## Key Steps
### **1. Data Preparation**: When AutoML run is created, *Bank-Marketing* data is uploaded and registered so that we can use it in our experiments.
![imgdatareg](img/AutoML-RegData.png)    


   **Personal information**: Occupation, age, marital status and education.

   ![imgpersonal](img/personal_data.png)

   **Financial information**: Debts and other data about customer's financial health.

   ![imgfinance](img/financial_data.png)

   **Target**: The variable we seek to predict is the one that tells us if a given person is a potential client or not.
   
   ![imgtarget](img/target.png)
   <!-- <img src="img/AutoML-RegData.png" width="800" height="250" /> -->
### **2. Experiment Run**: AutoML experiment correctly run and submitted.
![imgexprun](img/AutoML-ExpRun.png)

### **3. Best Model**: The best performing model is the one using *VotingEnsemble*.
As it was mentioned in **ML-Pipeline** project, due to the high target unbalancement, we're going to focus on *macro* metrics.
![imgexprunrrank](img/AutoML-Runs.png)
![imgbestperfmod](img/BestModelPerf.png)

### **4. Deploy Model**: Create an endpoint associated to an ACI.

![imgmoddep](img/AutoML-Deployed.png)  

### **5. Activate Application Insights**:
   1. Check out *az* extension is installed with `az version` and `az extension add -n azure-cli-ml`.
   2. Create a python virtual environment with `virtualenv venv`.
   3. Edit and run `logs.py` writing the endpoint name (`demo-model-deploy` in 
      this case) and check output in console:
   ![appins](img/logs_activ.png)    
   1. Check that **Application Insights** is enabled and wotking:
   ![appinsenab](img/appins_enabled.png)
   ![appinswork](img/mlappins.png)

### **6. Display Swagger Documentation**
   1. Download swagger.json from *Details* tab inside the endpoint.
   2. Change port from recommended `80` to `9000` in `swagger.sh` because 80 is
      not available and run it to start the `swagger-ui` docker container. Now it 
      is displayed in `http://localhost:9000/`.
   3. Run server.py in 8000 port
   4. Check `http://localhost:8000/swagger.json` in `Swagger`.
      ![swagger](img/swagger.png)

### **7. Consume Endpoint and benchmarking**
   1. Edit *endpoint.py* with the URL and the key necessary to authorize the HTTP
      request. Some data in a json format is used to make the request and see
      what the best model predicts from it.
      ![endpoint_script](img/endpoint_script.png)
      ![endpoint_call](img/endpoint_call.png)
   2. Now we want to know the average time necessary to receiver our responses.
      For that we use **Apache Benchmark**. First of all we check that it is
      installed displaying the help `ab -h`. Once we see that it works, 
      Authorization key and URI can be introduced into *benchmark.sh* and run 
      the script.
      ![apache_script](img/benchmark_script.png)
      ![apache_out](img/benchmark_out.png)
      
      We can see that, calling 10 times the API with a *data.json* POST (the 
      same used for testing the endpoint) we see that all of them are done 
      without issues in 226 ms in average. This is a very acceptable responsing 
      time.

### **8. Create, Publish and Consume a Pipeline**
   1. Upload the Jupyter Notebook that contains the process of the Pipeline creation
      and change the experiment name so that it's the same used for AutoML.
   2. Upload the `config.json` with the info about the workspace.
   3. Using Python SDK, run the AutoML step and publish the Pipeline so that we
      can find it in MLStudio Pipelines section.
      ![published](img/pipeline_rundetails.png)
      ![published](img/pipeline.png)
   4. Deploy it creating an HTTP endpoint.
      ![published](img/pipeline_endpoints.png)
      ![published](img/pipeline_flow.png)
   5. Authenticate using interactive login and make a POST request with the 
      new experiment name so that a new Pipeline run is executed. 

## Screen Recording
Clicking on the following picture you can watch a **5 minutes video** with 
explanations about the content of the project.

[<img src="img/AzureAI.png">](https://youtu.be/NDL4-IqeMsU)

## Standout Suggestions

For future work, I would suggest making further tweaks to the AutoML step of the pipeline. There are a lot of settings involved and making changes to them could improve the search space and help find an even better model solution. There are also additional steps that could be added to the pipeline, perhaps doing some dataset cleanup or feature engineering before the AutoML step, or doing additional steps after the AutoML step has completed.

In addition, I propose connecting Application Insights to our Pipeline API and 
Scheduling periodical runs or each time Banking Dataset updates (trigger). 
