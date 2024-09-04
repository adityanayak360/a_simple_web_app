from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the hostname of the instance
    hostname = socket.gethostname()
    
    # Get the IP address of the instance
    ip_address = socket.gethostbyname(hostname)
    
    # Display "hello world from x" where x is the IP address
    return f"hello world from {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
