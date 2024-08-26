from http.server import BaseHTTPRequestHandler, HTTPServer

class Server1Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello from Server1\n')

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8080), Server1Handler)
    print("Server1 running on port 8080")
    httpd.serve_forever()
