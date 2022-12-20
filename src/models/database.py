import sqlite3

class Database:
    def __init__(self) -> None:
        self.__db = sqlite3.connect("project.db")
    def setup(self):
        self.execute("CREATE table users (uid INTEGER PRIMARY KEY UNIQUE, email VARCHAR UNIQUE, password VARCHAR)")
        self.execute("INSERT INTO users (email,password) VALUES ('admin','aeadd64d34c8cdbdb0594366c811a803e7df4ad791f96c3190a39d86faff7c9b')")
        self.commit()
    def drop (self):
        self.execute("DROP Table users")
    def execute(self,query:str):
        return self.__db.execute(query) 
    def commit(self):
        return self.__db.commit()



