from database.databaseAccess import DatabaseAccess

def main():
    # Database connection string
    connection_string = 'mysql+mysqlconnector://root:*Sinh08062004*@localhost/OSPS'
    
    # Initialize DatabaseAccess
    db_access = DatabaseAccess(connection_string)
    
    # Create a session to interact with the database
    session = db_access.getSession()
    db_access.queryMenu()
    
    # Close the session
    session.close()

if __name__ == "__main__":
    main()
