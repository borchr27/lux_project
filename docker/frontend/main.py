import http.server
import socketserver
import time
from PostgresDatabase import PostgresDatabase

def build_html():
    """! Connect to the database, get all items, close connection, build the html.
    """
    # conn = psql.connect()
    db = PostgresDatabase()
    db.connect()
    db.execute('SELECT * FROM quotes')
    result = db.cursor.fetchall()
    db.close()

    p = '<tr><td>Id</td><td>Author</td><td>Quote</td></tr>'

    for row in result:
        # for displaying an image
        # item = f'<tr><td>{row[0]}</td><td>{row[1]}</td><td><img src="{row[2]}" alt="" height=100 width=100 /></td>'
        item = f'<tr><td>{row[0]}   </td><td>{row[1]}       </td><td>{row[2]}</td>'
        p = p + item

    contents = f'''<!DOCTYPE html>
    <html>
    <body>
    <table>
    {p}
    </table>
    </body>
    </html>
    '''
    filename = 'index.html'
    return contents, filename

def main():
    """! Main function that opens the webpage. The while loop keeps the server running and repeatedly calls main().
    """
    contents, filename = build_html()
    output = open(filename,"w")
    output.write(contents)
    output.close()

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

while(True):
    # time.sleep(10)
    main()
    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    PORT = 8080
    my_server = socketserver.TCPServer(("", PORT), handler_object)
    # find site at localhost:8080 or 127.168.0.0:8080 in browser

    # Star the server
    my_server.serve_forever()