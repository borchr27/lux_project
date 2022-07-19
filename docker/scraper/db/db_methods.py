import psycopg2

# pg_ctl -D /usr/local/var/postgres start
# pg_ctl -D /usr/local/var/postgres stop
# psql postgres

def connect():
    """! Connect to the postgres database.
    """
    conn = psycopg2.connect(
        # server = postgres
        database="maindb",
        user="docker",
        password="docker",
        host="postgres"
    )
    return conn

def create_flat_listed_table(conn):
    """! Open cursor and create table to store data.

    @param conn  Pass the connection to use to connect to the database
    """
    cur = conn.cursor()
    # build the table
    try:
        cur.execute("CREATE TABLE flat_listed (id serial not null, title text not null, image text not null);")
    except:
        print("WARNING: The table could not be created or the table has already been created.")
    
    cur.close()

def get_flat_listed_items(conn):
    """! Get request to retrieve all items from table

    @param conn  Pass the connection to use to connect to the database
    """
    # open cursor to perform db operations
    cur = conn.cursor()

    cur.execute("SELECT * FROM flat_listed")
    rows = cur.fetchall()

    if not len(rows):
        print("the table is empty!")
    
    cur.close()
    return rows

def post_flat_listed(conn, title, image):
    """! Method to post a single item into the database

    @param conn  Pass the connection to use to connect to the database
    
    @param title  The title of the item

    @param image  The image of the itme 
    """
    # preprocessing
    title = title.replace("\'"," ")
    image = image.replace("\'"," ") 
    
    # open cursor to perform db operations
    cur = conn.cursor()

    try:
        cur.execute(f"INSERT INTO flat_listed (title, image) VALUES  ('{title}', '{image}');")
    except:
        print("ERROR: file could not be inserted!")
    
    cur.close()