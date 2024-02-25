import argparse
import http
import http.server
import imposter.server
import socketserver
import tired.logging


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout-get', type=float, default=0.001, help="Timeout to server GET requests (in seconds)")
    parser.add_argument('--timeout-post', type=float, default=0.001, help="Timeout to server POST requests (in seconds)")
    parser.add_argument('--uri', default='/', help="Rest API URI")
    parser.add_argument('--port', default=8080, help="TCP port", type=int)

    return parser.parse_args()


def main():
    args = parse_arguments()
    configuration = imposter.server.TimeoutConfiguration(
        timeout_seconds_post=args.timeout_post,
        timeout_seconds_get=args.timeout_get,
        uri=args.uri,
        port=args.port
    )

    with socketserver.TCPServer(("", configuration.port), imposter.server.TimeoutPostGetHandler.make_constructor_wrapper(configuration)) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
