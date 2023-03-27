from sqlalchemy.orm import Session
from sqlalchemy import text
from sql import define_engine, create_table
from commandInsert.insertValue import Insert
from commandInsert.crud import Crud

class DB:
    def __init__(self):
        self.engine = define_engine()
        self.session = Session(self.engine)
        self.insert = Insert(self.session)
        self.crud = Crud(self.session, self.engine) 
    
    def create_tables(self):
        create_table(self.engine)  
    
    def insert_value(self):
        self.insert.insert()

    def create_op(self):
        self.crud.create()
    
    def read_op(self):
        self.crud.read()

    def update_op(self):
        self.crud.update()

    def delete_op(self):
        self.crud.delete()
    
    def drop_db(self):
        with self.engine.connect() as conn:
            conn.execute(text("DROP DATABASE IF EXISTS ecommerce"))
            conn.execute(text("CREATE DATABASE ecommerce"))

    
