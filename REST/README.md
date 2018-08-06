# REST Services with Eve  

* Install eve module on local machine using below command

```$sudo pip install eve```
    
* Download the REST git repository on your local machine
    
* Verify the settings.py and run.py available in eve folder
    
* Execute below command from within folder that contains run.py file

```$python run.py```


## Run below URL in browser to View all details of system - 

http://localhost:5000/mysystemdetails/alldetails

![Eve Browser](https://github.com/cloudmesh-community/hid-sp18-523/blob/master/REST/rest-eve-browser-result.PNG)


## Run below command in terminal to view result using curl - 
 
curl -H "Content-Type: application/json" http://localhost:5000/mysystemdetails/alldetails


![Eve Curl](https://github.com/cloudmesh-community/hid-sp18-523/blob/master/REST/rest-eve-curl-result.PNG)
