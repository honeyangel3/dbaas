from sqlalchemy import create_engine, inspect
from sqlalchemy import text

import os

DATABASE_URL="postgresql://exam_repo_user:Qa5oxTi8pC2MdeJ2G4RFm4aGpcnlLixk@dpg-cvsrfc49c44c73c4kk10-a.singapore-postgres.render.com/exam_repo"
engine = create_engine(DATABASE_URL,  client_encoding='utf8')

connection = engine.connect()
asd = inspect(engine) 


print (asd.get_table_names())


result = connection.execute(
    text("""CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL;
         
    CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    deadline DATE NOT NULL,
    user VARCHAR(255) NOT NULL,
    FOREIGN KEY (user) REFERENCES users(username) ON DELETE CASCADE);
);"""))


print( result )

x = connection.execute( 
text("""INSERT INTO users (username, password) VALUES ('IAN','MACALISANG');
;"""))


q = connection.execute(
    text(""" SELECT * FROM users
    ;"""))

print(q.mappings().all())
print(q.fetchall())


connection.commit()