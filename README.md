# social-media-data-harvester
### A platform for universal social media data harvesting.

## **Description** :

	This platform was designed to be a universal social media dataset generator,
	it collects the data using the NetworkExtractor according to a global
	 schema which is predefined inside in the Model folder.
	The resulting graph is passed through a Transformer class to apply any cleaning or
	 restraints either on the schema or the data.
	The final graph is conducted through a canal
	 to be received by the listening storage services. 
	



## **Dependendcies** : 

	Docker
	Neo4J
	concurrent-utils
	erlang
	rabbitmq-server
	Pyvis (for test visuals)

## **rabbitmq-server** : (for results publishing/listening functionality)
        
	sudo apt-get update && sudo apt-get upgrade
	sudo apt-get install erlang
	sudo apt-get install rabbitmq-server
	sudo systemctl enable rabbitmq-server
	sudo systemctl start rabbitmq-server
	sudo rabbitmq-plugins enable rabbitmq_management

Adding an account

	sudo rabbitmqctl add_user username password
	
Giving that user adiministraitve rights

	sudo rabbitmqctl set_user_tags username administrator
	sudo rabbitmqctl set_permissions -p / username "." "." "."
	pip install pika
	# enabling the service
	start rabbitmq server
	sudo systemctl start rabbitmq-server
	sudo systemctl enable rabbitmq-server


## **Neo4j** :

You can choose the native or containerised one (or both!!).
	
### **native Neo4j** :
	
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
	sudo add-apt-repository "deb https://debian.neo4j.com stable 4.1"
	sudo apt install neo4j
	sudo systemctl enable neo4j.service
	sudo systemctl status neo4j.service
	pip install neo4j
	# to interact with neo4j from CLI
#### **Cypher Shell:**
	# allow remote connections
	sudo nano /etc/neo4j/neo4j.conf
	# add this line
	dbms.default_listen_address=0.0.0.0
    
### **Neo4j container** :
	
	#getting the image for the first time
    docker pull neo4j
	docker pull confluentinc/cp-server    

	#running the container
	docker run \
		--name testneo4j \
		-p7474:7474 -p7687:7687 \
		-d \
		-v $HOME/neo4j/data:/data \
		-v $HOME/neo4j/logs:/logs \
		-v $HOME/neo4j/import:/var/lib/neo4j/import \
		-v $HOME/neo4j/plugins:/plugins \
		--env NEO4J_AUTH=neo4j/test \
		neo4j:latest

	#optional : to run neo4j as the current user@group, replace --env NEO4J_AUTH=neo4j/test
	docker run \
    ... \
    --user="$(id -u):$(id -g)" \
    neo4j:latest

#### **Cypher Shell:**
	#launch the container in interactive mode
	docker exec -it testneo4j bash

	#enter credentials (user,password)
	cypher-shell -u neo4j -p test

## **kafka container** :
	
	docker pull mongo
	docker pull confluentinc/cp-schema-registry
	docker pull cp-enterprise-control-center


## **Usage** : 
- **Networking :** go to the publishing service to verify your channels.
- **Schema models :** visit API_Models/ to view/modify schema models.
- **Execution :** go the the main.py file and launch it



## **Progress** : 
 - [ ] Current code consistency
 - [x] Multithreading 
 - [x] Containerisation
 - [ ] Natural language processing
 - [x] Graph oriented database storage
 - [ ] Document oriented database storage
 - [ ] Infrastructure as code
 - [ ] Database as a service
 - [ ] Communications as a service
 - [x] **Twitter** support
 - [x] **Youtube** support
 - [ ] **LinkedIn** support
 - [ ] **Facebook** support
 - [ ] **Instagram** support
 - [ ] Graphical user interface
 - [ ] Encrypting network circulating data

