from sqlalchemy import create_engine, inspect
from sqlalchemy import text

import os

DATABASE_URL="postgresql://new_d1ux_user:9A3mcbEEuKsgBUHJcyj1RvkZa050EjPu@dpg-d0k293vfte5s7389i9og-a.singapore-postgres.render.com/new_d1ux"
engine = create_engine(DATABASE_URL,  client_encoding='utf8')

connection = engine.connect()
asd = inspect(engine) 


print (asd.get_table_names())


result = connection.execute(
    text("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task VARCHAR(255) NOT NULL,
            deadline DATE NOT NULL,
            user_ VARCHAR(255) NOT NULL,
            FOREIGN KEY (user_) REFERENCES users(username) ON DELETE CASCADE
        );
    """)
)



print( result )

x = connection.execute(
    text("""INSERT INTO users (username, password) VALUES ('Honey','Pabololot');""")
)



q = connection.execute(
    text(""" SELECT * FROM users
    ;"""))

print(q.mappings().all())
print(q.fetchall())


connection.commit()
