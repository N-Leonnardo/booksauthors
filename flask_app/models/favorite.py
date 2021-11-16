from flask_app.config.mysqlconnection import connectToMySQL
class Favorite:
    def __init__( self , data ):
        self.book_id = data['book_id']
        self.author_id = data['author_id']

    @classmethod
    def save_favorite( cls , data ):
        query = "INSERT INTO favorite ( book_id, author_id ) VALUES (%(book_id)s,%(author_id)s);"
        return connectToMySQL('authorsbooks').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors JOIN favorite ON authors.id = favorite.author_id JOIN books ON books.id = favorite.book_id;"
        results = connectToMySQL('authorsbooks').query_db(query)
        favorites = []
        for favorite in results:
            favorites.append( cls(favorite) )
        return favorites
    
    @classmethod
    def get_from_author(cls, data:dict):
        query = "SELECT * FROM authors JOIN favorite ON authors.id = favorite.author_id JOIN books ON books.id = favorite.book_id WHERE author_id = %(author_id)s"
        results = connectToMySQL('authorsbooks').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas


    # @classmethod
    # def get_byid(cls, data:dict):
    #     query = "SELECT * FROM authors JOIN favorite ON authors.id = favorite.author_id JOIN books ON books.id = favorite.book_id WHERE author_id = %(author_id)s;"
    #     results = connectToMySQL('authorsbooks').query_db(query, data)
    #     favorites = []
    #     for favorite in results:
    #         favorites.append(cls(favorite))
    #     return favorites


    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM favorite WHERE book_id = %(book_id)s AND author_id = %(author_id)s;"
        return connectToMySQL('authorsbooks').query_db(query, data)

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO favorite ( name, created_at , updated_at) VALUES ( %(name)s, NOW() , NOW() );"
    #     return connectToMySQL('authorsbooks').query_db( query, data )

    # @classmethod
    # def update(cls, data ):
    #     query = "UPDATE authors SET( name ) VALUES ( %(name)s , NOW() , NOW() ) WHERE id = %(id)s;"
    #     return connectToMySQL('authorsbooks').query_db( query, data )        