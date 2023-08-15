import psycopg2

# pg_ctl -D /usr/local/var/postgres start
# pg_ctl -D /usr/local/var/postgres stop
# psql postgres

# DOCKER HELP BELOW
# psql -U postgres                  :: in terminal in docker container
# \dt                               :: to see tables
# SELECT COUNT(*) FROM table_name;  :: to see number of rows in table
# TRUNCATE table_name               :: to delete all rows in table

class PostgresDatabase:
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def connect(self):
        """! Connect to the postgres database. To view the database or debug open up the shell for the 
        database image then use the 'psql -U docker maindb' command to enter into the database bash. Then
        use the '\l' command to list the databases. Then you can use the command 'SELECT * FROM sites limit 10;'
        to view the items in the db.
        """
        try:
            conn = psycopg2.connect(
                # server = postgres
                database="postgres",
                user="postgres",
                password="postgres",
                host="postgres"
            )
            self.connection = conn
        except:
            pass

    def close(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def commit(self) -> None:
        if self.connection:
            self.connection.commit()

    def execute(self, command, values=None) -> None:
        if self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.execute(command, values)

    def number_of_quotes(self) -> int:
        if self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.execute('SELECT * FROM sites')
        return self.cursor.rowcount