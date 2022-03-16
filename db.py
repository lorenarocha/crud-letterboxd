import sqlalchemy
import pandas as pd
import os

#finding data path
PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
DB_NAME = input('Enter the database name you want to create:')
    
#open connection   
def open_conn():
    conn = sqlalchemy.create_engine('mysql+pymysql://root:admin@localhost/', echo=True)
    print('Connection created with MySQL')
    return conn


#print db list
def schemas(conn):
    inspect = sqlalchemy.inspect(conn)
    db_list = inspect.get_schema_names()
    return db_list


#create db
def create_use_db(conn, db_list):
    if DB_NAME in db_list:
        conn.execute(f'USE {DB_NAME}')
        print('Database already exists')
    else:        
        conn.execute(f'CREATE DATABASE {DB_NAME}')
        conn.execute(f'USE {DB_NAME}')
    return ('Database created') 


#list files
def files(path):
    return [ os.path.join(path, i) for i in os.listdir(path) if i.endswith('.csv') ]
        
 
#read files
def read_file(file, conn):
    table_name = file.split('\\')[-1].replace('.csv', '').split('\\')[-1]
    print(table_name)
    #insert values
    df = pd.read_csv(file)
    df.to_sql(table_name, conn, index=False)
    

def read_all(files, conn):
    for f in files:
        read_file(f,conn)


def main():
    conn = open_conn()
    db_list = schemas(conn)
    create_use_db(conn, db_list)
    file = files(PATH)
    read_all(file, conn)
    

if __name__ == '__main__':
    main()