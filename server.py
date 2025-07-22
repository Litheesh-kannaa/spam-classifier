from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from model.spam_classifier import classify_email

class SpamHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Respond to preflight CORS request
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = parse_qs(post_data.decode('utf-8'))

        email = parsed_data.get('email', [''])[0]
        result = classify_email(email)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")  # 👈 allow all origins
        self.end_headers()
        self.wfile.write(result.encode())

httpd = HTTPServer(('localhost', 8000), SpamHandler)
print(">> Server running on http://localhost:8000")
httpd.serve_forever()
