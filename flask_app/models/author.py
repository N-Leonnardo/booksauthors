from flask_app.config.mysqlconnection import connectToMySQL
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_author( cls , data ):
        query = "INSERT INTO authors ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('authorsbooks').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('authorsbooks').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors
    
    @classmethod
    def get_byid(cls, data:dict):
        query = "SELECT * FROM authors WHERE id = %(author_id)s;"
        results = connectToMySQL('authorsbooks').query_db(query, data)
        return cls (results[0])

    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL('authorsbooks').query_db(query, data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO authors ( name, created_at , updated_at) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL('authorsbooks').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE authors SET( name ) VALUES ( %(name)s , NOW() , NOW() ) WHERE id = %(id)s;"
        return connectToMySQL('authorsbooks').query_db( query, data )        