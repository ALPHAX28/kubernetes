from http.server import BaseHTTPRequestHandler, HTTPServer

class Server2Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello from Server2\n')

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8080), Server2Handler)
    print("Server2 running on port 8080")
    httpd.serve_forever()
