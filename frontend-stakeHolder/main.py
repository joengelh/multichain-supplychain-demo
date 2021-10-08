from website import create_app
import sys

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004) #, ssl_context='adhoc')
