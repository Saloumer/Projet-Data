import sqlite3

class Database:
    def __init__(self) -> None:
        self.__db = sqlite3.connect("project.db")
    def setup(self):
        self.execute("CREATE table users (uid INTEGER PRIMARY KEY UNIQUE, email VARCHAR UNIQUE, password VARCHAR)")
        self.execute("INSERT INTO users (email,password) VALUES ('admin','admin')")
        self.commit()
    def drop (self):
        self.execute("DROP Table users")
    def execute(self,query:str):
        return self.__db.execute(query) 
    def commit(self):
        return self.__db.commit()



    