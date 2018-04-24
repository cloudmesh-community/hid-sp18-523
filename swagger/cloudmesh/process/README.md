# REST Service for listing processes details with Swagger

Dockerfile and Makefile format was adopted from Kadupitiya ( 409 ) and Arijit ( 520 )

## Objective :

* This REST API is intended to list processes details ( CPU, Memory etc ) on the server it is running 

* Note - This was created on Ubuntu 16.04. One should have swagger-codegen-cli-2.3.1.jar installed and specified
in Environment variable. It also requires virtualenv to be installed on Ubuntu 16.04


# Steps to reproduce service code, build docker image and run in docker container
 
Make file has following commands.Execute below commands from the Makefile to create REST service , create docker image
and run it in docker container locally.

Run following command to create service

```make service```

Run following command to build and create docker image

```make docker-build```

Run following command to run docker image service inside docker container

```make docker-start```

Run following command to test the service that runs in local docker container

```make test```

Alternatively access following url to view service result in browser

```http://localhost:8080/cloudmesh/process```

Run following command to clean. This will remove the server folder and delete the .jar file

```make clean```


 
# Details ( steps ) of creating service, executing and testing locally without Docker

## Steps for creating the Server and client ( Manual Execution ) :

* On Ubuntu - Create a file "process.yaml" file that contains definition/structure of the service
* Generate Server Side Stub Code using swagger-codegen jar(swagger-codegen-cli-2.3.1.jar) by running following command. 
java -jar swagger-codegen-cli-2.3.1.jar generate
    -i ~/github/cloudmesh-community/hid-sp18-523/Swagger/cloudmesh/process/process.yaml
    -l python-flask
    -o ~/github/cloudmesh-community/hid-sp18-523/Swagger/cloudmesh/process/server/process/flaskConnexion
    -D supportPython2=true
* Update the code of default_controller.py under ~/github/cloudmesh-community/hid-sp18-523/cloudmesh/process/Swagger/server/process/flaskConnexion folder.
* Install the virtualenv environment.
* Run the REST service under virtual environment
* Execute below code for Installing and generating Client side code under virtualenv environment. 
java -jar swagger-codegen-cli-2.3.1.jar generate
    -i ~/github/cloudmesh-community/hid-sp18-523/Swagger/cloudmesh/process/process.yaml
    -l python
    -o ~/github/cloudmesh-community/hid-sp18-523/Swagger/cloudmesh/swagger/myclient/process
    -D supportPython2=true

## Create Bash Shell Script ( Local without Docker ):

* Create the Bash Shell scripts that will generate the server stub code using yaml,replace the implementation of controller file, install the serber and run the service on virtualenv

* Execute the bash script - process_bash_script.sh

## Server:

* Create the Bash Shell scripts which will download the Swagger Codegen 2.3.1 and create the Server with Code and Virtual Environment.

* Execute the bash script mybashscript_Server.sh

## Client:

* Create the Bash Shell script to generate the client code and run using virtualenv.

* Execute the bash script - process_bash_script_Client.sh

## Execute REST service API:

Create the Bash Shell scripts to generate the client code and run using virtualenv.

Execute the bash script - process_bash_script_Client.sh


## Test the service ( Local without Docker ):

* Through Browser 
	- Verify the service by typing http://localhost:8080/cloudmesh/process. 


* Through curl 
	- curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/process

* Through Python Client 
	-Create and Execute the "process_bash_script_Client.sh".It will start the REST Client in virtualenv
	-$python process_client.py



![Process Image](https://github.com/cloudmesh-community/hid-sp18-523/blob/master/swagger/cloudmesh/process/images/process-screen-shot.PNG)


