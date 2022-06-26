import http
import socketserver
# from db import db_methods as psql

# def build_html():
#     conn = psql.connect()

#     if conn:
#         print ("Connected Successfully")
#     else:
#         print ("Connection Not Established")

#     result = psql.get_flat_listed_items(conn)

#     conn.close()

#     p = []
#     tbl = "<tr><td>ID</td><td>Title</td><td>Image</td></tr>"
#     p.append(tbl)

#     for row in result:
#         a = "<tr><td>%s</td>"%row[0]
#         p.append(a)
#         b = "<td>%s</td>"%row[1]
#         p.append(b)
#         c = "<td>%s</td>"%row[2]
#         p.append(c)

#     contents = '''<!DOCTYPE html>
#     <html>
#     <head>
#     <title>Scraped Website Data</title>
#     </head>
#     <body>
#     <table>
#     %s
#     </table>
#     </body>
#     </html>
#     '''%(p)

#     filename = 'index.html'
#     return contents, filename

# def main():
#     contents, filename = build_html()
#     output = open(filename,"w")
#     output.write(contents)
#     output.close()

# main()  

###############
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()