import dataclasses
import time
import http
import multiprocessing
import tired.logging


@dataclasses.dataclass
class TimeoutConfiguration:
    timeout_seconds_post: float
    """ Timeout that simulates processing of POST responses """

    timeout_seconds_get: float
    """ Timeout that simulates processing of GET responses """

    uri: str
    """ REST address """

    port: int = 8080
    """ Port on which to run """


class TimeoutPostGetHandler(http.BaseHTTPRequestHandler):
    """ Imitates REST API """

    def __init__(self, configuration: TimeoutConfiguration):
        self._configuration = configuration

    def do_GET(self):
        time.sleep(self._configuration.timeout_seconds_get)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        time.sleep(self._configuration.timeout_seconds_post)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))


class MultiprocessingTimeoutServer(multiprocessing.Process, http.HTTPServer):
    """
    POST / GET processing simulating server that runs in a separate process.

    Use `<instance>.start()` to start a new process, and `<instance>.join() to
    wait for completion , or `<instance>.serve_forever()` to run the server in
    the current process.
    """
    def __init__(self, configuration: TimeoutConfiguration):
        self._handler = TimeoutPostGetHandler(configuration)
        self._configuration = configuration
        multiprocessing.Process.__init__(self, target=self.serve_forever)
        http.HTTPServer.__init__((self._configuration.uri, self._configuration.port), self._handler)

