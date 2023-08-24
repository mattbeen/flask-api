from app import create_app
from config import api_port,api_host

app = create_app()

if __name__ == '__main__':
    port = api_port
    app.run(host=api_host,port=api_port,debug=True)