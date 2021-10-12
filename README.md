# social-media-data-harvester
### A platform for universal social media data harvesting.

## **Description** :

	This platform was designed to be a universal social media dataset generator,

	it collects the data using the NetworkExtractor according to a global schema which is predefined inside in the Model folder.

	The resulting graph is passed through a Transformer class to apply any cleaning or restraints either on the schema or the data.

	The final graph is conducted through a canal to be received by the listening storage services. 
	



## **Dependendcies** : 

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
	
	pip install neo4j
	

    




## **Usage** : 
- **Networking :** go to the publishing service to verify your channels.
- **Schema models :** visit API_Models/ to view/modify schema models.
- **Execution :** go the the main.py file and launch it



## **Progress** : 
 - [x] Current code consistency
 - [x] Multithreading 
 - [x] Graph oriented database storage
 - [ ] Document oriented database storage
 - [x] **Twitter** support
 - [ ] **Youtube** support
 - [ ] **LinkedIn** support
 - [ ] **Facebook** support
 - [ ] **Instagram** support
 - [ ] Graphical user interface

