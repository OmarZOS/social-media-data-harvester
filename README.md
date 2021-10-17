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
	
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
	sudo add-apt-repository "deb https://debian.neo4j.com stable 4.1"
	sudo apt install neo4j
	sudo systemctl enable neo4j.service
	sudo systemctl status neo4j.service
	pip install neo4j
	# to interact with neo4j from CLI
	cypher-shell
	# allow remote connections
	sudo nano /etc/neo4j/neo4j.conf
	# add this line
	dbms.default_listen_address=0.0.0.0
    




## **Usage** : 
- **Networking :** go to the publishing service to verify your channels.
- **Schema models :** visit API_Models/ to view/modify schema models.
- **Execution :** go the the main.py file and launch it



## **Progress** : 
 - [ ] Current code consistency
 - [x] Multithreading 
 - [x] Graph oriented database storage
 - [ ] Document oriented database storage
 - [ ] Infrastructure as a service
 - [ ] Database as a service
 - [ ] Communications as a service
 - [x] **Twitter** support
 - [ ] **Youtube** support
 - [ ] **LinkedIn** support
 - [ ] **Facebook** support
 - [ ] **Instagram** support
 - [ ] Graphical user interface
 - [ ] Encrypting network circulating data

