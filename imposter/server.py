import dataclasses
import time
import http
import http.server
import multiprocessing
import tired.logging


@dataclasses.dataclass
class TimeoutConfiguration:
    timeout_seconds_post: float = 0.001
    """ Timeout that simulates processing of POST responses """

    timeout_seconds_get: float = 0.001
    """ Timeout that simulates processing of GET responses """

    uri: str = '/'
    """ REST address """

    port: int = 8080
    """ Port on which to run """


class TimeoutPostGetHandler(http.server.BaseHTTPRequestHandler):
    """ Imitates REST API """

    def __init__(self, *args, **kwargs):
        configuration = TimeoutConfiguration()
        self._configuration = configuration
        http.server.BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self):
        time.sleep(self._configuration.timeout_seconds_get)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Served GET"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        time.sleep(self._configuration.timeout_seconds_post)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Served POST"
        self.wfile.write(bytes(message, "utf8"))

