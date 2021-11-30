from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path_folder = "data"
        abs_file_path = os.path.join(os.path.join(script_dir, rel_path_folder), 'mydata.json')
        
        with open(abs_file_path, 'r') as f:
            self.wfile.write(f.read().encode("utf8"))
        #message = "{ 'Hello': 'World!' }"
        #self.wfile.write(bytes(message, "utf8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()