from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser, threading, os

ROOT = Path(__file__).resolve().parent
PORT = 8000
os.chdir(ROOT)

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-store')
        super().end_headers()

if __name__ == '__main__':
    url=f'http://127.0.0.1:{PORT}/'
    print('\nSistema de Papayuela iniciado en:', url)
    print('Para detenerlo presione Ctrl+C.\n')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    ThreadingHTTPServer(('127.0.0.1',PORT), Handler).serve_forever()
