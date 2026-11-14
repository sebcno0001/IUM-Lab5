from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def main():
    handler = partial(SimpleHTTPRequestHandler, directory="/results")
    server = ThreadingHTTPServer(("0.0.0.0", 8080), handler)
    print("Wyniki dostępne na porcie 8080", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
