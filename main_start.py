from mysql_connection import *
from create_sql_tables import *
from populate_sql_tables import *
from query_api import *

# Main function


def main():

    # connect to mySQL DB
    dbConnection = mySQLConnection().createConnection()

    # create tables if needed
    tables = createTables().createTables()

    # get data

    # populate tables
    #populateTables().populateSQLTable()
    apiQuery = queryResult().queryResultMain()



if __name__ == "__main__":
    main()
