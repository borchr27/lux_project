import psycopg2

# pg_ctl -D /usr/local/var/postgres start
# pg_ctl -D /usr/local/var/postgres stop
# psql postgres

def connect():
    """! Connect to the postgres database. To view the database or debug open up the shell for the 
    database image then use the 'psql -U docker maindb' command to enter into the database bash. Then
    use the '\l' command to list the databases. Then you can use the command 'SELECT * FROM flat_listed limit 10;'
    to view the items in the db.
    """
    conn = psycopg2.connect(
        # server = postgres
        database="postgres",
        user="postgres",
        password="postgres",
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
        cur.execute("CREATE TABLE IF NOT EXISTS flat_listed (id serial not null, title text not null, image text not null);")
    except:
        print("WARNING: The table could not be created or the table has already been created.")
    
    cur.close()

def flat_listed_table_exists(conn, name):
    """! Open cursor search for table with name parameter and return boolean value describing if table exists.

    @param conn  Pass the connection to use to connect to the database

    @param name  The name of the table to look for

    @return   Returns a boolean value describing if the table exists or not
    """
    exists = False
    cur = conn.cursor()
    cur.execute(f"SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename = '{name}');")
    exists = cur.fetchone()[0]
    cur.close()
    return bool(exists)

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

def post_flat_listed(conn, item):
    """! Method to post a single item into the database

    @param conn  Pass the connection to use to connect to the database
    
    @param title  The title of the item

    @param image  The image of the itme 
    """
    # preprocessing
    title = item['title'].replace("\'"," ")
    image = item['image'].replace("\'"," ") 
    
    # open cursor to perform db operations
    cur = conn.cursor()

    try:
        cur.execute(f"INSERT INTO flat_listed (title, image) VALUES  ('{title}', '{image}');")
    except:
        print("ERROR: file could not be inserted!")
    
    cur.close()