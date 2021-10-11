# social-media-data-harvester
### A platform for universal social media data harvesting.

## **Description** :

	This platform was designed to be a universal social media dataset generator,
	it collects the data using the NetworkExtractor according to a global schema which is predefined inside in the Model folder. 
	The resulting graph is passed through a Transformer class to apply any cleaning or restraints either on the schema or the data.
	The resulting graph is conducted through a canal to be received by the listening storage services. 
	



## **Dependendcies** : 

		Neo4J
		concurrent-utils
		erlang
		Pyvis (for test visuals)

## **rabbitmq-server** : (for result-publisher/listener- services)
        
		sudo apt-get update && sudo apt-get upgrade
        sudo apt-get install erlang
        sudo apt-get install rabbitmq-server
        sudo systemctl enable rabbitmq-server
        sudo systemctl start rabbitmq-server
        sudo rabbitmq-plugins enable rabbitmq_management

user is the username and password is the new password

        sudo rabbitmqctl add_user user password
giving that user adiministraitve rights

        sudo rabbitmqctl set_user_tags user administrator
        sudo rabbitmqctl set_permissions -p / user "." "." "."

    	pip install pika
    




## **Usage** : 
		
		# after installing
		start rabbitmq server
	   	sudo systemctl start rabbitmq-server
	    sudo systemctl enable rabbitmq-server
		#go to the publishing service to verify your channels
		#visit API_Models/ to view/modify schema models
