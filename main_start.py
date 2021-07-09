from mysql_connection import *
from create_sql_tables import *
from populate_sql_tables import *
from query_api import *

# Main function


def main():

    # connect to mySQL DB
    print("########## CONNECT TO DATABASE ##########")
    print("Connecting to host server..")
    try:
        dbConnection = mySQLConnection().createConnection()
        print("Successfully connected to host server")
    except:
        print("**Error connecting to host server - Terminating Program")
        return

    # create tables if needed
    print("########## CREATE DATABASE TABLES ##########")
    tables = createTables().createTables()

    # get data and insert/populate tables
    print("########## GET DATA AND INSERT INTO DATABASE ##########")
    apiQuery = queryResult().queryResultMain()




if __name__ == "__main__":
    main()
