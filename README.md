# social-media-data-harvester
A platform for universal social media data harvesting

Dependendcies : 

		Neo4J
		Pyvis (for test visuals)
		concurrent-utils
		erlang
		rabbitmq-server : (for result(publisher/listener) services)
        sudo apt-get update && sudo apt-get upgrade
        sudo apt-get install erlang
        sudo apt-get install rabbitmq-server
        sudo systemctl enable rabbitmq-server
        sudo systemctl start rabbitmq-server
        sudo rabbitmq-plugins enable rabbitmq_management

        ##user is the username and password is the new password
        sudo rabbitmqctl add_user user password
        ##giving that user adiministraitve rights
        sudo rabbitmqctl set_user_tags user administrator

        sudo rabbitmqctl set_permissions -p / user "." "." "."
    
    	pip install pika





Usage : 
		# after installing,
		start rabbitmq server
	   	sudo systemctl start rabbitmq-server
	    sudo systemctl enable rabbitmq-server
		#go to the publishing service to verify your channels
		#visit API_Models/ to view/modify schema models
