
import socketserver


def start_server():
    '''start the server and accept requests from the form'''

    PORT = 8000
    with socketserver.TCPServer(('127.0.0.1', PORT), Handler) as s:
        print(f'Server running and listening on port {PORT}...\n')
        s.serve_forever() # this method will call do_POST upon invocation



if __name__ == "__main__":
    start_server()



# from app import app

# if __name__ == '__main__':
#     app.run(debug=True)