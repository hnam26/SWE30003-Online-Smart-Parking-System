from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import threading
from tabulate import tabulate
from .models import Base
from datetime import datetime


class DatabaseAccess:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, connection_string='mysql+mysqlconnector://root:*Sinh08062004*@localhost/OSPS'):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(DatabaseAccess, cls).__new__(cls)
                cls.__instance.engine = create_engine(connection_string)
                cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
                # Ensure the metadata is created using the imported Base
                Base.metadata.create_all(cls.__instance.engine)
                print("Database connection established")
            return cls.__instance

    def getSession(self):
        return self.Session()

    def close(self):
        if self.__instance and self.__instance.engine:
            self.__instance.engine.dispose()
            print("Database connection closed")

    def queryMenu(self):
        session = self.getSession()
        try:
            while True:
                print("\nQuery Menu:")
                print("1. Execute a SQL query")
                print("2. Logout")
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.queryDatabase(session)
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def queryDatabase(self, session):
        try:
            sqlQuery = input("Enter your SQL query: ")
            result = session.execute(text(sqlQuery))
            columns = result.keys()
            rows = []
            for row in result:
                formattedRow = [value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, datetime) else value
                                for value in row]
                rows.append(formattedRow)
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
