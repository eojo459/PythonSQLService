from mysql_connection import *


class populateTables():

    def updateSQLTable(self, records, tableName):

        print("Updating table " + tableName + "..")

        # connect to database
        db = mySQLConnection().createConnection()

        # cursor
        cursor = db.cursor()

        # keep track of items we updated, do not clean them
        updatedIDList = []

        # update each record in the table, if it does not exist create it, else update it
        for record in records:
            
            query = '''
                    REPLACE INTO `%s`
                    SET Content_ID = '%s', Ranking = '%s', Content_Type = '%s', Movie_Title = %s, 
                        Overview = %s, Poster = '%s', Release_Date = '%s', Rating = '%s', 
                        Genres = '%s', Trailer = '%s', Providers = %s
            ''' % (tableName, record[0], record[1], record[2], repr(record[3]), repr(record[4]), record[5], record[6], record[7], record[8], record[9], repr(record[10]))
            
            updatedIDList.append(record[0]) # add id to updated list

            cursor.execute(query)

        # commit
        db.commit()

        updatedIDTuple = tuple(updatedIDList)
        
        # clean up table, delete items that were not recently inserted/updated -> delete items not in the updatedIDTuple
        print("Cleaning up " + tableName + "..")

        query = '''
                DELETE FROM `%s`
                WHERE Content_ID NOT IN %s
        ''' % (tableName, str(updatedIDTuple))

        cursor.execute(query)

        # commit
        db.commit()
        
        db.close()

