import psycopg2

# pg_ctl -D /usr/local/var/postgres start
# pg_ctl -D /usr/local/var/postgres stop
# psql postgres

def connect():
    # connect to the db 
    conn = psycopg2.connect(
        # server = postgres
        database="maindb",
        user="docker",
        password="docker",
        host="postgres"
    )
    return conn

def create_flat_listed_table(conn):
    # open cursor to perform db operations
    cur = conn.cursor()
    # build the table
    try:
        cur.execute("CREATE TABLE flat_listed (id serial not null, title text not null, image text not null);")
    except:
        print("ERROR: the table could not be created!")
    
    cur.close()

def get_flat_listed_items(conn):
    # open cursor to perform db operations
    cur = conn.cursor()

    cur.execute("SELECT * FROM flat_listed")
    rows = cur.fetchall()

    if not len(rows):
        print("the table is empty!")
    
    cur.close()
    return rows

def post_flat_listed(conn, title, image):
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