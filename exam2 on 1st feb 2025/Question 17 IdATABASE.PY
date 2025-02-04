from abc import ABC, abstractmethod
# Define the abstract class
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass
    @abstractmethod
    def update(self, data):
        pass
    @abstractmethod
    def delete(self, data):
        pass
# Implement the SQLDatabase class
class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        return f"SQL: Inserting {data} into the database."
    def update(self, data):
        return f"SQL: Updating {data} in the database."
    def delete(self, data):
        return f"SQL: Deleting {data} from the database."
# Implement the NoSQLDatabase class
class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        return f"NoSQL: Inserting {data} into the database."
    def update(self, data):
        return f"NoSQL: Updating {data} in the database."
    def delete(self, data):
        return f"NoSQL: Deleting {data} from the database."
# Create instances of SQLDatabase and NoSQLDatabase
sql_db = SQLDatabase()
nosql_db = NoSQLDatabase()
# Perform database operations
print(sql_db.insert("user data"))
print(sql_db.update("user data"))
print(sql_db.delete("user data"))
print(nosql_db.insert("document"))
print(nosql_db.update("document"))
print(nosql_db.delete("document"))
