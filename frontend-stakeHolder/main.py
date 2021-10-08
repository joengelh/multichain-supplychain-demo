from website import create_app
import sys

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT), ssl_context='adhoc')
