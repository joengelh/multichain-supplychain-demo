from website import create_app
import sys

#get port and name from arguments
print("Give name of client as first, port as second argument like python3 frontend-shareHolder/main.py oem 5004")
NAME = sys.argv[1]
PORT = sys.argv[2]

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT), ssl_context='adhoc')
