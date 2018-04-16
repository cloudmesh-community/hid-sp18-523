SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=process.yaml
FLASKDIR=server/process/flaskConnexion


docker-start:
	cd $(FLASHDIR); docker build -t ritandon/swaggerprocess .;docker run -p 8080:8080 ritandon/swaggerprocess;
	
docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

service: 
	sudo wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	#$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true
	
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true

	#cp -r data $(FLASKDIR)
	rm $(FLASKDIR)/swagger_server/controllers/default_controller.py
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers

run: 
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	curl http://localhost:8080/cloudmesh/process

start:
	python -m swagger_server
		            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9


container:
	cd $(FLASKDIR);	sudo docker build -t ritandon/swaggerprocess .;sudo docker run -p 8080:8080 ritandon/swaggerprocess;

osx:
	docker build -t cloudmesh-process .
	docker run -p 4000:80 cloudmesh-process 
