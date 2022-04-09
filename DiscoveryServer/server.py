from http.server import SimpleHTTPRequestHandler, HTTPServer

class AllowCorsHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header('Access-Control-Allow-Origin', '*')
        return super(AllowCorsHandler, self).end_headers()

httpd = HTTPServer(("localhost", 8000), AllowCorsHandler)
httpd.serve_forever()

