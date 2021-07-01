from mysql_connection import *


class populateTables():

    def populateSQLTable(self):

        # connect to database
        db = mySQLConnection().createConnection()

        # cursor
        cursor = db.cursor()

        # populate tables
        #queryResult().queryResultMain()

    def insertSQLTable(self, records, tableName):

        try:
            # connect to database
            db = mySQLConnection().createConnection()

            # cursor
            cursor = db.cursor()
                    
            # INSERT query
            '''
            query = """
                INSERT INTO `ALL-Movies` (
                    Content_ID, 
                    Ranking, 
                    Content_Type, 
                    Movie_Title, 
                    Overview, 
                    Poster, 
                    Release_Date, 
                    Rating, 
                    Genres, 
                    Trailer, 
                    Providers)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            '''

            # insert each record into the sql tableName
            query = "INSERT INTO `" + tableName + "` "
            query += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            # execute query on records
            cursor.executemany(query, records)

            # commit
            db.commit()
            db.close()

        except:
            return
