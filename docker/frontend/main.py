import http.server
import socketserver
import time
from db import db_methods as psql

def build_html():
    conn = psql.connect()
    if conn:
        print("Connected Successfully")
    else:
        print("Connection Not Established")
    result = psql.get_flat_listed_items(conn)
    conn.close()

    p = '<tr><td>Id</td><td>Title</td><td>Image</td></tr>'

    for row in result:
        item = f'<tr><td>{row[0]}</td><td>{row[1]}</td><td><img src="{row[2]}" alt="" height=100 width=100 /></td>'
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
    time.sleep(10)
    main()
    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    PORT = 8080
    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    my_server.serve_forever()