import BusinessLogic
from DataAccessLayer.database.databaseAccess import DatabaseAccess

def main():
    
    # Initialize DatabaseAccess
    db_access = DatabaseAccess()
    
    # Create a session to interact with the database
    session = db_access.getSession()
    db_access.queryMenu()
    
    # Close the session
    session.close()

if __name__ == "__main__":
    main()
