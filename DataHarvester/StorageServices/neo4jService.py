
from neo4j import GraphDatabase
import json 
import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# from .StorageService import StorageService
# from StorageServices.StorageService import StorageService




class neo4jService:#(StorageService)

    def __init__(self,scheme,host_name,port, user, password):
        #url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host_name, port=port)
        url=scheme+"://"+host_name+":"+str(port)
        print(url)
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        self.driver.close()

    ###########  FIND PERSON ###########
    def find_person(self, person_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_person, person_id)
            
            if len(result)==0:
                 
                return False
            else:
                return True
                for record in result:
                    print("Found person: {record}".format(record=record))

    @staticmethod
    def _find_and_return_person(tx, person_id):
        query = (
            "MATCH (p:Person) "
            "WHERE p.id = $person_id "
            "RETURN p.id AS id"
        )
        result = tx.run(query, person_id=person_id)
        return [record["id"] for record in result]
    
    
    #####Create NODES  ###########
    def create_NODE(self, F_json):
        with open(F_json) as file:
            db = json.load(file)
        for item in db['nodes']:
            id_person=str(item['id'])
            
            if self.find_person(id_person)==True:
                
                 
                continue 
            with self.driver.session() as session:
                
                result = session.write_transaction(self._create_node,item )
                """"for record in result:
                    
                    print("Created friendship between: {p1} ".format(p1=record['p1'] ))"""

    def saveData(data):
        pass
    def queryData(args):
        pass
        

      
    @staticmethod
    def _create_node(tx, item ):

        
        list_key=item.keys()
        query = "CREATE (p1:Person {"
        s=1
        for a in item.keys():
            if s==len(list_key):
                val1=str(item[a])
                val=val1.replace(" ","\ ")
                val=val.replace(",","\,")
                val="\""+val+"\""
                query=query+str(a)+":"+str(val) 
            else:
                 val1=str(item[a])
                 val=val1.replace(",","\,")
                 val=val.replace(" ","\ ")
                 val="\""+val+"\""
                
                 query=query +str(a)+":"+str(val)+" , "
                 s=s+1
        query=query+" })"#+ "RETURN p1"
        q=(query)
           
        result = tx.run(q)
        try:
            x=1 
              
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{q} raised an error: \n {exception}".format(
                q=q, exception=exception))
            
            raise
    
    
    ###RELATIONSHIP######################
    
    def create_friendship(self,F_json):
        
                                  
                                  
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._create_and_return_friendship,F_json)
            """"for record in result:
                print("Created friendship between: {p1}, {p2}".format(
                    p1=record['p1'], p2=record['p2']))"""

    @staticmethod
    def _create_and_return_friendship(tx,F_json ):

        with open(F_json) as file:
            db = json.load(file)
        
        for item in db['links']:
            #print(len(db['links']))
            rel=str(item["other"])
            
            vals="\""+str(item["source"])+"\""
            valt="\""+str(item["target"])+"\""
            """"q_verify_rel="MATCH (:Person {id: "+ str(vals)+"})-[r]->(:Person {id: "+ str(valt)+"})RETURN type(r) AS aa"
            res_verify=tx.run(q_verify_rel )
            out=0
            for record in res_verify:
                if record["aa"]==rel:
                    out=1
                    continue
            if out==1:
                continue
            """
            q= "MATCH  (p1:Person { id:"+str(vals)+" }) MATCH (p2:Person { id:"+str(valt)+" }) CREATE (p1)-[:"+rel+"]->(p2) RETURN p1, p2"
            query=(q) 
            #print("aa")
            result = tx.run(query )
            try:
                x=1
            except ServiceUnavailable as exception:
                    logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
                    raise
    def requestAll(tx):
        query = (
            "Match (n)-[r]->(m)"
            "Return n,r,m"
        )
        result = tx.run(query)
        return result




def insertCurrentGraph():
    scheme = "bolt"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687
    user = "neo4j"
    password = "test"
    print("creating connection")
    app = neo4jService(scheme,host_name,port, user, password)
    print("creating graph")
    app.create_NODE("Graph.json")
    app.create_friendship("Graph.json")
    #app.find_person("1192946702891790336")
    
    app.close()    

                    



if __name__ == "__main__":
    # See https://neo4j.com/developer/aura-connect-driver/ for Aura specific connection URL.
    scheme = "bolt"  # Connecting to Aura, use the "neo4j+s" URI scheme
    host_name = "localhost"
    port = 7687
    user = "neo4j"
    password = "test"
    print("creating connection")
    app = neo4jService(scheme,host_name,port, user, password)
    print("getting graph")
    print(app.requestAll())
    
    
    #app.find_person("1192946702891790336")
    
    app.close()