SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=prediction.yaml
FLASKDIR=server/prediction/flaskConnexion
SERVERDIR=./server

all: service docker-build docker-start

service: 
	#sudo wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true

	#cp -r data $(FLASKDIR)
	rm $(FLASKDIR)/swagger_server/controllers/default_controller.py
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers
	#cp -r train.csv $(FLASKDIR)/swagger_server/controllers
	#cp -r test.csv $(FLASKDIR)/swagger_server/controllers
	#cp -r train.csv $(FLASKDIR)
	#cp -r test.csv $(FLASKDIR)

run: 
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/prediction
	
		            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9


docker-build:
	rm $(FLASKDIR)/Dockerfile
	cp -r Dockerfile $(FLASKDIR)/
	cd $(FLASKDIR); sudo docker build -t cloudmeshprediction .; 

docker-start:
	docker run -p 8080:8080 cloudmeshprediction


clean:
	rm -r $(SERVERDIR)
	#rm -f ./swagger-codegen-cli-2.3.1.jar

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

