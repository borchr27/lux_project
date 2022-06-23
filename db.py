import psycopg2

# pg_ctl -D /usr/local/var/postgres start
# pg_ctl -D /usr/local/var/postgres stop
# psql postgres

def test_connection():
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

    # Close connection
    cur.close()
    conn.close()

test_connection()