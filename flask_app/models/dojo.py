from flask_app.config.mysqlconnection import connectToMySQL
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_dojo( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojoninja').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojoninja').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_byid(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojoninja').query_db(query, data)
        return cls (results[0])

    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at , updated_at) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL('dojoninja').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE dojos SET( name ) VALUES ( %(name)s , NOW() , NOW() ) WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db( query, data )        