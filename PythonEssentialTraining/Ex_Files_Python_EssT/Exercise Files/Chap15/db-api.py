#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# The python database API provides a common interface for various database engines. Is a consolidated interface for a number of database systems. Every database engine has its own interface, its own requirements and its own paradigms. No single interface will serve them all equally.

# The DB will be fully contained in one file. This file is completely portable. I can use it in mac, windows, linux, etc. I can interface with any sqlite driver in any language and use that file. 

import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('db-api.db') # This returns a DB handle to manipulate it.
    cur = db.cursor() # First we grab a cursos from the DB handle. This is a paradigm that allow us to keep track of where we are in the DB.
    print('create')
    cur.execute("DROP TABLE IF EXISTS test") # We will drop a table if it exists.
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    # Now we are going to insert a row with the "STRING TEXT" and "NUMBER INTEGER" (3 rows are inserted)
    # From here
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    #To here. After inserting we commit our changes. 
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
