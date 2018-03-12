#!/bin/bash
echo "Create REST service for listing processes"


#swagger-codegen generate -i process.yaml -l python-flask -o server/process/flaskConnexion -D supportPython2=true

echo " Create server stub code"
java -jar swagger-codegen-cli-2.3.1.jar generate \
-i process.yaml \
-l python-flask \
-o server/process/flaskConnexion \
-D supportPython2=true

echo "Move controller file"
rm server/process/flaskConnexion/swagger_server/controllers/default_controller.py

echo "Move default_controller.py file from current folder to server controller folder"
cp default_controller.py server/process/flaskConnexion/swagger_server/controllers/default_controller.py

echo "Starting Virtual REST server"
virtualenv RESTServer
source RESTServer/bin/activate
cd server/process/flaskConnexion
pip install -r requirements.txt
python setup.py install

echo "Run the REST service"
python -m swagger_server





