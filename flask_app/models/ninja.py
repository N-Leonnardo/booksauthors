from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojoninja').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def get_from_dojo(cls, data:dict):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojoninja').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas


    @classmethod
    def get_byid(cls, data:dict):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojoninja').query_db(query, data)
        return cls (results[0])

    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name, last_name , age, created_at , updated_at, dojo_id ) VALUES (%(fname)s, %(lname)s, %(age)s,NOW(),NOW(),%(dojo_id)s);"
        return connectToMySQL('dojoninja').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE ninjas SET( first_name, last_name , age, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s,NOW(),NOW()) WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db( query, data )        