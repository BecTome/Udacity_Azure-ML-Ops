# Operationalizing Machine Learning

## Overview
This project is part of the Udacity Azure ML Nanodegree.

In this project, we use Azure to **configure a cloud-based machine learning production model, deploy it, and consume it**.
We will also create, publish, and consume a pipeline.

## Summary

**Personal information**: Occupation, age, marital status and education.

![imgpersonal](img/personal_data.png)

**Financial information**: Debts and other data about customer's financial health.

![imgfinance](img/financial_data.png)

**Target**: The variable we seek to predict is the one that tells us if a given person is a potential client or not.
 
![imgtarget](img/target.png)


## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
1. **Data Preparation**: When AutoML run is created, *Bank-Marketing* data is uploaded and registered so that we can use it in our experiments.
![imgdatareg](img/AutoML-RegData.png)    

<!-- <img src="img/AutoML-RegData.png" width="800" height="250" /> -->
2. **Experiment Run**: AutoML experiment correctly run and submitted.
![imgexprun](img/AutoML-ExpRun.png)

3. **Best Model**: The best performing model is the one using *VotingEnsemble*.
As it was mentioned in **ML-Pipeline** project, due to the high target unbalancement, we're going to focus on *macro* metrics.
![imgexprunrrank](img/AutoML-Runs.png)
![imgbestperfmod](img/BestModelPerf.png)

4. **Deploy Model**: Create an endpoint associated to an ACI.
![imgmoddep](img/AutoML-Deployed.png)  

5. **Activate Application Insights**:
   1. Check out *az* extension is installed with `az version` and `az extension add -n azure-cli-ml`.
   2. Create a python virtual environment with `virtualenv venv`.
   3. Edit and run `logs.py` writing the endpoint name (`demo-model-deploy` in 
      this case) and check output in console:
   ![appins](img/logs_activ.png)    
   4. Check that **Application Insights** is enabled and wotking:
   ![appinsenab](img/appins_enabled.png)
   ![appinswork](img/mlappins.png)

6. **Display Swagger Documentation**
   1. Download swagger.json from *Details* tab inside the endpoint.
   2. Change port from recommended `80` to `9000` in `swagger.sh` because 80 is
      not available and run it to start the `swagger-ui` docker container. Now it 
      is displayed in `http://localhost:9000/`.
   3. Run server.py in 8000 port
   4. Check `http://localhost:8000/swagger.json` in `Swagger`.
      ![swagger](img/swagger.png)

7. **Consume Endpoint and benchmarking**
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
## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
