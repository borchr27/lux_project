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

def connect():
    # connect to the db 
    conn = psycopg2.connect(
        # server = database
        database="maindb",
        user="docker",
        password="docker",
        host="0.0.0.0"
    )
    return conn

def create_flat_listed_table(conn):
    # open cursor to perform db operations
    cur = conn.cursor()

    # query the db
    cur.execute("CREATE TABLE flat_listed ( \
        flat_listed_id serial PRIMARY KEY, \
        title VARCHAR ( 100 ) NOT NULL, \
        image NVARCHAR ( MAX ) NOT NULL);" )

    cur.close()

def get_flat_listed_items(conn):
    # open cursor to perform db operations
    cur = conn.cursor()

    cur.execute("SELECT * FROM flat_listed")
    rows = cur.fetchall()

    if not len(rows):
        print("the table is empty!")
    else:
        for row in rows:
            print(row)
    
    cur.close()

def post_flat_listed(conn, title, image):
    # open cursor to perform db operations
    cur = conn.cursor()

    try:
        cur.execute(f"INSERT INTO flat_listed (title, image) VALUES ({title}, {image})")
    except:
        print("ERROR: file could not be inserted!")
    
    cur.close()