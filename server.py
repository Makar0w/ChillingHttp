import logging
import http.server
import socketserver
import os
import time
import threading
import argparse
from colorama import Fore, Back, Style
principal_title = '''
  |\'/-..--.
 / _ _   ,  ;
`~=`Y'~_<._./
 <`-....__.'  -Chilling Http- ( Debug Version )
 )
'''
print(principal_title)
parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Where the website template is located", default="static")
parser.add_argument("-p", type=int, help="Port That The Server will run on" , default="443")
args = parser.parse_args()
logging.basicConfig(filename='Log/serverweb.log', level=logging.INFO)
logger = logging.getLogger(__name__)
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)
STATIC_DIR = args.s
PORT = args.p
if PORT < 1024 :
    print(Back.RED + "WARNING : The server is running on a port under 1024 windows may stop the server from running",Back.BLACK +"")
if PORT == 0:
    print(Back.RED+"Port invalid !",Back.BLACK +"")
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Frame-Options', 'DENY') 
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()
        logger.info(MyHttpRequestHandler)
        logger.info("MyHttpRequestHandler has started !")

def main():
    os.chdir(STATIC_DIR)
    with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
        print("Server started at localhost:" + str(PORT))
        logger.info("Server started at localhost:" + str(PORT))
        log_thread = threading.Thread(target=thread_function, args=("LoggingThread",))
        log_thread.daemon = True
        log_thread.start()
        logger.warning('Deamon has started !')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            logger.error("I whant to say that this server is not secured line 24 , 23 there is only basic protection !")
            logger.critical("\nCRITICAL: Server stopped by Admin Input. This is for maintenance, upgrade, or due to an error.")
        

if __name__ == "__main__":
    main()
