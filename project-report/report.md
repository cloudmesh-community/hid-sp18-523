# SciKit Learn Algorithms with Rest API :wave: hid-sp18-520 hid-sp18-523

| Arijit Sinha, Ritesh Tandon
| arisinha@iu.edu, ritandon@iu.edu
| Indiana University Bloomington
| hid: hid-sp18-520, hid-sp18-523
| github: [:cloud:](https://github.com/cloudmesh-community/hid-sp18-523/tree/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/hid-sp18-523/tree/master/project-code)

---

Keywords: docker, Scikit, AWS, Azure, Linear Regression, Boosted Decision

---

## Abstract

In current world, data is getting generated and stored with different 
storage systems. We need to use this data for a better understanding, 
analyze and can estimate the future scenarios with certain probability. 
There are many algorithms, which have developed and implemented for 
providing better accuracy on the future scenarios.

## Introduction

Scikit learn is a library created for machine learning algorithms,
which uses different datasets gathered over years to learn and predicts
future scenarios. This library have methods for implementing supervized
and unsupervized machine learning algorithm.
Supervised algorithms are on the dataset, which has the target variable,
which need to be predicted or estimated. This datasets can be acted with
below different approaches
Classification is based on the classes and the labeled data, we need to
predict the unlabeled data.
Regression is based on the continuous variable or data, we need to
predict the future state of data is known as regression
Unsupervised algorithms are on the dataset, where we do not see the
target variable for prediction, we learn its behavior set of vector
input variable to identify the clustering group of similar behavior data
or sample  @sckitml Kaggle is a known location for different kind of
datasets gathered by various institutes across globe.

## Scope of work

Below are the 3 algorithm from Scikit learn

* Implement Linear Regression
* Implement Boosted Decision
* Implement Hyper-tuned Boosted Decision

## Reason

We are planning to use Regression learning algorithm because the target
variable is numerical and continuous in nature. We will be creating ML
pipeline using linear, regularized linear, tree and forest learning
algorithm. We will compare and evaluate different models based on RMSE
of learning algorithm. [@sckitml]

## Technology Stack

Python will be used for Data loading, preprocessing and cleaning. Using
Scikit learn library, we will implement variety of algorithms to conduct
above process and finally will predict the sale price of its products.

REST services has been implemented to provide a prediction of price of
the products:

* REST data preprocessing: It will be the service, which does the data
  processing with removal or imputing the data with mean or median.
  Removal of the columns which doesn’t any correlation with target
  variable
* REST data prediction: it will be the service, which will do multiple
    predictions using multiple algorithms as below
* Rest API with Linear Regression – Display the outcome of product and
  predicted price
* Rest API with Boosted Decision – Display the outcome of product and
  predicted price
* Rest API with Hyper-tuned Boosted Decision – Display the outcome of
  product and predicted price

Cloud technology utilized will be Microsoft Azure, AWS, it has been
implemented at Local machine and Docker.
We have acquired the dataset from Kaggle and read the data dictionary
details on different websites which includes below describes attributes.
We have 14204 instances and 13 attributes in the dataset, which will be
spitted into Training and Test Data set. This dataset is available on
public websites
BigMart Dataset, With this dataset, we will predict the sale price of
various products based on the learning of historical data in the
datasets using different algorithm. The dataset has various data with
respect to

* Item Fat Content
* Item Identifier
* Item MRP
* Item Outlet Sales
* Item Type
* Item Visibility
* Item Weight
* Outlet Establishment Year
* Outlet Identifier
* Outlet Location Type
* Outlet Size
* Outlet Type
* source

[@kaggleds]

## Dataset Details

It has following 12 attributes with continuous and categorical values
with Unique Values

* Item Fat Content has 5 unique values
* Item Identifier has 1559 unique values
* Item MRP has 8052 unique values
* Item Outlet Sales has 3494 unique values
* Item Type has 16 unique values
* Item Visibility has 13006 unique values
* Item Weight has 416 unique values
* Outlet Establishment Year has 9unique values
* Outlet Identifier has 10 unique values
* Outlet Location Type has 3 unique values
* Outlet Size has 4 unique values
* Outlet Type has 4 unique values

## Data Visualization

The histogram in +@fig:HistogramofImportantAttributes shows the distribution of data of different variables. :o: I still do not understand this.

![Histogram of Important Attributes](images/HistrogramofImpAttributes.png){#fig:HistogramofImportantAttributes}

Correlation plot informs about the relation between variables

![Correlation Matrix between Variables](images/Correlation.png){#fig:CorrelationMatrixbetweenVariables}

## Data Exploration

Analyzed and plotted the categorical and continuous feature summaries to
see which feature is closely related with target variable. This helped
us with deciding which feature are influencing the prediction.

## Data Preprocessing

* Missing values (2439) of item weight is replaced with mean.
* Missing values (4016) of outlet size observations, which been
  replaced with mode.

## Azure ML Studio

Azure ML studio provides the GUI interface for creating the Machine
Learning Train models and Predictions. It provides a provision to
integrate with Azure Cloud and expose the Web Services

## Train Model with Azure

Created on Azure ML Studio, 3 Learning Algorithms used

* Boosted Decision Tree
* Linear Regression
* HyperTuned Boosted Decision Tree

From the RMSE results, Hyper-tuned Boosted Decision Tree has provided
better results.

![RMSE Comparision Results](images/RMSEComparison.png){#fig:RMSEComparisionResults}

![Hypertuned Algorithm RMSE Comparision](images/RMSEComparisionBetweenHypertune.png){#fig:HypertunedAlgorithmRMSEComparision}

## Predictive Model

Update the Trained model with Test dataset for predicting the Item
Outlet Sales data. Verified and updated the data cleaning process which
we have implemented for Train dataset. After converting the categorical
data with indicators, we can apply the trained model.

Created predictive model using the above Hyper-tuned Boosted Decision
Tree.

From the score function, have extracted only 2 columns

* Item Identifer
* Item Outlet Sales

Create the Web service input and Web service Output.

![Output of Prediction from Models](images/PredictionOutputfromModel.png){#fig:OutputofPredictionfromModels}

## Web Service Deployment

Once the Prediction model has been executed successfully, it can be
deployed as web service from Azure ML Studio.

It will generate the API key, which will be used for Azure Cloud
deployment.

![Azure MLStudio Webservice Deploy](images/Webservicedeploy.png){#fig:AzureMLStudioWebserviceDeploy}

It will provide an option to Test web service locally with below options

* Click on Test button enabled at the bottom of the screen
* Download the CSV file from the tool to test the Web API with
    prediction model.

## Azure Cloud deployment

Once Web Service is created locally, It creates a hyper link
with name of the web service. On clicking this hyperlink 
service dashboard opens up that let the develop set up and 
configure web service on Azure cloud for consumption.

It provides test tab on the dashboard where we can provide
inputs and get the prediction values given by model after 
clicking on Test Request response button.

This step will assure that, the web services are working as expected.

![WebService Configration Details](images/Webserviceconf.png){#fig:WebServiceConfigrationDetails}

After clicking consume tab from Dashboard, It will display option for
Response Request Web Template link.

Copy the request response link generated on the page.

Once clicked on the link, it will redirect to Azure cloud configuration
using Response Request Web application.

Azure ML Request, Response Service Web App In Azure cloud, it need to
created as

* Create the request response service web app
* Create Resource Group
* Add Model Management services
* Click on the URL link generated under resource group
* Update the Settings with API POST URL
* Update the API key generated from Web service from Azure ML studio.

Expose the Web Service from Azure cloud

Click on the below link to access the prediction web service
* <https://predictbigmart.azurewebsites.net/>

Entered the values used to for testing locally, the amount should match
so as to see if the service is functioning as expected.

![WebService Result](images/WebService.png){#fig:WebServiceResult}

Batch Mode for Web Service Execution Download the CSV generated from
Azure ML Studio

* Open the CSV, it will be open with Web API built in
* Use Sample data link on the API
* Select the range of columns and provide as input to API
* Select the cell from where the prediction values needs to be
  displayed.
* Click on Prediction button. It will generate the prediction values
  for all the selected Input entries with Item Identifiers.

![Built API on CSV File](images/csvscreenshot.png){#fig:BuiltAPIonCSVFile}

## Drawback of using Azure ML Studio

Azure ML studio provides easy to use drag and drop objects for
all steps ( from model intialization to deployment ) such as 
data preprocessing, training model, fitting model, evaluating 
model, tuning model and prediction. It is every easy to use and
handy tool for data scientists and data engineer. However, it has 
a drawback; developers are not able to generate the code that is 
generated at the backend for further experimentation and testing.


## Azure with Notebook Instance

Notebook instance of Azure ML Studio was used to execute python
code file for benchmarking. Code containing data preprocessing, 
training model, fitting model, evaluating model, tuning model and 
prediction steps was executed on Azure notebook instance. 
It took 15.2 ms for overall batch prediction using notebook. 
Computation time using model saved on disk was recorded  as 
1.95 micro secs.


```
line 1
line 2
```

![Azure Notebook Screenshot](images/Azurenotebookscreenshot.png){#fig:AzureNotebookScreenshot}

## AWS with Notebook Instance

AWS Sagemaker service was used to benchmark performance of
model on AWS cloud. Python notebook file containing code for
data preprocessing, training model, fitting model, evaluating 
model, tuning model and prediction was executed on AWS notebook
instance. 
Execution time of prediction was captured for comparison.
It took 8.2 ms for overall batch prediction using notebook. 
Computation time using model saved on disk was recorded  as 
371 micro secs.

```
line 1
line 2
```

![AWS Notebook Screenshot](images/AWSnotebookscreenshot.png){#fig:AWSNotebookScreenshot}

## LocalMachine Instance

Python notebook file was executed on local instance for comparing 
performance with cloud. Data preprocessing, training, fitting and 
prediction steps were performed on local python instance.
Start time and end time was recorded and execution time was calculated.
It was observed that execution and prediction took more time compared
to execution time on cloud. It took approximately 10 minutes on local
instance.

Start time

![Local Machine Start Time](images/Starttimelocal.png){#fig:LocalMachineStartTime}

Endtime

![Local Machine End Time](images/EndTimelocal.png){#fig:LocalMachineEndTime}

## Docker

Docker Image was created on local environment. Excution of docker image of
model predict prices for passed dataset. This code can be reproduced  
using Docker commands.
Once replicated locally, running locahost website created by docker
image on port- 8080 will predict prices of all items of datset.

Link for localhost 

* <http://localhost:8080/cloudmesh/prediction>

## Conclusion

In this project, below two models have been implemented and hyper-tuned. 

* Boosted Decision
* Linear Regression
* HyperTuned Boosted Decision

Best model was decided based on accuracy and that was used for prediction
of sales price of items across all store outlets.

Model was  deployed on Azure Cloud, AWS Cloud and Local machine for 
predicting prices. Docker image was created for reproducing. 
Performance was benchmarked on different cloud and local environment. 
On comparison we observed that prediction performance
was best on AWS cloud.

## Performance Comparison

Environment  | Description       |  Elapsed Time
-------------|-------------------|----------------
Azure Cloud  | Notebook Instance |  15.2 ms
AWS Cloud    | Notebook Instance |  8.2 ms
Local        | Python Instance   |  9 min 10 s


## Appendix

Web service was deployed on Azure Cloud. Weservice endpoints
was exposed to predict price of passed Item Identifiers. 

Deployment and usage playback Video of using exposed webservice 
endpoint is uploaded at below location

* <https://www.youtube.com/watch?v=xrLto4XPn1o&t=518s>

## Acknowledgement 

The authors would like to thank Dr. Gregor von Laszewski for his support
and suggestions to write this paper.

## Workbreakdown

Arijit and Ritesh worked on data processing,Data exploration and designing 
the Machine learning Algorithms. We both have brainstromed on visualizing 
data. Arijit worked on Azure cloud and creating web service and Ritesh 
worked on Docker image creation on local machine. We both worked on 
comparing performance benchmarks. Compared the time running on AWS cloud 
to prepare the time comparision chart and project report.
